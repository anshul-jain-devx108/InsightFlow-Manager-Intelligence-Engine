from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.email_log import EmailLog
from app.schemas.email_log import EmailLogOut

router = APIRouter(prefix="/email-logs", tags=["Email Logs"])

@router.get("/", response_model=list[EmailLogOut])
def get_email_logs(db: Session = Depends(get_db)):
    """
    Fetch all email logs (sent, failed, pending).
    """
    return db.query(EmailLog).order_by(EmailLog.sent_at.desc()).all()

