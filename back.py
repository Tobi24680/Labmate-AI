from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

OLLAMA_MODEL = "qwen2.5:1.5b"

llm = ChatOllama(
    model=OLLAMA_MODEL,
    temperature=0.2,  
    timeout=60
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a study assistant for computer science students. "
            "Explain concepts in simple words. "
            "Use step-by-step explanations. "
            "Give small examples when helpful. "
            "Avoid unnecessary complexity."
        ),
        ("human", "{question}")
    ]
)

chain = prompt | llm | StrOutputParser()


def lab_ai_response(question: str) -> str:
    try:
        return chain.invoke({"question": question}).strip()
    except Exception as e:
        return f"❌ Error: {e}"
