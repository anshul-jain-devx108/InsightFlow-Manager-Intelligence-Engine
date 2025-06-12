from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.session import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    department = Column(String)
    role = Column(String)

    reports = relationship("Report", back_populates="employee")
    employee_managers = relationship("EmployeeManager", back_populates="employee")
