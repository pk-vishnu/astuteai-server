from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from langchainn.llm_chain import invoke_with_history
from langchainn.vectorstore import SimpleRetriever
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

router = APIRouter()

chat_history = []
@router.post("/chatbot")
async def index(request: Request):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma(persist_directory='./vector_db', embedding_function=embeddings)
    retriever = SimpleRetriever(vectorstore)
    global chat_history
    data = await request.json()
    user_question = data.get("prompt")
    if user_question:
        answer, sources, chat_history = invoke_with_history(user_question, retriever, chat_history)
        return JSONResponse(content={"response": answer, "chat_history": chat_history, "sources": list(sources)})
    return JSONResponse(content={"response": None, "chat_history": chat_history})

@router.get("/chatbot/clear_chat_history")
async def clear_chat_history():
    global chat_history
    chat_history = []
    return JSONResponse(content={"response": "Chat history cleared!"})