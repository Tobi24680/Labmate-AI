import os
import certifi

os.environ["SSL_CERT_FILE"] = certifi.where()

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
            "You are a study assistant ONLY for computer science students. "
            "You must answer questions related to computer science subjects such as "
            "C programming, C++, Java, Python, data structures, algorithms, "
            "operating systems, DBMS, computer networks, software engineering, "
            "AI, ML, and cybersecurity. "
            "If a question is NOT related to computer science studies, "
            "respond ONLY with: "
            "'I can only answer computer science study-related questions.' "
            "Explain answers in simple words, step by step, with small examples."
        ),
        ("human", "{question}")
    ]
)

chain = prompt | llm | StrOutputParser()

CS_KEYWORDS = [
    "c", "c programming", "c++", "java", "python",
    "function", "pointer", "array", "structure",
    "data structure", "algorithm", "stack", "queue",
    "linked list", "tree", "graph", "sorting", "searching",
    "operating system", "os", "process", "thread",
    "deadlock", "memory", "paging", "scheduling",
    "dbms", "database", "sql", "normalization",
    "transaction", "index",
    "computer networks", "tcp", "ip", "http", "dns",
    "software engineering", "uml",
    "ai", "machine learning", "ml",
    "compiler", "interpreter"
]

GREETINGS = ["hi", "hii", "hello", "hlo", "hey"]

def is_cs_question(question: str) -> bool:
    question = question.lower()
    return any(keyword in question for keyword in CS_KEYWORDS)

def lab_ai_response(question: str) -> str:
    q = question.lower().strip()

    if q in GREETINGS:
        return "👋 Hello! I am your LabMate AI. Ask me a CS-related question."

    if not is_cs_question(question):
        return "❌ Sorry, I can only answer study-related questions."

    try:
        return chain.invoke({"question": question}).strip()
    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == "__main__":
    while True:
        q = input("Ask a CS study question (or type 'exit'): ")
        if q.lower() == "exit":
            break
        print(lab_ai_response(q))
