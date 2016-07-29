# appString.py
#   purp:
#   created by:
#   edited by:

# tutorial for set-up found here: https://www.raspberrypi.org/learning/python-web-server-with-flask/worksheet/
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from ev3dev import *
import ev3dev.ev3 as ev3
import logging, time
import json

PYTHONIOENCODING = 'utf-8'  # should usually fix the UNIX file lang. bug; it seems to think it's ASCII characters

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)  # basic logging, prints when request received

# UNCOMMENT line below for thorough debugging
# logging.getLogger('flask_cors').level = logging.DEBUG

# run the app through CORS which will allow other computers to access your server;
# resources = pages, * = all, / = root; so /* = all pages off root/index;
# origin is allowed list of IP addresses besides yours, method is what they can do with your webpages
CORS(app, resources=r'/*', origin="http://130.64.94.22:8888/", methods=["GET", "POST"])


# main page is called index, it's at root ('/') and it catches and processes JSON requests
# Inspiration for methods parameter and if method == format: https://github.com/distortenterprises/Webinterface
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.get_data()

        print("Command received")
        status, sm_type, port, info, value = data.split(':')
        value = int(value)
#        print(
#            "status is ", status, " and sm_type is", sm_type, " and port is ", port, " and info is ", info,
#            " and value is ", value)
        requesteddata = str(process_command(status, sm_type, port, info, value))
        return '{"httpCode": 200, "value": ' + requesteddata + '}'

    elif request.method == "GET":
        # return render_template('index.html')
        return "Successful get request"


def process_command(status, sm_type, port, info, value):
    result = "Not found"
    if status == 'Get' or status == 'get':
        if sm_type == 'touch':
            result = get_touch(port, info)
        if sm_type == 'large motor':
            result = get_lm(port, info)
    if status == 'Set' or status == 'set':
        if sm_type == 'large motor':
            set_lm(port, info, value)
            return "-1"
    return result


def get_touch(port, info):
    try:
        if info == 'value':
            return ev3.TouchSensor(port).value()
    except ValueError:
        return "Not found"


def get_lm(port, info):
    try:
        if info == 'position':
            return ev3.LargeMotor(port).position()
    except ValueError:
        return "Not found"


def set_lm(port, info, value):
    try:
        i = ev3.LargeMotor(port)
        power = value
        if info == 'run_forever':
            i.run_forever(duty_cycle_sp=power)
            # i.run_timed(time_sp = 3000, duty_cycle_sp = value)
        if info == 'stop':
            i.stop()
        if info == 'reset':
            i.reset()
    except ValueError:
        return "Not found"


@app.route('/1', methods=["GET", "POST"])
def index1():
    if request.method == "POST":
        if request.form['direction'] == 'forward':
            m.run_forever(duty_cycle_sp=40)
        if request.form['direction'] == 'backward':
            m.run_forever(duty_cycle_sp=-40)
        if request.form['direction'] == 'stop':
            m.stop()
        print("Command received")
        print(request.form['direction'])
        return render_template('index.html')
    if request.method == "GET":
        return render_template('index.html')


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
