from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import serial


app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def reply_sms():
    # Get the message sent to the Twilio number
    received_msg = request.values.get('Body', None)

    # Start the Twilio response
    resp = MessagingResponse()

    global msg
    recent_lines = str(ser.read(1024)).replace('\\t', '    ').split('\\r\\n')
    if len(recent_lines) > 2:
        msg = recent_lines[-2]

    resp.message(msg)

    return str(resp)


if __name__ == "__main__":
    port = 'COM6'
    baudrate = 9600
    ser = serial.Serial(port, baudrate, timeout=0)
    msg = 'No data yet'
    app.run()
