# states.py
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
# from langchain_community.embeddings import OpenAIEmbeddings
# from langchain_openai import OpenAIEmbeddings
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings.huggingface import HuggingFaceInstructEmbeddings


# from langchain_community.vectorstores import FAISS
# from langchain.vectorstores import FAISS #faiss
# from langchain_community.vectorstores import faiss
from langchain.vectorstores.faiss import FAISS


from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

from html_templates import css, bot_template, user_template

from datetime import datetime

# from langchain.chat_models import AIMessage
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)


from pdf_parser import get_pdf_text, get_text_chunks, get_text_from_files
from pdf_embeddings import get_conversation_chain, get_vector_store


# def get_pdf_text(pdf_docs):
#     # Read content of pdf_docs page by page and add to text string
#     text_string = ""

#     for pdf in pdf_docs:
#         pdf_reader = PdfReader(pdf)
#         for page in pdf_reader.pages:
#             text_string += page.extract_text()

#     return text_string


# def get_text_chunks(raw_text):
#     text_splitter = CharacterTextSplitter(
#         separator="\n", 
#         chunk_size=1000,
#         chunk_overlap=200,
#         length_function=len
#     )

#     # Get list of split text with the specifications above
#     chunks = text_splitter.split_text(raw_text)
#     return chunks

# def get_vector_store(text_chunks):

#     embeddings = OpenAIEmbeddings()
#     # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
#     vector_store = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
#     return vector_store

# def get_conversation_chain(vector_store):
#     llm = ChatOpenAI()
#     memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
#     conversation_chain = ConversationalRetrievalChain.from_llm(
#                 llm=llm,
#                 retriever=vector_store.as_retriever(),
#                 memory=memory
#             )
    
#     return conversation_chain

# def handle_user_input1(user_question):

#     print(st.session_state.conversation)
#     response = st.session_state.conversation({"question": user_question})
#     # st.write(response)
#     print("\n\n","another chat history ------------   ",st.session_state.conversation)
    
#     st.session_state.chat_history = response["chat_history"]
#     print("\n\n","another chat history ------------   ",st.session_state.chat_history)
    
#     for i, message in enumerate(st.session_state.chat_history):
#         if i % 2 == 0:
#             st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
#         else:
#             st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)



#     return 

def handle_user_input(user_question):
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
        st.session_state.chat_history_time = []

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    

    # st.session_state.chat_history.append(user_message)

    response = st.session_state.conversation({"question": user_question})
    # print(response)
    # Update chat history with bot messages
    # print("1st --------", st.session_state.chat_history)
    if "chat_history" in response:
        for message in response["chat_history"]:
            # Extract the content of each message
            content = message.content
            # Determine the sender (assuming AIMessage is from the bot)
            sender = "bot" if isinstance(message, AIMessage) else "user"
            # Get the timestamp (use the current time for simplicity)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Create a dictionary representing the message
            chat_message = {
                "content": content,
                "sender": sender,
                # "timestamp": timestamp
            }

            
            
            
            # Check if the message already exists in the chat history
            if chat_message not in st.session_state.chat_history:
                st.session_state.chat_history.append(chat_message)
                
                message_with_timestamp = {**chat_message, "timestamp": timestamp}
                st.session_state.chat_history_time.append(message_with_timestamp)
            
            

    # Sort the chat history based on timestamps
    
    st.session_state.chat_history_time = sorted(st.session_state.chat_history_time, key=lambda x: x["timestamp"])
    
    # Display the chat history

    
    for message in st.session_state.chat_history_time:
        if message["sender"] == "user":
            st.write(user_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)

    

def main():

    load_dotenv()
    # Set up GUI page
    st.set_page_config(page_title="Chat with Multiple PDFs", page_icon=":books:")

    # add it to top?
    st.write(css, unsafe_allow_html=True)

    # # Create an empty slot at the top for the initial bot message
    # top_slot = st.empty()
    # top_slot.write(bot_template.replace("{{MSG}}", "Hello, how can I help you today?"), unsafe_allow_html=True)


    # start a conversation if there is none already
    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        # st.session_state.chat_history = None
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state.chat_history = [{"content" : "Hello, how can I help you today?", 
                                           "sender" : "bot"}]
        
        st.session_state.chat_history_time = [{"content" : "Hello, how can I help you today?", 
                                                "sender" : "bot",
                                              "timestamp": timestamp}]
        # starter_bot_message = {"content" : "Hello, how can I help you today?", 
                            #    "sender" : "bot"}

    st.header("Chat with Multiple PDFs :books:")


    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        handle_user_input(user_question)

    # at bottom?
    # st.write(user_template.replace("{{MSG}}", "Hello robot"), unsafe_allow_html=True)
    
    # st.write(bot_template.replace("{{MSG}}", "Hello, how can I help you today?"), unsafe_allow_html=True)
    # print("\n\n","chat history --------",st.session_state.chat_history)
    # Side bar for uploading PDFs
    with st.sidebar:

        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        
        if st.button("Process"):
            with st.spinner("Processing"): # Spinning wheel for processing

                # Getting PDF/DOCX text
                raw_text = get_text_from_files(pdf_docs)
                # st.write(raw_text) # write the text in sidebar

                # Getting the text Chunks
                text_chunks = get_text_chunks(raw_text)
                # st.write(text_chunks) # list of chunks

                # Creating Vector Store
                vector_store = get_vector_store(text_chunks)

                # create conversation chain -- for memory
                # use OOP to keep conversation for this session so 
                # we dont lose conversation when it runs again in same session
                st.session_state.conversation = get_conversation_chain(vector_store)
                





# if __name__ == "__main__":

#     main()