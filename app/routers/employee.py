from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.employee import Employee

router = APIRouter()

@router.get("/")
def get_all_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()
