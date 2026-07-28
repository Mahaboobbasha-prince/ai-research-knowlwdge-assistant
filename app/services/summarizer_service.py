from app.services.gemini_service import model


def summarize_document(text: str):

    prompt = f"""
You are an AI Research Assistant.

Summarize the following document into 8-10 concise bullet points.

Document:
{text}
"""

    response = model.generate_content(prompt)

    return response.text