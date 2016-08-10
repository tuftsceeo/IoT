# blink_tweet.py
# Purpose: to flash an LED whenever a tweet in the world is posted with '#yes';
#          shows how the virtual world can affect the physical world
# By: Bianca Capretta
# Date: August 8th, 2016
# Used this tutorial for help: https://learn.sparkfun.com/tutorials/raspberry-pi-twitter-monitor

import time
import grovepi
from twython import TwythonStreamer

# Search terms
TERMS = '#yes'

# connections
LED = 4

# twitter application authentication
APP_KEY = 'fU0tfgDqBNFbvOaioNSb0U7fe'
APP_SECRET = 'twoKiW0Re1t5wUJth2wCQwy6XR3zT8kIf3KJwBkp3qFG7wGCK7'
OAUTH_TOKEN = '756129972075556864-qCwlEdp78HxKJGNVS8fXwVr4Id7rrtt'
OAUTH_TOKEN_SECRET = 'nMnG50nvjiFlvdC866wrCzoieBCuLgB5tSKXsA2eeBJTa'

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')
            print
            # when tweet with #yes found, blink LED
            grovepi.digitalWrite(LED, 1)
            time.sleep(1)
            grovepi.digitalWrite(LED, 0)

# setup LED as output
grovepi.pinMode(LED, "OUTPUT")
grovepi.digitalWrite(LED, 0)

print "Looking for tweets with " + TERMS + "\n"

# create streamer
try:
    stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    # filters through every tweet posted in the moment  
    stream.statuses.filter(track=TERMS)

except KeyboardInterrupt:
        exit()
