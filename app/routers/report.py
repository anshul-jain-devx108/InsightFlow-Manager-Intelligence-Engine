from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, List

from app.database.session import get_db
from app.models import Employee
from app.services.insight_generator import generate_insights
from app.services.report_builder import build_report
from app.services.email_sender import send_email_report  

router = APIRouter()


class GenerateReportRequest(BaseModel):
    employee_id: Optional[int] = None


class GenerateReportResponse(BaseModel):
    message: str
    report_ids: List[int]


@router.post("/generate/", response_model=GenerateReportResponse)
def generate_reports(
    request: GenerateReportRequest = Body(default=None),
    db: Session = Depends(get_db)
):
    report_ids = []

    if request and request.employee_id:
        employee = db.query(Employee).filter_by(id=request.employee_id).first()
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        if not employee.employee_managers:
            raise HTTPException(status_code=400, detail="No manager assigned")

        manager = employee.employee_managers[0].manager
        insights = generate_insights(employee)
        report = build_report(db, employee, manager, insights)
        report_ids.append(report.id)

      
        try:
            send_email_report(report, db)
        except Exception as e:
            print(f"Failed to send email for report ID {report.id}: {str(e)}")

        return {"message": "Report generated and email sent for one employee", "report_ids": report_ids}

    else:
       
        employees = db.query(Employee).all()
        for emp in employees:
            if not emp.employee_managers:
                continue
            manager = emp.employee_managers[0].manager
            insights = generate_insights(emp)
            report = build_report(db, emp, manager, insights)
            report_ids.append(report.id)

            try:
                send_email_report(report, db)
            except Exception as e:
                print(f"Failed to send email for report ID {report.id}: {str(e)}")

        return {"message": f"Reports generated and emails sent for {len(report_ids)} employees", "report_ids": report_ids}
