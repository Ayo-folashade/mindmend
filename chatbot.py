import os
import pyttsx3 as pyttsx3
from dotenv import load_dotenv, find_dotenv
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader
from langchain.embeddings import OpenAIEmbeddings, openai
from langchain.indexes import VectorstoreIndexCreator
from langchain.vectorstores import DocArrayInMemorySearch
import streamlit as st

# Load environment variables from .env file
_ = load_dotenv(find_dotenv())

# Set OpenAI API key from environment variable
openai.api_key = os.environ['OPENAI_API_KEY']

# Load data from CSV file
file = 'data.csv'
loader = CSVLoader(file_path=file)
docs = loader.load()

# Initialize embeddings
embeddings = OpenAIEmbeddings()

# Create document search database
db = DocArrayInMemorySearch.from_documents(
    docs,
    embeddings
)

# Create index for search
index = VectorstoreIndexCreator(
    vectorstore_cls=DocArrayInMemorySearch
).from_loaders([loader])

# Create retriever
retriever = db.as_retriever()

# Create ChatOpenAI instance
llm = ChatOpenAI(temperature=0.0)

# Create RetrievalQA instance
qa_stuff = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    verbose=True
)


# Bot Avatar
def display_avatar():
    st.image("avatar/bot_avatar.jpeg", width=100)


# Text-to-speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# Set title and subheader/head
st.title("MindMend")
st.subheader("A Mental Wellness Support Chatbot")

# Multi-step Conversation
query = st.text_input("Enter your question:")
if query:
    response = index.query(query, llm=llm)
    if "follow_up_question" in response:
        follow_up_query = st.text_input(response["follow_up_question"])
        if follow_up_query:
            response = index.query(follow_up_query, llm=llm)
    st.text("Response:")
    display_avatar()
    st.markdown(f"**MindMend:** {response}")
    st.button("Read Response", on_click=lambda: speak(response))

# Error Handling
if not query:
    st.warning("Curious about something?")
