# tutorial for set-up found here: https://www.raspberrypi.org/learning/python-web-server-with-flask/worksheet/
from flask import Flask, render_template, request
from ev3dev.auto import *
import ev3dev.ev3 as ev3

m = ev3.LargeMotor('outA')
ts1 = ev3.TouchSensor('in1')

app = Flask(__name__)

# Inspiration for methods parameter and if method == format
# https://github.com/distortenterprises/Webinterface
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print("Command received")
        if request.form['direction']=='forward':
            m.run_forever(duty_cycle_sp = 40)
        if request.form['direction']=='backward':
            m.run_forever(duty_cycle_sp = -40)
        print(request.form['direction'])
        if request.form['direction']=='stop':
            m.stop()
        if ts1.value() == True:
            m.run_timed(time_sp = 1000, duty_cycle_sp = 75)   
        print("Command processed")
        return render_template('index.html')

    elif request.method == "GET":
        return render_template('index.html')

@app.route('/1')
def index1():
    return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
