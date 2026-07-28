from app.services.gemini_service import model


def compare_documents(text1: str, text2: str):

    prompt = f"""
You are an AI Research Assistant.

Compare these two documents.

Provide:

1. Summary of Document 1
2. Summary of Document 2
3. Similarities
4. Differences
5. Conclusion

Document 1:
{text1}

--------------------------------

Document 2:
{text2}
"""

    response = model.generate_content(prompt)

    return response.text