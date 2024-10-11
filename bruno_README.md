Name: Bruno Felalaga

The project allows for the user to upload a pdf document and ask question to a chatbot on it. 
We make sure the user can upload multiple pdf and docx files and process them. 
The uploaded files are parsed with pypdf to get texts from it in string form
Then we split the text string into chunks to allow for feeding it to an embedding model
The embedding model creates a vector representation of the data that is stored in a vector database with FAISS
This database is what is used by the language model as sourced material for semantic search in order to interact with user questions

TEXT CHUNKING
We use text splitter from langchain to split text into chunks.
the chunks use an overlap to allow for chunks to overlap. 
By doing this when splitting is done such that meaning is lost, 
the overlap of about two hundred words between chunks makes it so meaning can be reconstructed

EMBEDDINGS
Embeddings capture the contextual and semantic meaning of sentences and phrases in a high dimension vector space. 
With this we can represent words/tokens in vector form and store them with their meaning
This information is then learned during training of large language models for the purposes of 
generatign texts, answering questions on learned embeddings, and classifying text

Here we use openai embeddings to create a vectore store of the data from the text chunks we created. 
this is a paid service but can be done with HuggingFace IntructorEmbeddings. 
However for running on personal computers it would be slower to make embeddings and would require a GPU rather than a CPU
We FAISS as a database to store the embeddings in a vector store locally. 

CONVERSATION RETRIEVAL CHAIN
Create a conversation chain using OpenAI chat model
A conversation chain will allow for us to chat with the bot and maintain context
When user asks a follow up question the bot should be able to understand and get the context of the it
For this we use the OpenAI llm and langchanin Buffer memory to create a conversation retrieval chain
The retrieval chain combines a new question with a conversation chain as a standalone question to be answered by
 an answering chain using referenced sourced documents




SELECTED PROJECT IDEA: PDF chatbot

This is a project that will allow a user to upload a pdf and query it. 
This will use the embeddings from OpenAI and LangChain and PyPDF as a pdf reader

Functionalities:
    - User should be able to upload a pdf to the application and get feedback on whether it is parsable or not
    - User should be able to simply query the bot and get information from the pdf
    - User should be able to upload multiple pdfs within some total pages limit

Week 4: - Research on how embeddings, parsing, chunking etc works and how to set up the  project for success. 
        - Scope out what libraries and packages will be needed 

Week 5: - Implement parsing and inspect parsing for several pdfs and 
        - Explore cleanliness and usability of parsed data 

Week 6: - Implement body aspects of application: 
                - Chunking
                - Vectorization
                - Handling of multiple pdfs

Week 7: - Implement additional features:
                - Keeping a conversation chain 
                - Incorporating a friendlier UI 

Week 8: - Test application efficiency for different pdfs and prompts and 
        - Ensure that application works reasonably and matches expected functionalities



DEPENDENCIES
>> pip install streamlit pypdf2 faiss-cpu langchain python-dotenv openai huggingface_hub

use this instead of langchain, langchain not supported as of langchain==0.2.0.
>> pip install -U langchain-community
>> pip install -U langchain-openai

======================================================================================================
>> streamlit run app.py
======================================================================================================

##WATCH HOW TO CHAT WITH PDFS
to use instead of OpenAI one, but heavy packages
>> pip install InstructorEmbedding sentence_transformers

>> pip uninstall sentence-transformers
>> pip install sentence-transformers==2.2.2

>> pip uninstall langchain  
>> pip install langchain==0.1.2 

for processing docx files
>> pip install python-docx


-------------------------------------------------------------------------------------------------------------------------------------
Project Selection

PROJECT IDEA #1:
Spotify Extended History Listening Habits

I would like to create a web application that takes the extended history of a user and presents them with charts on their listening habits. 

Functionalities:
    - User should be able to select any time period in their history 
    - Access all Playlists and playlist information
    - Information on mood, top songs, favorite genres, artists and songs
    - Possibly recommendations on songs based on playlist, mood or specific period

Week 4: Create an api client that can interact with the spotify api client and download data
Week 5: Scope out a user dataset to see what information there is and how to parse it and then parse it
Week 6:Implement functionalities based on data and ensure that we have meaningful results
Week 7: Implement a frontend platform to take user input and relay to backend
Week 8: Implement a visualization tool to display analysis information


PROJECT IDEA #2:
PDF chatbot
This is a project that will allow a user to upload a pdf and query it. This will use the embeddings from OpenAI and LangChain and PyPDF as a pdf reader

Functionalities:
User should be able to upload a pdf to the application and get feedback on whether it is parsable or not
User should be able to simply query the bot and get information from the pdf
User should be able to upload multiple pdfs within some total pages limit

Week 4: Research on how embeddings, parsing, chunking etc works and how to set up the  project for success. Scope out what libraries and packages will be needed 
Week 5: Implement parsing and inspect parsing for several pdfs and explore cleaning of parsed data
Week 6: Implement remaining aspects of application 
Week 7-8: Test application efficiency for different pdfs and prompts and ensure that application works reasonably



PROJECT IDEA #3 (Optional):
Amazon Customer Review Sentiment Analysis

This will allow a user to input a specific product and get the overall sentiment of users from the review comments. The sentiments will be simple : great, neutral and bad

Functionalities:
Should take in a specific product id or product url and run a sentiment analysis on its reviews
Should be able to compare reviews for two products 


Week 4: - Scope out datasets available to see which will be most suitable. 
	    - Research on best training algorithms for project
Week 5-6: Clean dataset and train a couple of algorithms on it for the best efficiency
Week 7: Implement functionality to take in user input, scrape reviews for product and clean them
Week 8: Implement functionality to get analysis on data for multiple products
