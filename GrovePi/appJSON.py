# app.py
# Purpose: to create a user-responsive, GrovePi server that can interpret user form input
# Date: August 2nd, 2016
# By: Bianca Capretta
# Used tutorial for assistance: https://www.raspberrypi.org/learning/python-web-server-with-flask/workshee$

from flask import Flask, render_template,  request, json
from flask_cors import CORS, cross_origin
import logging, time
import grovepi, grove_rgb_lcd

# sets character encoding
PYTHONIOENCODING = 'utf-8'

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# connects to static interface using IP address
CORS(app, resources=r'/*', origin="130.64.94.22:8888", methods=["GET", "POST"])

# considers if reqeust is a GET or a POST
@app.route('/', methods=["GET", "POST"])
def index():
        if request.method == "POST":
                JSONinput = request.get_data()

                data = json.loads(JSONinput)

                requesteddata = str(process_command(data))
                return json.jsonify(httpCode=200, value=requesteddata)

        elif request.method == "GET":
                return "Successful get request"

# with data sent, process_command parses the status (get/set) and target sensor
def process_command(data):
        status = data['status']
        io_type = data['io_type']

        result = "Not found"
        if status == 'get':
                if io_type == 'button':
                        result = get_button(data['port'], data['info'])
                if io_type == 'led':
                        result = get_led(data['port'], data['info'])
                if io_type == 'rotary_angle_sensor':
                        result = get_rotary_angle_sensor(data['port'], data['info'], data['mode'])
                if io_type == 'sound':
                        result = get_sound(data['port'], data['info'], data['mode'])
                if io_type == 'temperature':
                        result = get_temperature(data['port'], data['info'], data['mode'])
                if io_type == 'light_sensor':
                        result = get_light_sensor(data['port'], data['info'], data['mode'])
                if io_type == 'ultrasonic':
                        result = get_ultrasonic(data['port'], data['info'], data['mode'])
        if status == 'set':
                if io_type == 'led':
                        set_led(data['port'], data['info'])
                if io_type == 'buzzer':
                        set_buzzer(data['port'], data['info'])
                if io_type == 'relay':
                        set_relay(data['port'], data['info'])
                if io_type == 'display':
                        set_display(data['info'], data['value'])
                return "successful set"
        return result
        
# WRAPPER FUNCTIONS

# returns state of button (on/off) 
def get_button(port, info):
        try:
                if info == 'value':
                        return grovepi.digitalRead(port)
        except ValueError:
                return "Not found"

# returns state of LED (on, off)
def get_led(port, info):
        try:
                if info == 'value':
                        return grovepi.digitalRead(port)
        except ValueError:
                return "Not found"

# turns the LED on or off
def set_led(port, info):
        try:
                # sets the LED to be the value thats passed in
                if info == 'on':
                        grovepi.digitalWrite(port, 1)
                elif info == 'off':
                        grovepi.digitalWrite(port, 0)
        except ValueError:
                return "Not found"

# returns the potentiometer value in analog and degrees
def get_rotary_angle_sensor(port, info, mode):
        try:
                if info == 'angle':
                        if mode == 'analog':
                                return grovepi.analogRead(port)
                        elif mode == 'degrees':
                                sensor_value = grovepi.analogRead(port)
                                voltage = round((float)(sensor_value)*5/1023, 2)
                                degrees = round((voltage*300)/5, 2) # 300 is the full value of the rotary $
                                return degrees

        except ValueError:
                return "Not found"

# microphone returns the sound strength of the environment
def get_sound(port, info, mode):
        try:
                if info == 'volume':
                        if mode == 'voltage':
                                return (grovepi.analogRead(port)/1024) * 5
                        elif mode == 'analog':
                                return grovepi.analogRead(port)
        except ValueError:
                return "Not found"

# returns temperature (in celsius and fahrenheit) and humidity of the environment
def get_temperature(port, info, mode):
        try:
                if info == 'temp':
                        if mode == 'celsius':
                                return grovepi.dht(port, 1)
                        elif mode == 'fahrenheit':
                                return (grovepi.dht(port, 1)*1.8) + 32
        except ValueError:
                return "Not found"

# this sensor detects the light intensity of the environment
def get_light_sensor(port, info):
        try:
                if info == 'value':
                        return grovepi.analogRead(port)
        except ValueError:
                return "Not found"

# turns buzzer on or off
def set_buzzer(port, info):
        try:
                if info == 'on':
                        grovepi.digitalWrite(port, 1)
                elif info == 'off':
                        grovepi.digitalWrite(port, 0)
        except ValueError:
                return "Not found"

# switches the voltages and currents
def set_relay(port, info):
        try:
                if info == 'switch':
                        grovepi.digitalWrite(port, 1)
                elif fino == 'stay':
                        grovepi.digitalWrite(port, 0)
        except ValueError:
                return "Not found"

# prints out message on LCD display monitor
# NOTE port isn't important b/c it's a 12C connector
def set_display(info, value):
        try:
                if info == 'post':
                        grove_rgb_lcd.setRGB(200, 0, 230)
                        grove_rgb_lcd.setText(value)
                # if nothing is sent, don't post anything
        except ValueError:
                return "Not found"

# returns distance of object in front of sensor (in centimeters and inches)
def get_ultrasonic(port, info, mode):
        try:
                if info == 'distance':
                        if mode == 'cm':
                                return grovepi.ultrasonicRead(port)
                        elif mode == 'in':
                                return grovepi.ultrasonicRead(port) * 0.393701
        except ValueError:
                return "Not found"

@app.errorhandler(400)
def client_error(error):
        app.logger.error('Client Error: %s', error)
        return ('{httpCode: %s}', error)

@app.errorhandler(500)
def internal_server_error(error):
        app.logger.error('Server Error: %s', error)
        return ('{httpCode: %s}', error)

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')

