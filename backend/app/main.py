from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # ✅ add this
from app.routes.report_route import router as report_router
from app.routes.scan_route import router as scan_router   

app = FastAPI()

# ✅ CORS (VERY IMPORTANT for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ existing routers
app.include_router(report_router)
app.include_router(scan_router)

# ✅ NEW scan route (temporary / fallback)
@app.post("/scan")
def scan(data: dict):
    return {"status": "success", "data": data}

@app.get("/")
def root():
    return {"message": "Model Scanner Running"}