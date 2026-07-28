import os
import shutil

from app.utils.pdf_loader import extract_text_from_pdf
from app.utils.chunking import split_text

from app.services.embedding_service import generate_embedding
from app.rag.vector_store import collection

UPLOAD_FOLDER = "uploads"


def save_pdf(file):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_pdf(file_path)

    chunks = split_text(text)

    for index, chunk in enumerate(chunks):

        embedding = generate_embedding(chunk)

        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[f"{file.filename}_{index}"]
        )

    return file_path, text