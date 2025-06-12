# # app/routers/report.py

# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from pydantic import BaseModel
# from app.database.session import get_db
# from app.models import Employee, Manager, Report, Insight, ReportInsightMap
# from app.services.insight_generator import generate_insights
# from app.services.report_builder import build_report

# router = APIRouter()


# # Response schema for FastAPI docs
# class ReportResponse(BaseModel):
#     message: str
#     report_id: int


# @router.post("/generate/{employee_id}", response_model=ReportResponse)
# def generate_employee_report(employee_id: int, db: Session = Depends(get_db)):
#     # Step 1: Get employee
#     employee = db.query(Employee).filter_by(id=employee_id).first()
#     if not employee:
#         raise HTTPException(status_code=404, detail="Employee not found")

#     # Step 2: Ensure employee has at least one manager
#     if not employee.employee_managers or len(employee.employee_managers) == 0:
#         raise HTTPException(status_code=400, detail="No manager assigned to this employee")

#     # Step 3: Resolve manager (currently assuming 1:1 mapping)
#     manager = employee.employee_managers[0].manager
#     if not manager:
#         raise HTTPException(status_code=400, detail="Manager record not found")

#     # Step 4: Generate insights
#     insights = generate_insights(employee)

#     # Step 5: Create and store report
#     report = build_report(db=db, employee=employee, manager=manager, insights=insights)

#     return {"message": "Report created", "report_id": report.id}


# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from pydantic import BaseModel
# from typing import Optional, List
# from app.database.session import get_db
# from app.models import Employee
# from app.services.insight_generator import generate_insights
# from app.services.report_builder import build_report
# from fastapi import Body

# router = APIRouter()


# class GenerateReportRequest(BaseModel):
#     employee_id: Optional[int] = None


# class GenerateReportResponse(BaseModel):
#     message: str
#     report_ids: List[int]


# # @router.post("/generate/", response_model=GenerateReportResponse)
# # def generate_reports(
# #     request: GenerateReportRequest = Body(default={}),
# #     db: Session = Depends(get_db)
# # ):
# #     report_ids = []

# #     if request.employee_id:
# #         # Generate report for a specific employee
# #         employee = db.query(Employee).filter_by(id=request.employee_id).first()
# #         if not employee:
# #             raise HTTPException(status_code=404, detail="Employee not found")
# #         if not employee.employee_managers:
# #             raise HTTPException(status_code=400, detail="No manager assigned")

# #         manager = employee.employee_managers[0].manager
# #         insights = generate_insights(employee)
# #         report = build_report(db, employee, manager, insights)
# #         report_ids.append(report.id)

# #         return {"message": "Report generated for one employee", "report_ids": report_ids}

# #     else:
# #         # Generate reports for all employees
# #         employees = db.query(Employee).all()
# #         for emp in employees:
# #             if not emp.employee_managers:
# #                 continue
# #             manager = emp.employee_managers[0].manager
# #             insights = generate_insights(emp)
# #             report = build_report(db, emp, manager, insights)
# #             report_ids.append(report.id)

# #         return {"message": f"Reports generated for {len(report_ids)} employees", "report_ids": report_ids}
# @router.post("/generate/", response_model=GenerateReportResponse)
# def generate_reports(
#     request: GenerateReportRequest = Body(default=None),
#     db: Session = Depends(get_db)
# ):
#     report_ids = []

#     if request and request.employee_id:
#         employee = db.query(Employee).filter_by(id=request.employee_id).first()
#         if not employee:
#             raise HTTPException(status_code=404, detail="Employee not found")
#         if not employee.employee_managers:
#             raise HTTPException(status_code=400, detail="No manager assigned")

#         manager = employee.employee_managers[0].manager
#         insights = generate_insights(employee)
#         report = build_report(db, employee, manager, insights)
#         report_ids.append(report.id)

#         return {"message": "Report generated for one employee", "report_ids": report_ids}

#     else:
#         employees = db.query(Employee).all()
#         for emp in employees:
#             if not emp.employee_managers:
#                 continue
#             manager = emp.employee_managers[0].manager
#             insights = generate_insights(emp)
#             report = build_report(db, emp, manager, insights)
#             report_ids.append(report.id)

#         return {"message": f"Reports generated for {len(report_ids)} employees", "report_ids": report_ids}


from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, List

from app.database.session import get_db
from app.models import Employee
from app.services.insight_generator import generate_insights
from app.services.report_builder import build_report
from app.services.email_sender import send_email_report  # ✅ Import email sender

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
        # ✅ Generate report for a specific employee
        employee = db.query(Employee).filter_by(id=request.employee_id).first()
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        if not employee.employee_managers:
            raise HTTPException(status_code=400, detail="No manager assigned")

        manager = employee.employee_managers[0].manager
        insights = generate_insights(employee)
        report = build_report(db, employee, manager, insights)
        report_ids.append(report.id)

        # ✅ Send email after building report
        try:
            send_email_report(report, db)
        except Exception as e:
            print(f"❌ Failed to send email for report ID {report.id}: {str(e)}")

        return {"message": "Report generated and email sent for one employee", "report_ids": report_ids}

    else:
        # ✅ Generate reports for all employees
        employees = db.query(Employee).all()
        for emp in employees:
            if not emp.employee_managers:
                continue
            manager = emp.employee_managers[0].manager
            insights = generate_insights(emp)
            report = build_report(db, emp, manager, insights)
            report_ids.append(report.id)

            # ✅ Send email after building report
            try:
                send_email_report(report, db)
            except Exception as e:
                print(f"❌ Failed to send email for report ID {report.id}: {str(e)}")

        return {"message": f"Reports generated and emails sent for {len(report_ids)} employees", "report_ids": report_ids}
