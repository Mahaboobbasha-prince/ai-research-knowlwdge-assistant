from fastapi import FastAPI

from app.api.document_routes import router as document_router
from app.api.search_routes import router as search_router
from app.api.chat_routes import router as chat_router
from app.api.summarize_routes import router as summarize_router
from app.api.compare_routes import router as compare_router

app = FastAPI()

app.include_router(document_router)
app.include_router(search_router)
app.include_router(chat_router)
app.include_router(summarize_router)
app.include_router(compare_router)

@app.get("/")
def root():
    return {"message": "AI Research & Knowledge Assistant"}

@app.get("/health")
def health():
    return {"status": "healthy"}