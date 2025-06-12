from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class EmployeeCreate(BaseModel):
    name: str
    email: str
    department: Optional[str]
    role: Optional[str]

class ManagerCreate(BaseModel):
    name: str
    email: str

class InsightOut(BaseModel):
    id: int
    content: str
    confidence: str
    category: str

    class Config:
        orm_mode = True

class ReportOut(BaseModel):
    id: int
    employee_id: int
    manager_id: int
    generated_at: datetime
    version: Optional[str]
    duration: Optional[str]
    insights: Optional[List[InsightOut]]

    class Config:
        orm_mode = True
