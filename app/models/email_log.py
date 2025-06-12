from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from app.database.session import Base

class EmailLog(Base):
    __tablename__ = "email_logs"

    id = Column(Integer, primary_key=True)
    to_email = Column(String)
    report_id = Column(Integer, ForeignKey("reports.id"))
    status = Column(String)
    error_message = Column(String, nullable=True)
    smtp_code = Column(String, nullable=True)
    bounce_type = Column(String, nullable=True)
    opened = Column(String, nullable=True)
    clicked = Column(String, nullable=True)
    sent_at = Column(DateTime, default=func.now())
