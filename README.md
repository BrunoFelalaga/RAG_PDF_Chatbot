# Retrieval-Augmented Generation(RAG) PDF Chatbot

This program enables users to upload a PDF document and interact with a chatbot by asking questions about the content. 
It supports multiple PDF and DOCX file uploads for processing. 
The workflow involves parsing, chunking text, creating vector embeddings, 
and utilizing a language model for semantic search to answer user queries.

### Key Steps

1. **File Parsing**:  
The uploaded files are parsed with PyPDF to extract text in string form.

2. **Text Chunking**:  
The extracted text is split into chunks using LangChain’s text splitter. Overlapping chunks (approximately 200 words) are used to preserve meaning across boundaries and enhance context reconstruction.

3. **Embeddings**:  
Embeddings capture the semantic meaning of text, converting sentences into high-dimensional vector representations.  
We use OpenAI embeddings to create a vector store from text chunks, stored locally using FAISS for rapid search.  
Alternatively, HuggingFace’s InstructorEmbeddings can be used for generating embeddings on personal machines, though it may be slower without a GPU.

4. **Conversation Retrieval Chain**:  
The OpenAI chat model is used to create a conversation chain, allowing the bot to maintain context and handle follow-up questions effectively.  
LangChain’s Buffer Memory is employed to build a conversation retrieval chain, which combines the user’s question with previously discussed context, enabling more accurate responses from the source documents.

### Functionalities:
- Users can upload PDF files and receive feedback on their parse-ability.
- Users can query the chatbot to retrieve information from the PDF.
- Multiple PDFs can be uploaded within a total page limit.

### Selected Project Idea: PDF Chatbot

This program enables users to upload a PDF, which is then parsed and queried through a chatbot. 
Embeddings from OpenAI and LangChain are used, along with PyPDF as the PDF reader.

To run the application:
```bash
streamlit run app.py
```

### Dependencies:

To install required dependencies, use the following commands:

```bash
pip install streamlit pypdf2 faiss-cpu langchain python-dotenv openai huggingface_hub
```


For LangChain updates:

```bash
pip install -U langchain-community
pip install -U langchain-openai
```

Non-OpenAI Embedding Generation:
For local embedding generation (non-OpenAI):

```bash
pip install InstructorEmbedding sentence_transformers
pip uninstall sentence-transformers
pip install sentence-transformers==2.2.2
```

For older versions of LangChain:

```bash
pip uninstall langchain  
pip install langchain==0.1.2
```

DOCX File Support:
To process DOCX files, use the following:

```bash
pip install python-docx
```