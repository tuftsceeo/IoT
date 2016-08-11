FunctionList
  purp: shows each input and output object's get and set functions and options

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
