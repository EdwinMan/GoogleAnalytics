# from fastapi import FastAPI
from report import Reporting

# app = FastAPI()

report = Reporting()
return report.getReport()

# @app.get("/")
# async def downloadCSV():
#     report = Reporting()
#     return report.getReport()