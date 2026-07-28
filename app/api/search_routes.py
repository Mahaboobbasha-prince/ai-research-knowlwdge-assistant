from fastapi import APIRouter
from pydantic import BaseModel

from app.services.embedding_service import generate_embedding
from app.rag.vector_store import collection

router = APIRouter(prefix="/search", tags=["Search"])


class SearchRequest(BaseModel):
    query: str


@router.post("/")
def semantic_search(request: SearchRequest):

    query_embedding = generate_embedding(request.query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return results