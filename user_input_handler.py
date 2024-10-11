# user_input_handler.py
from datetime import datetime
from langchain.schema import AIMessage
from html_templates import my_css, my_bot_template, my_user_template

# custom exception classes
class InvalidInputError(Exception):
    pass
class NoneTypeConversationStateError(Exception):
    pass

class FileSizeLimitExceeded(Exception):
    pass



# method to handle user input to the bot. We want to save conversation or start one. 
# We add the timestamp of when there is a new message and use that to sort the messages whenever we display it
def handle_user_input(user_question, st):
    # check for valid questions. If no question raise input exception
    if not user_question:
        raise InvalidInputError(f"Upload a file and input user question to start a conversation")

    if not st.session_state.conversation: # session state cannot be nonetype either
        raise NoneTypeConversationStateError(f"Upload and process files to begin Conversation")
    
    # create the chat history data sets if they are not there
    if "chat_history" not in st.session_state: 
        st.session_state.chat_history = []
        st.session_state.chat_history_time = [] # with timestamp for sorting

    
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    response = st.session_state.conversation({"question": user_question})
    
    # Update chat history with bot messages
    if "chat_history" in response:
        for message in response["chat_history"]:

            # Extract the content of each message
            content = message.content

            # Determine the sender (assuming AIMessage is from the bot)
            sender = "bot" if isinstance(message, AIMessage) else "user"

            # Get the timestamp (use the current time for simplicity)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Create a dictionary representing the message
            chat_message = {"content": content,"sender": sender }


            # Check if the message already exists in the chat history
            if chat_message not in st.session_state.chat_history:
                st.session_state.chat_history.append(chat_message)
                
                message_with_timestamp = {**chat_message, "timestamp": timestamp}
                st.session_state.chat_history_time.append(message_with_timestamp)
    
    # write message chain to html template with helper method
    write_to_template(st)
    

# helper method for writing to template
def write_to_template(st):
    # Sort the chat history based on timestamps
    st.session_state.chat_history_time = sorted(st.session_state.chat_history_time, key=lambda x: x["timestamp"])
    
    # Display the chat history with user and bot templates
    for message in st.session_state.chat_history_time:
        if message["sender"] == "user":
            st.write(my_user_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)
        else:
            st.write(my_bot_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)


