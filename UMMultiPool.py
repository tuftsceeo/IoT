# Useless Machine Multi-Threading

from ev3dev import *
import ev3dev.ev3 as ev3
from multiprocessing import Pool
import time


ts_curr = True
ts2_curr = True


def interpret_command(info):
    m = ev3.LargeMotor('outA')
    ts = ev3.TouchSensor('in1')
    ts2 = ev3.TouchSensor('in4')

    global ts_curr # 1st touch sensor, attached to lever; last saved state
    global ts2_curr  # 2nd touch sensor, reliant on to arm; last saved state

    sm, sep, port = info.partition(":")

    if sm == 'TOUCH':
        if port == 'in1':  # port
            # if lever is not pressed, stop
            if ts_curr == False and ts.value() == 1:
                ts_curr = True
            while ts_curr == True and ts.value() == 1:
                m.stop()

            # if lever is pressed, 'unpress' the button with the arm
            if ts_curr == True and ts.value() == 0:
                ts_curr = False
            while ts_curr == False and ts.value() == 0:
                m.run_forever(duty_cycle_sp=60)

        if port == 'in4':
            # if the arm is not resting, return to resting position
            while ts.value() == 1 and ts2.value() == 0:
                m.run_forever(duty_cycle_sp=-30)


def main():

    tm_start = time.time()
    tm = 8

    sensors = ['TOUCH:in1', 'TOUCH:in4']

    p = Pool()

    while time.time() < tm_start + tm:
#        for item in sensors:
#            interpret_command(item)
        results = p.map(interpret_command, sensors)

    p.close()
    p.join()

    print('Took {}'.format(time.time() - tm))


main()
