# # from .employee import Employee
# # from .manager import Manager
# # from .report import Report
# # from .insight import Insight
# # from .email_log import EmailLog
# # from .report_insight_map import ReportInsightMap
# # from .employee_manager import EmployeeManager
# # from .admin_user import AdminUser
# # from app.models import employee, manager, employee_manager, report_log, email_log
# # app/models/__init__.py

# from app.models import manager
# from app.models import employee
# from app.models import employee_manager
# from app.models import report_log
# from app.models import email_log


from .employee import Employee
from .manager import Manager
from .employee_manager import EmployeeManager
from .report import Report  # ✅ Make sure this line is added
from .report_log import ReportLog
from .email_log import EmailLog
from .insight import Insight
from .report_insight_map import ReportInsightMap
from .admin_user import AdminUser

# Optional: expose them explicitly to avoid circular import bugs
__all__ = [
    "Employee",
    "Manager",
    "EmployeeManager",
    "Report",
    "ReportLog",
    "EmailLog",
    "Insight",
    "ReportInsightMap",
    "AdminUser",
]
