from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.session import Base

class ReportLog(Base):
    __tablename__ = "report_logs"

    id = Column(Integer, primary_key=True, index=True)
    manager_id = Column(Integer, ForeignKey("managers.id"))
    generated_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="success")
    insights_summary = Column(String, nullable=True)

    manager = relationship("Manager", back_populates="report_logs")
