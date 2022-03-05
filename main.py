from fastapi import FastAPI
from index import Reporting

app = FastAPI()


@app.get("/")
async def downloadCSV():
    report = Reporting()
    print(report.getReport())
    return report.getReport()