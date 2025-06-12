from pydantic import BaseModel
from datetime import datetime

class EmailLogOut(BaseModel):
    id: int
    to_email: str
    report_id: int
    status: str
    error_message: str | None = None
    smtp_code: str | None = None
    bounce_type: str | None = None
    opened: str | None = None
    clicked: str | None = None
    sent_at: datetime

    class Config:
        orm_mode = True
