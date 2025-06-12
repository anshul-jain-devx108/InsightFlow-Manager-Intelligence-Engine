from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.report import Report
from app.services.email_sender import send_email_report

router = APIRouter()

@router.post("/send/{report_id}")
def send_report_email(report_id: int, db: Session = Depends(get_db)):
    report = db.query(Report).filter_by(id=report_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    send_email_report(report, db)

    return {"message": f"Email sent to manager for report ID {report_id}"}
