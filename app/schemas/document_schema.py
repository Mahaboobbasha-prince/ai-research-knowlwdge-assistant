from pydantic import BaseModel
from datetime import datetime


class DocumentResponse(BaseModel):
    id: int
    filename: str
    title: str | None = None
    author: str | None = None
    upload_time: datetime

    class Config:
        from_attributes = True