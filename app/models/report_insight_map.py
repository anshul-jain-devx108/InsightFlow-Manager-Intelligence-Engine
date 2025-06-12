from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database.session import Base

class ReportInsightMap(Base):
    __tablename__ = "report_insight_map"

    id = Column(Integer, primary_key=True)
    report_id = Column(Integer, ForeignKey("reports.id"))
    insight_id = Column(Integer, ForeignKey("insights.id"))

    report = relationship("Report", back_populates="report_insights")
    insight = relationship("Insight", back_populates="report_insights")
