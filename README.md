# Twilio_JokeBot

## Overview
The Twilio JokeBot is a simple web application built with Flask and Twilio that delivers random jokes to users via both voice and SMS. This service fetches jokes from an external joke API and uses Twilio to communicate with users.

## Features
- Delivers random jokes to users in voice format or as SMS messages.
- Filters out jokes with specific blacklisted content (e.g., religious, political, racist, sexist).
- Provides error handling to handle potential issues with API requests and user interactions.

## Prerequisites
Before running the Twilio JokeBot, ensure you have the following:

- Python 3.x installed on your system.
- The required Python libraries, including Flask, Twilio, and Requests. You can install them using pip: `pip install Flask twilio requests`.

## Configuration
To use the Twilio JokeBot, you need to configure a few things:

1. Twilio Account:
   - Sign up for a Twilio account if you don't have one.
   - Obtain your Twilio Account SID, Auth Token, and a phone number to send SMS messages from.
   - Configure your Twilio account settings in the code by replacing the placeholders.

2. Joke API:
   - The service fetches jokes from an external joke API by default (https://v2.jokeapi.dev/). Ensure the API is accessible and reliable.

## Usage
1. Clone this repository to your local machine: git clone https://github.com/AakashBedi01/Twilio_JokeBot.git

2. Open a terminal and navigate to the project directory.

3. Run the Flask application:python app.py

4. Your Flask app should now be running locally. You can access it at `http://localhost:5000`.

5. To receive a joke, use Twilio's SMS service by sending an SMS to the provided phone number. You can also use the voice service by making a POST request to the `/voice` endpoint.

## Example
To receive a joke via SMS, send a text message to the configured phone number. You'll receive a response with a random joke.

To receive a joke via voice, make a POST request to `http://localhost:5000/voice` or deploy the app and configure a public URL for the voice service. You'll receive the joke as a spoken message.

## Error Handling
The application is equipped with error handling to provide user-friendly error messages in case of issues. Users will be notified if there are problems with the joke retrieval or any other errors.


## Acknowledgments
This project was created for educational and demonstration purposes and is not meant for production use. It uses external APIs and services, and you should ensure compliance with their terms and conditions.

## Contact
For questions or support, contact [Aakashdeep Singh Bedi](mailto:akashdeepsinghbedi@gmail.com).




