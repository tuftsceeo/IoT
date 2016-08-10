FunctionList
  purp: shows each input and output object's get and set functions and options

Large/Medium Motor
--------------
~ get_motor ~ can return  
- position (in rotations or degrees)  
- duty_cycle (read about tachometer motors; power)  
- speed  

~ set_motor ~ can change  
- run_forever (Will cause an error but is okay)  
- run_timed ()  
- stop  
- reset  
- switch  

Touch Sensor
--------------
~ get_touch ~ can return  
- raw_touch (aka touch sensor value)  

Ultrasonic Sensor
--------------
~ get_ultrasonic ~ can return  
- distance (in cm and in)  

Color/Light Sensor
--------------
~ get_color ~ can return  
- reflected  
- ambient  
- color  

Gryo Sensor
--------------
Not currently implemented with wrapper functions

LED
--------------


Brick Buttons
--------------
~ get_button ~ can return  
- raw_touch (aka whether a brick button is pressed; for left, right, up, down, enter and backspace)  

Sound
--------------

