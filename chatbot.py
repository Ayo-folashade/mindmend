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

_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

file = 'data.csv'
loader = CSVLoader(file_path=file)
docs = loader.load()

embeddings = OpenAIEmbeddings()

db = DocArrayInMemorySearch.from_documents(
    docs,
    embeddings
)

index = VectorstoreIndexCreator(
    vectorstore_cls=DocArrayInMemorySearch
).from_loaders([loader])

retriever = db.as_retriever()
llm = ChatOpenAI(temperature=0.0)

qa_stuff = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    verbose=True
)


# query = "I feel sad"
# response = index.query(query, llm=llm)
# print(response)

# Bot Avatar
def display_avatar():
    st.image("bot_avatar.jpeg", width=100)


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
