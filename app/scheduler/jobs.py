from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.models.employee import Employee
from app.services.insight_generator import generate_insights
from app.services.report_builder import build_report
from app.services.email_sender import send_email_report

def run_scheduled_jobs():
    scheduler = BackgroundScheduler()
    scheduler.add_job(generate_and_send_reports, "cron", hour=8)  # every day at 8 AM
    scheduler.start()

def generate_and_send_reports():
    db: Session = SessionLocal()
    try:
        employees = db.query(Employee).all()

        for emp in employees:
            if not emp.employee_managers:
                continue

            manager = emp.employee_managers[0].manager
            insights = generate_insights(emp)
            report = build_report(db, employee=emp, manager=manager, insights=insights)
            send_email_report(report, db)

    except Exception as e:
        print(f"Scheduler error: {e}")
    finally:
        db.close()
