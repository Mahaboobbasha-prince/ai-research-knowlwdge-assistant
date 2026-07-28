import google.generativeai as genai

from app.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)


model = genai.GenerativeModel("models/gemini-flash-lite-latest")


def generate_answer(question: str, context: str, history: str = ""):

    prompt = f"""
You are an AI Research & Knowledge Assistant.

Use ONLY the uploaded document and previous conversation.

Previous Conversation:
{history}

Context:
{context}

Question:
{question}

If the answer is not found in the context, reply exactly:

"I couldn't find that information in the uploaded document."

Answer:
"""

    response = model.generate_content(prompt)

    return response.text