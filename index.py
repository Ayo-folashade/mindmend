from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import os
from dotenv import load_dotenv

from chatbot import setup_chain

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Set secret key
app.secret_key = os.getenv('secret_key')

# Initialize chain variable
chain = None


# Define route for home page
@app.route("/")
def hello():
    return render_template("home.html")


# Define route for start page
@app.route("/start")
def start():
    if "OPENAI_API_KEY" in session:
        return redirect(url_for("chat"))
    else:
        # If not logged in, redirect to the login page
        return redirect(url_for("login"))


# Define route for login page
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


# Define route for chat page
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

        # Return the chatbot response as JSON
        return jsonify({"message": message, "bot_reply": response})

    else:
        # If it's a GET request, render the chat page
        return render_template("chat.html")


# Define route for ending the chat
@app.route('/end_chat')
def end_chat():
    # Clear the session
    session.clear()

    # Redirect to the start page
    return redirect(url_for('start'))


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
