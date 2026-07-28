from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database.database import get_db
from app.models.document import Document
from app.services.summarizer_service import summarize_document

router = APIRouter(
    prefix="/summarize",
    tags=["Summarization"]
)


class SummaryRequest(BaseModel):
    document_id: int


@router.post("/")
def summarize(
    request: SummaryRequest,
    db: Session = Depends(get_db)
):

    document = db.query(Document).filter(
        Document.id == request.document_id
    ).first()

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    summary = summarize_document(document.content)

    return {
        "document_id": document.id,
        "filename": document.filename,
        "summary": summary
    }