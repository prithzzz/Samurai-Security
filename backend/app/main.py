from fastapi import FastAPI
from app.routes.report_route import router as report_router
from app.routes.scan_route import router as scan_router   
from app.routes.evaluation_route import router as evaluation_router   
from app.routes.approval_route import router as approval_router  
app = FastAPI()

app.include_router(scan_router)   
app.include_router(evaluation_router)  
app.include_router(report_router)
app.include_router(approval_router) 


@app.get("/")
def root():
    return {"message": "Model Scanner Running"}