from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import upload, report, email, employee  # ✅ add `employee`
from app.scheduler.jobs import run_scheduled_jobs
from app.database.init_db import init_db
from app.routers import email_log
# Initialize database
init_db()

# Initialize FastAPI app
app = FastAPI(
    title="People Insights API",
    description="Automated insights and email reporting system for People Managers",
    version="1.0.0"
)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(upload.router, prefix="/upload", tags=["Upload CSV"])
app.include_router(report.router, prefix="/report", tags=["Generate Report"])
app.include_router(email.router, prefix="/email", tags=["Send Emails"])
app.include_router(employee.router, prefix="/employee", tags=["Employee CRUD"])  # ✅ register here
app.include_router(email_log.router)
# Start background job scheduler
run_scheduled_jobs()
