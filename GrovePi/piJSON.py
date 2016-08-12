# piJSON.py
# Purpose: to accept JSON strings from an input and interpret get and set requests;
#          uses wrapper functions to call grovepi functions
# Date: August 10th, 2016
# By: Bianca Capretta
# Used tutorial for assistance: https://www.raspberrypi.org/learning/python-web-server-with-flask/worksheet/

from flask import Flask, render_template,  request, json
from flask_cors import CORS, cross_origin
import logging, time, math
import grovepi, grove_rgb_lcd
import tweepy

# sets the language to standard English characters
PYTHONIOENCODING = 'utf-8'

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# connects to static interface using IP address
CORS(app, resources=r'/*', origin="130.64.94.22:8888", methods=["GET", "POST"])

# considers if reqeust is a GET or a POST
@app.route('/', methods=["GET", "POST"])
def index():
        # POST sends info to the GrovePi
        if request.method == "POST":
                JSONinput = request.get_data() # take in JSON string from the request

                data = json.loads(JSONinput) # turns JSON string into Python Dictionary 

                requesteddata = str(process_command(data))
                return json.jsonify(httpCode=200, value=requesteddata)

        # GET asks for info from my server
        elif request.method == "GET":
                return "Successful get request"

# purp: to take the received input as a dictionary and interpret the values
#       to do the requested action
def process_command(data):
        status = data['status'] # what you want to do: get/set
        io_type = data['io_type'] # type of input or output

        result = "Not found" # default value
        if status == 'get':
                if io_type == 'button':
                        result = get_button(data['port'], data['settings'])
                if io_type == 'led':
                        result = get_led(data['port'], data['settings'])
                if io_type == 'rotary_angle_sensor':
                        result = get_rotary_angle_sensor(data['port'], data['settings'])
                if io_type == 'sound':
                        result = get_sound(data['port'], data['settings'])
                if io_type == 'temperature':
                        result = get_temperature(data['port'], data['settings'])
                if io_type == 'light_sensor':
                        result = get_light_sensor(data['port'], data['settings'])
                if io_type == 'ultrasonic':
                        result = get_ultrasonic(data['port'], data['settings'])
        if status == 'set':
                if io_type == 'led':
                        set_led(data['port'], data['settings'])
                if io_type == 'buzzer':
                        set_buzzer(data['port'], data['settings'])
                if io_type == 'relay':
                        set_relay(data['port'], data['settings'])
                if io_type == 'display':
                        set_display(data['settings'])
                if io_type == 'twitter':
                        set_tweet(data['settings'])
                return "successful set"
        return result

# purp: to return state of button (on/off) 
def get_button(port, settings):
        try:
                if settings['touch_mode'] == 'raw_touch':
                        return grovepi.digitalRead(port)
        except ValueError:
                return "Not found"

# purp: to return state of LED (on, off)
def get_led(port, settings):
        try:
                if settings['led_mode'] == 'raw_led':
                        return grovepi.digitalRead(port)
        except ValueError:
                return "Not found"

# purp: to return the potentiometer value (in analog or degrees)
def get_rotary_angle_sensor(port, settings):
        try:
                if settings['angle_mode'] == 'raw_angle':
                        if settings['units'] == 'analog':
                                return grovepi.analogRead(port)
                        elif settings['units'] == 'degrees':
                                sensor_value = grovepi.analogRead(port)
                                voltage = round((float)(sensor_value)*5/1023, 2)
                                degrees = round((voltage*300)/5, 2) # 300 is the full value of the rotary angle
                                return degrees

        except ValueError:
                return "Not found"
                
# purp: to return the sound strength of environment from microphone
def get_sound(port, settings):
        try:
                if settings['sound_mode'] == 'raw_volume':
                        if settings['units'] == 'voltage':
                                return (grovepi.analogRead(port)/1024) * 5
                        elif settings['units'] == 'analog':
                                return grovepi.analogRead(port)
        except ValueError:
                return "Not found"

# purp: to return temperature (in celsius and fahrenheit) and humidity of the environment
def get_temperature(port, settings):
        try:
                if settings['temp_mode'] == 'raw_temp':
                        if settings['units'] == 'celsius':
                                return grovepi.dht(port, 1)
                        elif settings['units'] == 'fahrenheit':
                                return (grovepi.dht(port, 1)*1.8) + 32
        except ValueError:
                return "Not found"

# purp: to return light intensity of the environment
def get_light_sensor(port, settings):
        try:
                if settings['light_mode'] == 'raw_light':
                        return grovepi.analogRead(port)
        except ValueError:
                return "Not found"

# purp: to return distance of object in front of sensor (in centimeters or inches)
def get_ultrasonic(port, settings):
        try:
                if settings['ultrasonic_mode'] == 'distance':
                        if settings['units'] == 'cm':
                                return grovepi.ultrasonicRead(port)
                        elif settings['units'] == 'in':
                                return grovepi.ultrasonicRead(port) * 0.393701
        except ValueError:
                return "Not found"

# purp: to turn the LED on or off
def set_led(port, settings):
        try:
                # sets the LED to be the value thats passed in
                if settings['led_mode'] == 'on':
                        grovepi.digitalWrite(port, 1)
                elif settings['led_mode'] == 'off':
                        grovepi.digitalWrite(port, 0)
        except ValueError:
                return "Not found"
                
# purp: to turn buzzer on or off
def set_buzzer(port, settings):
        try:
                if settings['buzz_mode'] == 'on':
                        grovepi.digitalWrite(port, 1)
                elif settings['buzz_mode'] == 'off':
                        grovepi.digitalWrite(port, 0)
        except ValueError:
                return "Not found"

# purp: to switch voltages and currents
def set_relay(port, settings):
        try:
                if settings['relay_mode'] == 'on':
                        grovepi.digitalWrite(port, 1)
                elif settings['relay_mode'] == 'off':
                        grovepi.digitalWrite(port, 0)
                elif settings['relay_mode'] == 'switch':
                        state = grovepi.digitalRead(port)
                        if state == 1:
                                grovepi.digitalWrite(port, 0)
                        elif state == 0:
                                grovepi.digitalWrite(port, 1)
        except ValueError:
                return "Not found"

# purp: to show message on LCD display monitor
# NOTE port isn't important b/c it's a 12C connector
def set_display(settings):
        try:
                if settings['display_mode'] == 'post':
                        # sets color on monitor
                        if settings['color'] == 'red':
                                grove_rgb_lcd.setRGB(255, 0, 0)
                        elif settings['color'] == 'green':
                                grove_rgb_lcd.setRGB(0, 255, 0)
                        elif settings['color'] == 'blue':
                                grove_rgb_lcd.setRGB(0,0, 255)

                        # prints out message on display monitor
                        grove_rgb_lcd.setText(settings['message'])

        except ValueError:
                return "Not found"

# send a tweet
def set_tweet(settings):
        try:
                def get_api(cfg):
                        auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
                        auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
                        return tweepy.API(auth)


                cfg = {
                        "consumer_key":'9iHdYDCrzpNefQqtUyDh7tScN',
                        "consumer_secret":'pYP8c8njj3vtJqeoDNZpR2kMwuNi0LQKmiGnBlL1Dg5sylEUyI',
                        "access_token":'756129972075556864-8G9mT1j8RxOx7cgrTbWsQ9CqrK3f0iG',
                        "access_token_secret":'ZmjDVFHZgYKNvI0Cr2bKQfSYue2tOh4R6uLBWblRUndvN'
                }

                api = get_api(cfg)

                if settings['tweet_mode'] == 'post':
                        status = api.update_status(status=settings['message'])
                        print(settings['message'])

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

