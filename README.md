# MINDMEND

This README provides an overview of the files and functionality of the chatbot implemented in the codebase. The chatbot is designed to provide answers related to mental health queries using conversational AI.

## Files
The codebase consists of the following files:

- [chatbot.py](): This file contains the setup function to initialize the chatbot chain and define the necessary components for the chatbots operation.

- [index.py](): This file contains the Flask application that serves as the backend for the chatbot. It handles the routing and communication with the frontend.

- [streamlit.py](): This file contains the Streamlit application that provides a user interface for the chatbot.

- [Mental_Health_FAQ.csv](): This CSV file contains the dataset used as the knowledge base for the chatbot. It stores questions and corresponding answers related to mental health.

- [templates/](): This directory contains the HTML templates used for rendering the frontend pages.

- [avatar/](): This directory contains the bot avatar image [bot_avatar.jpeg]() used in the Streamlit application.

- [.streamlit/config.toml]() : This is a configuration file used by Streamlit to customize the appearance of the application in terms of background color, text color, fonts, e.t.c.

## Prerequisites
Before running the chatbot, ensure you have the following:

- Python 3.x installed
- Required Python packages installed (Flask, dotenv)

## Setup
1. Download the codebase and extract it to your local machine.


2. Install the required Python packages by running the following command in the project directory:
```
pip install flask python-dotenv
```
3. Set up the OpenAI API key by creating a .env file in the project directory. Add the following line to the .env file, replacing <your_api_key> with your actual OpenAI API key:
```
OPENAI_API_KEY=<your_api_key>
```

## Usage

### Flask Application
1. Run the Flask application by executing the following command in the project directory:
```
python index.py
```
2. Open a web browser and navigate to http://localhost:5000 to access the chatbot.


3. If you are a new user, click on the "Start" button to enter your OpenAI API key and login. If you already have an API key stored in your session, you will be redirected to the chat page directly.


4. On the chat page, enter your queries related to mental health in the text input field and press Enter or click the "Send" button to submit the message.


5. The chatbot will process your message and provide a response based on the knowledge base. The conversation will continue by exchanging messages with the chatbot.


6. To end the chat session, click on the "End Chat" button. This will clear the session and redirect you to the login page.

### Streamlit Application

1. Run the Streamlit application by executing the following command in the project directory:
```
streamlit run streamlit.py
```

2. Open a web browser and navigate to the URL displayed in the terminal to access the chatbot.


3. On the chat page, enter your queries related to mental health in the text input field and press Enter or click the "Enter" button to submit the message.


4. The chatbot will process your message and provide a response based on the knowledge base. The conversation will continue by exchanging messages with the chatbot.

## Important Note
Please ensure that you have a valid OpenAI API key to use the chatbot. If you don't have one, sign up for an API key at the OpenAI website before running the chatbot.

It's also important to note that the [Mental_Health_FAQ.csv]() file should be properly formatted with questions and answers related to mental health. Ensure that the file is present in the project directory and correctly structured to provide accurate responses.

