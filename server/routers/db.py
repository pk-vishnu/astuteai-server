from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from langchainn.vectorstore import create_vector_store
from langchainn.embed_text_chunks import fetch_content_from_api, split_documents
import shutil,os,logging

router = APIRouter()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# This route is to refresh vector store upon changes made in CMS
@router.get("/db/refresh_vector_store")
def create_vector_store_api():
    API_URL = "https://vishnupk05.pythonanywhere.com/api/fetch_posts_txt"
    try:
        documents = fetch_content_from_api(API_URL)
        splits = split_documents(documents)
        
        if os.path.exists('./vector_db'):
            shutil.rmtree('./vector_db')
            logger.info("Existing vector store removed.")
        
        create_vector_store(splits)
        logger.info("Vector store refreshed successfully.")
        
        return JSONResponse(content={"message": "Vector store refreshed using contents fetched from CMS!"}, status_code=200)
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        return JSONResponse(content={"error": e.detail}, status_code=e.status_code)
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return JSONResponse(content={"error": "An unexpected error occurred"}, status_code=500)

# This route is to init create vector store using contents fetched from CMS
@router.get("/db/create_vector_store")
def create_vector_store_api():
    API_URL = "https://vishnupk05.pythonanywhere.com/api/fetch_posts_txt"
    documents = fetch_content_from_api(API_URL)
    splits = split_documents(documents)
    create_vector_store(splits)
    return "Vector store created using contents fetched from CMS!"