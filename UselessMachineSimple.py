# Useless Machine
from ev3dev import *
import ev3dev.ev3 as ev3
import time

m = ev3.LargeMotor('outA') # controls the 'arm'
ts = ev3.TouchSensor('in1') # affected by the lever
ts2 = ev3.TouchSensor('in4') # affected by the 'arm'

# just for fun, print the information from the first touch sensor (in port 1)
print ts.driver_name, ts.address, ts.mode, ts.num_values, ts.modes
# print ts.units - No units for touch sensor, bool
print " "
# also for fun, print the motor's information
print m.driver_name, m.address, m.commands, m.duty_cycle, m.position

go = True
while go == True # infinite loop
    # when the lever is not pushed, the first sensor is pressed
    while ts.value() == True:
        m.stop()
        continue
    # when the lever is pushed, the first sensor is unpressed; 
    # the goal - use the 'arm' to repress the sensor
    while ts.value() == False:
        m.run_forever(duty_cycle_sp = 60)
        continue
    # when the 'arm' has moved, the second sensor is not pressed;
    # the goal - repress it, so you move the arm back again until the sensor is re-pressed
    while ts2.value() == False:
        m.run_forever(duty_cycle_sp = -30)
        continue
