# Twilio_JokeBot
Designed and developed a Twilio-based Joke Bot application using Python, Flask, and the Twilio API. This application can tell jokes to users via both voice calls and SMS messages. 

Joke Retrieval: The code utilizes the JokeAPI to fetch jokes, ensuring a wide range of joke types while avoiding inappropriate content.

Voice Response (Call Handling): For voice calls, I implemented a route ('/voice') that responds to incoming calls by generating TwiML using Twilio's twilio.twiml.voice_response. The bot answers calls with a random joke retrieved from the JokeAPI.

SMS Response: The code also handles incoming SMS messages via a separate route ('/sms'). When users send an SMS, the bot replies with a personalized message and the joke of the day.

Flask Web Application: The application is built using the Flask web framework, allowing it to receive and handle both voice and SMS requests from the Twilio API.

Dynamic Joke Generation: The application ensures a dynamic user experience by fetching a new joke for each interaction.
