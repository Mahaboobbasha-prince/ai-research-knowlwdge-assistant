conversation_history = []


def add_to_memory(question, answer):
    conversation_history.append({
        "question": question,
        "answer": answer
    })

    # Keep only last 5 conversations
    if len(conversation_history) > 5:
        conversation_history.pop(0)


def get_memory():
    history = ""

    for chat in conversation_history:
        history += f"""
User: {chat['question']}
Assistant: {chat['answer']}

"""

    return history