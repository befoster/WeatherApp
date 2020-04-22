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

    # Send a reply
    msg = str(ser.readline()).strip()  # This *should* get the most recent serial port line, but I don't have an arduino to test it
    resp.message(msg)

    return str(resp)


if __name__ == "__main__":
    port = str(input('Serial port (e.g. COM1): '))
    baudrate = int(input('Baud rate (e.g. 9600): '))
    ser = serial.Serial(port, baudrate)
    app.run()
