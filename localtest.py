from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    #"""Respond to incoming calls with a simple text message."""
 
    return 'hello'
 
if __name__ == "__main__":
    app.run(debug=True)