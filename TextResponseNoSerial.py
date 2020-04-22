from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def reply_sms():
    # Get the message sent to the Twilio number
    received_msg = request.values.get('Body', None)

    # Start the Twilio response
    resp = MessagingResponse()

    # Send a reply
    resp.message("Generic reply")

    return str(resp)


if __name__ == "__main__":
    app.run()
