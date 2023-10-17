# Import necessary modules
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from twilio.twiml.messaging_response import MessagingResponse
import requests

# Function to retrieve a random joke from a web API
def get_joke():
    url = "https://v2.jokeapi.dev/joke/Programming,Miscellaneous?blacklistFlags=religious,political,racist,sexist"
    response = requests.get(url)
    if response.status_code == 200:
        joke_data = response.json()
        if joke_data.get("type") == "single":
            return joke_data.get("joke")
        elif joke_data.get("type") == "twopart":
            return f"{joke_data.get('setup')} {joke_data.get('delivery')}"
    return "Sorry, I couldn't find a joke for you."

# Initialize a Flask web application
app = Flask(__name__)

# Route for handling voice requests
@app.route('/voice', methods=['POST'])
def voice():
    joke = get_joke()
    resp = VoiceResponse()
    resp.say(joke)  # Respond with the retrieved joke using voice

    return str(resp)

# Route for handling SMS (text) requests
@app.route('/sms', methods=['POST'])
def sms():
    joke = get_joke()
    number = request.form['From']
    resp = MessagingResponse()
    resp.message(f"Hello {number}, this is your joke of the day!\n{joke}")  # Respond with the retrieved joke via SMS

    return str(resp)

# Start the Flask application when this script is run
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)