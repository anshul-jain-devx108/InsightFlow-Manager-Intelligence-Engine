from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, func
from sqlalchemy.orm import relationship
from app.database.session import Base

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    manager_id = Column(Integer, ForeignKey("managers.id"))
    generated_at = Column(DateTime, default=func.now())
    duration = Column(String)
    version = Column(String)

    employee = relationship("Employee", back_populates="reports")
    manager = relationship("Manager", back_populates="reports")
    report_insights = relationship("ReportInsightMap", back_populates="report")
