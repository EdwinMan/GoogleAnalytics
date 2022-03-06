# Google Analytics

### The project is connected to Google Analytics Reporting V4. and it is using the FastAPI python framework.
---

*To be able to run the project on your machine, **I need to provide you with the client_secret.json credentials. otherwise, the application will not run.***

*make sure those packages are installed at your machine or a virtual environment*:
- `pip install --upgrade google-api-python-client`
- `pip install oauth2client`
- `pip install pandas`
- `pip install fastapi`

to be able to run the application navigate into the project and run the command: `uvicorn index:app`.

---

the project is a python API that will call reporting data from **Google Analytics Reporting V4** using the specified metrics and dimensions:

### metrics
- ga:users
- ga:sessions
- ga:avgSessionDuration
- ga:pageviewsPerSession
- ga:bounceRate
- ga:avgTimeOnPage.
### dimensions
- ga:date 
- ga:pagePath
- ga:country
- ga:city 
- ga:browser

---

*The API has 1 Get request that will return the Data Frame as JSON object, and it will create a CSV file and will save it on the backend folder. **Please Check the report.csv to see the result of the code.***
