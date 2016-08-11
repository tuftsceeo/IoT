FunctionList
  purp: shows each input and output object's get and set functions and options for EV3JSON.py  
  
EV3JSON.py runs a flask (Python) server that takes in POST and GET requests. When it takes a POST request, it expects a  
JSON string with commands that it makes into a dictionary to be processed. The same format can be seen below.  

Some of the ev3dev functions are not very user friendly. Luckily I've made wrapper functions for most functions for all sensors and
motors except for the gyroscopic sensor. These wrapper functions also cover LEDs, sound (limited), and brick buttons. You can find
these functions in the EV3JSON.py file as they are used in the EventServer. You can use the Event Server and keep the format,
which would result in a simple brick (controlled by an interface) or to get a complex (autonomous) brick, you can have the brick host
its own interface like in the WebInterface folder. You would just need to change the parameters of the wrapper functions as they
currently want a JSON string like this: 

```{"status":"set","io_type":"large motor","port":"outA","settings":{"motor_mode":"run forever","power":25}}```

This is a command that will run a large motor in Port A at a power of 25. If you send a JSON string like this to the Event Server 
EV3 server file, then it will turn it into Python dictionary and interpret the fields to direct the command to the right get or set
function.

If you want to add anything, such as the ability to edit the screen's image while a program is running, or use a gyroscopic sensor,
you will have to write the wrapper functions yourself. I suggest adding them to the already existing functions in appJSON.py (under
EventServer) and updating the file. However most, if not all, basic wrapper functions are already written for you.

If there is something you need that is missing, bring it up as an issue and I can add it.


# Standard Sensors/Motors/Etc.

Large/Medium Motor
--------------
'get_motor' can return  
- position (in rotations or degrees)  
- duty_cycle (read about tachometer motors; power)  
- speed  

'set_motor' can change  
- run_forever (will cause an error but it's okay, there's a reason; it works; see ProblemAssistance.txt for details)  
- run_timed (time in ms)  
- stop  
- reset (should stop motor and reset encoder - aka set position to 0)  
- switch (should reverse direction of motor; right now only stops the motor which it shouldn't; is calling stop for some weird reason)  

Touch Sensor
--------------
'get_touch' can return  
- raw_touch (aka touch sensor value)  

Ultrasonic Sensor
--------------
'get_ultrasonic' can return  
- distance (in cm and in)  

Color/Light Sensor
--------------
'get_color' can return  
- reflected  
- ambient  
- color  

Gryo Sensor
--------------
Not currently implemented with wrapper functions

LED
--------------
'set_led' can change  
- on (sides: left, right, or both; colors: green, red, yellow, amber)
- off (sides: left, right, both)

Brick Buttons
--------------
'get_button' can return  
- raw_touch (aka whether a brick button is pressed; for left, right, up, down, enter and backspace)  

Sound
--------------
'set_sound' can change  
- tone (takes frequency, duration, delay; a tuple)
- note (NOT IMPLEMENTED since a dictionary would have to be build to recognize notes)
- file (file must be on brick)
- speech (text to speech)
- song (an array of tones; warning: always sounds like extreme guitar solo)

Program Wide / Other Misc Functions
--------------
'stop_all' stops all motors with coast; in a simple brick with a complex interface, this effectively stops the program as it does not
signal to itself to check sensors

# Digital Inputs and Outputs
'set_twitter' can  
- post to Twitter a message of your choice (It prompts you)
- ALSO can (but not implemented: check and/or return your 'home page', your most recent posts, your number of followers, etc.)
