# WeatherApp

Using this requires ngrok (https://ngrok.com/download), Python 3.7, and the python modules pyserial, flask, and twilio

Verify your phone number on the tiwlio account so that it can receive messages (https://www.twilio.com/console/phone-numbers/verified)


Setting up the ngrok server:

  -Unzip the ngrok download, open your command prompt terminal, and run "C:\path\to\the\exe\file\ngrok.exe http 5000"
  
  -Copy the url that shows up that is similar to "https://9bb5398b.ngrok.io"
  
  -Go to "https://www.twilio.com/console/phone-numbers/incoming" and click on the phone number
  
  -Scroll to the bottom of the page, and in the field labelled "A message comes in", enter the ngrok url with "/sms" on the end, e.g. https://9bb5398b.ngrok.io/sms, and then click save


I included two python programs, one which should reply with the most recent line of the serial port, and another which replies with a generic message for testing purposes
