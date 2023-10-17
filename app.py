from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from twilio.twiml.messaging_response import MessagingResponse
import requests

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

app = Flask(__name__)

@app.route('/voice', methods=['POST'])
def voice():
    joke = get_joke()
    resp = VoiceResponse()
    resp.say(joke)

    return str(resp)

@app.route('/sms', methods=['POST'])
def sms():
    joke = get_joke()  # Fix the typo here
    number = request.form['From']
    resp = MessagingResponse()
    resp.message(f"Hello {number}, this is your joke of the day!\n{joke}")

    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)