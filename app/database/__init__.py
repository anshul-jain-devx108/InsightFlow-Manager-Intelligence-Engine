from app.database.session import engine
from app.database.base import Base  # Ensure this is where Base = declarative_base() is defined

# Import all model modules to register them with SQLAlchemy metadata
from app.models import employee, manager, employee_manager, report_log, email_log

def init_db():
    print("[INFO] Creating all tables in the database...")
    Base.metadata.create_all(bind=engine)
    print("[SUCCESS] All tables created successfully.")
