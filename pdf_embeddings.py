# pdf_embeddings.py
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain



# Vectorize the text chunks using OPENAIEmbeddings
def get_vector_store(text_chunks):

    my_embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")

    # Generate FAISS vector store DB using the text chunks and embeddings
    my_vector_store = FAISS.from_texts(texts=text_chunks, embedding=my_embeddings)
    return my_vector_store

# Create a conversation chain using OpenAI chat model
def get_conversation_chain(vector_store):

    # use OpenAIs large language model and bot to handle chat 
    my_llm = ChatOpenAI()
    buffer_memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
                llm=my_llm,
                retriever=vector_store.as_retriever(),
                memory=buffer_memory
            )
    
    return conversation_chain