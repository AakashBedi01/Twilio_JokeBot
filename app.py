import requests
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse


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


if __name__ == "__main__":
    app.run(debug=True)
