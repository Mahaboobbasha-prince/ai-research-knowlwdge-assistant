from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database.database import get_db
from app.models.document import Document
from app.services.comparison_service import compare_documents

router = APIRouter(
    prefix="/compare",
    tags=["Comparison"]
)


class CompareRequest(BaseModel):
    document1_id: int
    document2_id: int


@router.post("/")
def compare(
    request: CompareRequest,
    db: Session = Depends(get_db)
):

    doc1 = db.query(Document).filter(
        Document.id == request.document1_id
    ).first()

    doc2 = db.query(Document).filter(
        Document.id == request.document2_id
    ).first()

    if doc1 is None or doc2 is None:
        raise HTTPException(
            status_code=404,
            detail="One or both documents not found"
        )

    comparison = compare_documents(
        doc1.content,
        doc2.content
    )

    return {
        "document_1": doc1.filename,
        "document_2": doc2.filename,
        "comparison": comparison
    }