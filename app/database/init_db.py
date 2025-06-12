from app.database.session import engine
from app.database.session import Base
from app.models import employee, manager, employee_manager, report_log, email_log  # Make sure these exist

def init_db():
    """
    Creates all tables in the database.
    """
    Base.metadata.create_all(bind=engine)
