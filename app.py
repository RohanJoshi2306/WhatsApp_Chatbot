
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from util import fetch_reply

app = Flask(__name__)

# to test the server with some text instead of just blank page
@app.route("/")
def hello():
    return "Hello, World!" 

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    phone_no = request.form.get('From')

    reply = fetch_reply(msg, phone_no)

    # Create reply
    resp = MessagingResponse()
    #forexample
    #resp.message("You said: {}".format(msg))
    resp.message(reply)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)