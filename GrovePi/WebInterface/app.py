# app2.py
# Purpose: to control an LED through input from a web-browser       
# Date: August 4th, 2016
# By: Bianca Capretta

from flask import Flask, render_template, request
import grovepi

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
        try:
                if request.method == "POST":
                        print("Command received")

                        # will turn into unicode if not turned into an int
                        port = int(request.form['port'])

                        # captures input from radio button and port
                        if request.form['port'] == '':
                                return "No port entered"
                        if request.form['light'] == 'on':
                                grovepi.digitalWrite(port, 1)
                        if request.form['light'] == 'off':
                                grovepi.digitalWrite(port, 0)

                        print("Command processed")

                        return render_template('index.html')

                elif request.method == "GET":
                        return render_template('index.html')
        except ValueError:
                return "Not found"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
