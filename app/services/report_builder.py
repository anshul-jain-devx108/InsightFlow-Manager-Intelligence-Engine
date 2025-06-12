from sqlalchemy.orm import Session
from app.models import Report, ReportInsightMap, Insight

def build_report(db: Session, employee, manager, insights: list):
    report = Report(
        employee_id=employee.id,
        manager_id=manager.id,
        version="1.0"
    )
    db.add(report)
    db.flush()

    for insight in insights:
        # Save or reuse the insight
        db.add(insight)
        db.flush()

        mapping = ReportInsightMap(report_id=report.id, insight_id=insight.id)
        db.add(mapping)

    db.commit()
    return report
