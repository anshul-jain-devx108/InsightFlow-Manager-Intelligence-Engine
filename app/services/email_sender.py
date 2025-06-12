from app.models import EmailLog
from jinja2 import Template
from app.config import settings
import smtplib
from email.mime.text import MIMEText
from sqlalchemy.orm import Session

def render_email(report):
    template = """
    <h2>People Insight Report</h2>
    <p><strong>Employee:</strong> {{ employee.name }}</p>
    <p><strong>Manager:</strong> {{ manager.name }}</p>
    <p><strong>Generated At:</strong> {{ report.generated_at }}</p>
    <h4>Insights:</h4>
    <ul>
    {% for mapping in report.report_insights %}
        <li>{{ mapping.insight.content }} (Confidence: {{ mapping.insight.confidence }})</li>
    {% endfor %}
    </ul>
    """
    jinja_template = Template(template)
    return jinja_template.render(report=report, employee=report.employee, manager=report.manager)

def send_email_report(report, db: Session):
    html_content = render_email(report)

    msg = MIMEText(html_content, "html")
    msg["Subject"] = "Your Employee Report is Ready"
    msg["From"] = settings.EMAIL_FROM
    msg["To"] = report.manager.email

    try:
        with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
            server.starttls()
            server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
            server.sendmail(msg["From"], [msg["To"]], msg.as_string())

        log = EmailLog(
            to_email=msg["To"],
            report_id=report.id,
            status="Sent"
        )
    except Exception as e:
        log = EmailLog(
            to_email=msg["To"],
            report_id=report.id,
            status="Failed",
            error_message=str(e)
        )

    db.add(log)
    db.commit()
