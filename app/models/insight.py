from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.session import Base

class Insight(Base):
    __tablename__ = "insights"

    id = Column(Integer, primary_key=True)
    content = Column(String)
    confidence = Column(String)
    category = Column(String)

    report_insights = relationship("ReportInsightMap", back_populates="insight")
