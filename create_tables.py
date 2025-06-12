# create_tables.py

from app.database.session import engine
from app.models import employee, manager, employee_manager  # ensure all models are imported
from app.database.base import Base

print("Creating all tables...")
Base.metadata.create_all(bind=engine)
print("Done.")
