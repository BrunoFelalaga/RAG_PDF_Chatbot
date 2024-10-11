
import pickle

# HELPER METHODS FOR LOADING AND SAVING CONVERSATION STATES
# method to display chat history in side bar
def display_conversation_history(st):

    # load conversation history from pickle file 
    chat_history, chat_history_time = load_conversation_history()
    
    # display only the last three messages with timestamp
    st.write("Saved Chat History:")
    if chat_history:
        num_messages = len(chat_history)
        if num_messages >= 3:
            start_index = num_messages - 3
        else:
            start_index = 0
        for message, time in zip(chat_history[start_index:], chat_history_time[start_index:]):
            st.write(f"[{time}] {message['sender']}: {message['content']}")



# load conversation history from pickl files saved
def load_conversation_history():
    try:
        # open saved pickl file
        with open("conversation_history.pkl", "rb") as file:
            conversation_history = pickle.load(file)
            chat_history = conversation_history.get("chat_history", [])
            chat_history_time = conversation_history.get("chat_history_time", [])
            
            return chat_history, chat_history_time
        
    except FileNotFoundError: # return empty lists when there is no file
        return [], []


# method to save conversation before exiting
def save_conversation_history(chat_history, chat_history_time):
    # if there is an already saved pickl file, we load it and add the current conversation to it
    # else we just add conversation to new pickle file
    try:
        # Load existing chat history from the pickle file if there is one
        with open("conversation_history.pkl", "rb") as file:
            existing_data = pickle.load(file)
            existing_chat_history = existing_data.get("chat_history", [])
            existing_chat_history_time = existing_data.get("chat_history_time", [])
    except FileNotFoundError: # if none, use empty lists
        existing_chat_history, existing_chat_history_time = [], []
    
    # Append the new chat history and chat history with time to the existing history
    updated_chat_history = existing_chat_history + chat_history
    updated_chat_history_time = existing_chat_history_time + chat_history_time
    
    # Create a dictionary with updated data
    conversation_history = {
        "chat_history": updated_chat_history,
        "chat_history_time": updated_chat_history_time
    }
    
    # Save the updated data back to the pickle file
    with open("conversation_history.pkl", "wb") as file:
        pickle.dump(conversation_history, file)

