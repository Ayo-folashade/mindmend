from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import os
from dotenv import load_dotenv

from chatbot import setup_chain


load_dotenv()


app = Flask(__name__)

app.secret_key = os.getenv('secret_key')

chain = None


@app.route("/")
def hello():
    return render_template("home.html")


@app.route("/start")
def start():
    if "OPENAI_API_KEY" in session:
        return redirect(url_for("chat"))
    else:
        # If not logged in, redirect to the login page
        return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Retrieve the API key from the form data
        apikey = request.form.get("apikey")

        # Store the API key in the session
        session["OPENAI_API_KEY"] = apikey

        # Initialize the LLM chain with the user's API key
        os.environ["OPENAI_API_KEY"] = apikey

        return redirect(url_for("chat"))

    return render_template("login.html")


@app.route("/chat", methods=["GET", "POST"])
def chat():
    print("Session data:", session)  # Print session data
    global chain  # Access the global chain object

    # Check if the API key is in the session
    if "OPENAI_API_KEY" not in session:
        # If the API key is not in the session, redirect to the login page
        return redirect(url_for("login"))

    if request.method == "POST":
        # Get the chat message from the POST data
        message = request.form.get("message")

        # Initialize the LLM chain if it has not been initialized yet
        if chain is None:
            chain = setup_chain()

        # Pass the chat message to the LLM chain
        response = chain.run(message)

        # Return the chatbot's response as JSON
        return jsonify({"message": message, "bot_reply": response})

    else:
        # If it's a GET request, render the chat page
        return render_template("chat.html")

@app.route('/end_chat')
def end_chat():
    # Clear the session
    session.clear()

    # Redirect to the start page
    return redirect(url_for('start'))



if __name__ == "__main__":
    app.run(debug=True)