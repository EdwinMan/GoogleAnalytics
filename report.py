from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import httplib2
import pandas as pd
import numpy as np


class Reporting:

    service = None

    def __init__(self):
        # Create service credentials
        credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secrets.json', [
            'https://www.googleapis.com/auth/analytics.readonly'])
        # Create a service object
        http = credentials.authorize(httplib2.Http())
        self.service = build('analytics', 'v4', http=http,
                             discoveryServiceUrl='https://analyticsreporting.googleapis.com/$discovery/rest')

    def format_summary(self, res):
        try:
            # create row index
            try:
                row_index_names = res['reports'][0]['columnHeader']['dimensions']
                row_index = [element['dimensions'] for element in res['reports'][0]['data']['rows']]
                row_index_named = pd.MultiIndex.from_arrays(np.transpose(np.array(row_index)),
                                                            names=np.array(row_index_names))

            except:
                row_index_named = None

            # extract column names
            summary_column_names = [item['name'][3:] for item in res['reports'][0]
            ['columnHeader']['metricHeader']['metricHeaderEntries']]

            # extract table values
            summary_values = [element['metrics'][0]['values'] for element in res['reports'][0]['data']['rows']]

            # combine. I used type 'float' because default is object, and as far as I know, all values are numeric
            df = pd.DataFrame(data=np.array(summary_values),
                              index=row_index_named,
                              columns=summary_column_names).astype('float')

        except:
            df = pd.DataFrame()

        return df

    def getReport(self):
        
        # setting up the metrics and dimensions of the request.
        response = self.service.reports().batchGet(
            body={
                'reportRequests': [
                    {
                        'viewId': '262094784',
                        'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                        'metrics': [
                            {'expression': 'ga:users'},
                            {'expression': 'ga:sessions'},
                            {'expression': 'ga:avgSessionDuration'},
                            {'expression': 'ga:pageviewsPerSession'},
                            {'expression': 'ga:bounceRate'},
                            {'expression': 'ga:avgTimeOnPage'}
                        ],
                        'dimensions': [
                            {"name": "ga:date"},
                            {"name": "ga:pagePath"},
                            {"name": "ga:country"},
                            {"name": "ga:city"},
                            {"name": "ga:browser"}
                        ],
                        'pageSize': 10000
                    }]
            }
        ).execute()
        
        # convert the response to a Data Frame
        df = self.format_summary(response)
        
        # save a csv file of the result in folder
        df.to_csv("reprot.csv")
        
        return df.to_json(orient = 'columns')
