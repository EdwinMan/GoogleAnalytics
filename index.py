from fastapi import FastAPI
from report import Reporting

app = FastAPI()

@app.get("/")
async def downloadCSV():
    report = Reporting()
    return report.getReport()