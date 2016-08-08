# monitor.py
# Purpose: to control an RGB Backlight display through input from a web-browser       
# Date: August 8th, 2016
# By: Bianca Capretta

from flask import Flask, render_template, request
import grovepi, grove_rgb_lcd

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
        try:
                if request.method == "POST":
                        print("Command received")

                        # captures inputted message and clicked color on web page
                        message = request.form['message']
                        color = request.form['color']

                        # takes user's info to print out message and color on screen
                        if message == '':
                                return "No message entered"
                        elif color == 'red':
                                grove_rgb_lcd.setRGB(255, 0, 0)
                                grove_rgb_lcd.setText(message)
                        elif color == 'green':
                                grove_rgb_lcd.setRGB(0, 255, 0)
                                grove_rgb_lcd.setText(message)
                        elif color == 'blue':
                                grove_rgb_lcd.setRGB(0, 0, 255)
                                grove_rgb_lcd.setText(message)

                        print("Command processed")

                        return render_template('monitor.html')

                elif request.method == "GET":
                        return render_template('monitor.html')
        except ValueError:
                return "Not found"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
