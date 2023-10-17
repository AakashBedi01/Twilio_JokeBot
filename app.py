from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from twilio.twiml.messaging_response import MessagingResponse
import requests


def get_joke():
    url = "https://v2.jokeapi.dev/joke/Programming,Miscellaneous?blacklistFlags=religious,political,racist,sexist"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        joke_data = response.json()
        if joke_data.get("type") == "single":
            return joke_data.get("joke")
        elif joke_data.get("type") == "twopart":
            return f"{joke_data.get('setup')} {joke_data.get('delivery')}"
    except requests.exceptions.RequestException as e:
        return f"Sorry, I couldn't retrieve a joke. Error: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
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
    try:
        joke = get_joke()
        number = request.form['From']
        resp = MessagingResponse()
        resp.message(f"Hello {number}, this is your joke of the day!\n{joke}")
        return str(resp)
    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
