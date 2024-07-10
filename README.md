# Astute AI Backend Server

## Overview

The Astute AI Backend Server is designed to manage and serve a vector store from CMS content. This project is divided into two phases: creating and refreshing the vector store, and serving a chatbot using this vector store.

## Phase 1: Vector Store Management

### Routes

- **Create Vector Store (GET`/create_vector_store`)**: Initializes the vector store from the contents of the CMS.
- **Refresh Vector Store (GET`/refresh_vector_store`)**: Updates the vector store whenever the CMS content is modified.

### Notes

- The vector store is persistent and should be refreshed as the CMS updates.

## Phase 2: Chatbot Service

### Routes

- **Chatbot Service (POST`/chatbot`)**: Asynchronous route to serve the chatbot using the vector store in ChromaDB.
- **Clear Chat History (GET`/chatbot/clear_chat_history`)**: Clears the chat history when a chat session ends.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/pk-vishnu/astuteai-server.git
   cd astute-ai-backend-server
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Server

1. Start the FastAPI Server
   ```bash
   fastapi dev main.py
   ```
