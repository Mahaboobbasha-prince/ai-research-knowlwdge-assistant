from fastapi import APIRouter
from pydantic import BaseModel

from app.services.embedding_service import generate_embedding
from app.rag.vector_store import collection
from app.services.gemini_service import generate_answer

from app.services.memory_service import (
    add_to_memory,
    get_memory
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


class ChatRequest(BaseModel):
    question: str


@router.post("/")
def chat(request: ChatRequest):

    query_embedding = generate_embedding(request.question)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    documents = results["documents"][0]

    context = "\n\n".join(documents)

    history = get_memory()

    answer = generate_answer(
        request.question,
        context,
        history
    )

    add_to_memory(
        request.question,
        answer
    )

    return {
        "question": request.question,
        "answer": answer,
        "sources": results["ids"][0]
    }