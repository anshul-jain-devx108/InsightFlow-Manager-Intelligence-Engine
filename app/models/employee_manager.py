from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database.session import Base

class EmployeeManager(Base):
    __tablename__ = "employee_manager"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    manager_id = Column(Integer, ForeignKey("managers.id"))

    employee = relationship("Employee", back_populates="employee_managers")
    manager = relationship("Manager", back_populates="employee_managers")
