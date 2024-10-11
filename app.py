# app.py
import streamlit as st
import pickle
from dotenv import load_dotenv

# Custom modules
from html_templates import my_css, my_bot_template
from pdf_parser import get_text_chunks, get_text_from_files
from pdf_embeddings import get_conversation_chain, get_vector_store
from user_input_handler import InvalidInputError, NoneTypeConversationStateError,FileSizeLimitExceeded, handle_user_input
from pdf_parser import NoUploadedFileError
from pickle_conversation import display_conversation_history, save_conversation_history


def main():

    load_dotenv() # load environment variables

    # Set up GUI page with title, render css template display header
    st.set_page_config(page_title="Chat with your PDF/DOCX files", page_icon=":books:")
    st.write(my_css, unsafe_allow_html=True)
    st.header("Chat with your PDF/DOCX files :books:")

    # take user question input
    user_question = st.text_input("Enter your prompts/questions here:")

    # start a conversation if there is none already
    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    # start chat history if there is none
    if "chat_history" not in st.session_state:
       
        starter_message = "Welcome!!!  Upload a PDF/DOCX and let's chat!"
        st.write(my_bot_template.replace("{{MSG}}", starter_message), unsafe_allow_html=True)

        st.session_state.chat_history = [] 
        st.session_state.chat_history_time =[] 
    
    # handle user question with handler function and handle exceptions too
    if user_question:
        try:
            handle_user_input(user_question, st)
            
        except InvalidInputError as e: 
            st.error(f"Invalid input error: {e}")

        except NoneTypeConversationStateError as e:
            st.error(f"NoneType conversation state error: {e}")
                
    # Side bar for uploading PDFs and displaying saved chat history
    with st.sidebar:
        
        # subheader and upload prompt
        st.subheader("Your documents")
        text_docs = st.file_uploader("Upload your PDF/DOCX files here and click on 'Process' (<200MB total)", accept_multiple_files=True)
        if text_docs:
            # Get total file size
            total_size_mb = sum(file.size for file in text_docs) / (1024 * 1024)  # Convert to MB
            st.write(f"Total file size: {total_size_mb:.2f} MB")

            # Check if total size exceeds limit
            if total_size_mb > 200:
                st.error("Total file size exceeds the limit of 200MB. Please upload smaller files.")
                raise FileSizeLimitExceeded(f"Please upload only upto 200MB of files")
            
        # handle button press for processing files uploaded
        if st.button("Process"): 

            try:
                with st.spinner("Processing"): # Spinning wheel for processing
                    
                    # Get raw PDF/DOCX text
                    raw_text = get_text_from_files(text_docs)
            
                    # Get the text chunks as list
                    text_chunks = get_text_chunks(raw_text)
                    
                    # Create a Vector Store
                    vector_store = get_vector_store(text_chunks)

                    # Create conversation chain -- for memory so we do not lose session conversation
                    st.session_state.conversation = get_conversation_chain(vector_store)
            
            except NoUploadedFileError as e: # clicking on Process without file uploaded should raise exception
                st.error(f"No file uploaded error: {e}")

        # display Saved Chat History in side bar when clicked
        with st.sidebar.expander("Saved Chat History"):
            display_conversation_history(st)

    # save chat history before exiting from main
    save_conversation_history(st.session_state.chat_history, st.session_state.chat_history_time)


if __name__ == "__main__":

    main()

