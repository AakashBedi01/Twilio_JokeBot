# Import necessary modules
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from twilio.twiml.messaging_response import MessagingResponse
import requests


# Function to retrieve a random joke from a web API
def get_joke():
    # Define the URL of the joke API
    url = "https://v2.jokeapi.dev/joke/Programming,Miscellaneous?blacklistFlags=religious,political,racist,sexist"

    try:
        # Attempt to make an HTTP GET request to the joke API
        response = requests.get(url)

        # Check for HTTP request errors and raise an exception if there's an issue
        response.raise_for_status()

        # Parse the joke data from the response
        joke_data = response.json()

        # Check the type of joke (single-part or two-part) and construct the joke accordingly
        if joke_data.get("type") == "single":
            return joke_data.get("joke")
        elif joke_data.get("type") == "twopart":
            return f"{joke_data.get('setup')} {joke_data.get('delivery')}"

    except requests.exceptions.RequestException as e:
        # Handle exceptions related to the HTTP request (e.g., network issues)
        error_message = f"Failed to retrieve a joke. Request Exception: {str(e)}"
        return error_message

    except Exception as e:
        # Handle any other unexpected exceptions
        error_message = f"An error occurred: {str(e)}"
        return error_message

    # If no valid joke is found, return a default error message
    return "Sorry, I couldn't find a joke for you."


app = Flask(__name__)


# Route for handling voice requests
@app.route('/voice', methods=['POST'])
def voice():
    # Get a random joke
    joke = get_joke()

    # Create a Twilio VoiceResponse to deliver the joke via voice
    resp = VoiceResponse()
    resp.say(joke)

    return str(resp)


# Route for handling SMS (text) requests
@app.route('/sms', methods=['POST'])
def sms():
    try:
        # Get a random joke
        joke = get_joke()

        # Get the sender's phone number from the request
        number = request.form['From']

        # Create a Twilio MessagingResponse to send the joke as an SMS
        resp = MessagingResponse()
        resp.message(f"Hello {number}, this is your joke of the day!\n{joke}")
        return str(resp)

    except Exception as e:
        # Handle any unexpected exceptions that may occur during SMS processing
        error_message = f"An error occurred: {str(e)}"
        return error_message


if __name__ == "__main":
    # Start the Flask application, listening on the specified host and port
    app.run(host='0.0.0.0', port=5000)
