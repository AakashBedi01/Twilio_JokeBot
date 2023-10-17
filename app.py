from typing import Any

import requests
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from twilio.twiml.message_response import MessagingResponse


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
    print(request.form)
    joke: get_joke()
    number = request.form['From']
    resp = MessagingResponse()
    resp.message(f"hello {number}, This is your joke of the day! \n {joke} ")


if __name__ == "__main__":
    app.run(debug=True)
