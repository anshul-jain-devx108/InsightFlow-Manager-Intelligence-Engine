from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session
import csv
from app.database.session import get_db
from app.models.employee import Employee
from app.models.manager import Manager
from app.models.employee_manager import EmployeeManager

router = APIRouter(tags=["Upload"])

@router.post("/employee-csv/")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Invalid file format")

    contents = await file.read()
    decoded = contents.decode().splitlines()
    reader = csv.DictReader(decoded)

    for row in reader:
        employee = Employee(
            name=row["employee_name"],
            email=row["employee_email"],
            department=row["department"],
            role=row["role"]
        )
        db.add(employee)
        db.flush()  # To get employee.id

        manager = db.query(Manager).filter_by(email=row["manager_email"]).first()
        if not manager:
            manager = Manager(name=row["manager_name"], email=row["manager_email"])
            db.add(manager)
            db.flush()

        association = EmployeeManager(employee_id=employee.id, manager_id=manager.id)
        db.add(association)

    db.commit()
    return {"status": "Uploaded and processed"}
