# WhatsApp_Chatbot
WhatsApp chatbot made for local coffee shops that can take customer orders right from WhatsApp chat

# Tools and Technologies
This chatbot was made with python (Flask) and Twilio Sandbox for whatsapp.
Heroku is used for cloud deployment.
Dialogflow for NLU and contextual conversations.

# Explaination
Project contains two files, app.py and util.py where app.py is main flask app and util.py is just some utility file needed in app.py
runtime, requirements and procfiles are required by heroku to deploy app in specific environment

app.py uses Flask and requests to redirect requests to specific paths by using route method on a specific existing path.
util.py has methods for detecting intents for bot and fetching the reply. It also contains project id and required json file which itself contains metadata and private key for dialogflow.

I'm not providing the actual json file as it contains private keys. You can generaate one for yourself by visiting dialogflow


# Purpose
To help local businesses like coffee shops and provide higher customer support and interaction.
The other day I was starving and wanted something to eat. I think it's boring and tedious task to always go and order from food ordering apps and provide details, why not just provide details once and just send a text to the number with food item everytime I want to eat something. This project achieves the same, just by sending the message on WhatsApp and confirming the order, I'll get what I need.
