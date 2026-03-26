from fastapi import FastAPI
from app.routes.report_route import router as report_router

app = FastAPI()

app.include_router(report_router)

@app.get("/")
def root():
    return {"message": "Model Scanner Running"}