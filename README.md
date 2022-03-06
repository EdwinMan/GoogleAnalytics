# GoogleAnalytics

The project is connected to Google Analytics Reporting V4. and it is using the FastAPI python framework.

make sure those packages are installed at your machine or a virtual environment:
1- pip install --upgrade google-api-python-client
2- pip install oauth2client
3- pip install pandas
4- pip install fastapi

to be able to run the application navigate into the project and run the command: uvicorn index:app.

the project is a python API that will call reporting data from Google Analytics Reporting V4 using the specified metrics and dimensions:

metrics: ga:users, ga:sessions, ga:avgSessionDuration, ga:pageviewsPerSession, ga:bounceRate, ga:avgTimeOnPage.
dimensions: ga:date, ga:pagePath, ga:country, ga:city, ga:browser.

The API has 1 Get request that will return the Data Frame as JSON object, and it will create a CSV file and will save it on the backend folder
