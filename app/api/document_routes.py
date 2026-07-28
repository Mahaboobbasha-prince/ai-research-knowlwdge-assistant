from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.document import Document
from app.services.document_service import save_pdf

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post("/upload")
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    file_path, extracted_text = save_pdf(file)

    document = Document(
    filename=file.filename,
    content=extracted_text
)

    db.add(document)
    db.commit()
    db.refresh(document)

    return {
    "message": "Document uploaded successfully",
    "id": document.id,
    "filename": document.filename,
    "characters_extracted": len(extracted_text),
    "preview": extracted_text[:500]
}

@router.get("/")
def get_documents(db: Session = Depends(get_db)):
    documents = db.query(Document).all()

    return documents