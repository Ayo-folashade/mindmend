import os
import streamlit_app as st
from dotenv import load_dotenv, find_dotenv
from langchain.embeddings import openai

from chatbot import setup_chain

# Load environment variables
_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']


# Define bot avatar display function
def display_avatar():
    st.image("avatar/bot_avatar.jpeg", width=100)


# Define main function
def main():
    agent = setup_chain()

    # Set Streamlit app title and subheader
    st.title("MindMend")
    st.subheader("A Mental Wellness Support Chatbot")

    # User input text field
    user_input = st.text_input("Ask me anything! I'm here to help:")

    # Button to trigger chatbot response
    if st.button("Enter"):
        #  Get chatbot response
        response = agent.run(user_input)

        # Display bot avatar and chatbot response
        display_avatar()
        st.markdown(f"**MindMend:** {response}")


# Run the main function if the script is executed directly
if __name__ == '__main__':
    main()
