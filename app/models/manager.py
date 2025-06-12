# # from sqlalchemy import Column, Integer, String
# # from sqlalchemy.orm import relationship
# # from app.database.session import Base

# # class Manager(Base):
# #     __tablename__ = "managers"

# #     id = Column(Integer, primary_key=True, index=True)
# #     name = Column(String)
# #     email = Column(String, unique=True, index=True)

# #     employee_managers = relationship("EmployeeManager", back_populates="manager")
# #     report_logs = relationship("ReportLog", back_populates="manager", cascade="all, delete-orphan")


# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship
# from app.database.session import Base

# class Manager(Base):
#     __tablename__ = "managers"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     email = Column(String, unique=True, index=True)

#     employee_managers = relationship("EmployeeManager", back_populates="manager")
#     report_logs = relationship("ReportLog", back_populates="manager")

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.session import Base

class Manager(Base):
    __tablename__ = "managers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)

    employee_managers = relationship("EmployeeManager", back_populates="manager")
    report_logs = relationship("ReportLog", back_populates="manager")
    
    # ✅ Add this to fix the KeyError: 'reports'
    reports = relationship("Report", back_populates="manager", cascade="all, delete-orphan")
