# button_tweet.py
# Purpose: to tweet whethe current distance between the ultrasonic sensor 
#          and the closest object when the button is pressed
# Date: August 9thOB, 2016
# By: Bianca capretta
# used python twitter tutorial for assistance: nodotcom.org/python-twitter-tutorial.html

from setuptools import setup
import tweepy
import time
import grovepi
import math

# connections
ultrasonic_ranger = 4
button = 3

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def main():
    cfg = {
        "consumer_key":'9iHdYDCrzpNefQqtUyDh7tScN',
        "consumer_secret":'pYP8c8njj3vtJqeoDNZpR2kMwuNi0LQKmiGnBlL1Dg5sylEUyI',
        "access_token":'756129972075556864-8G9mT1j8RxOx7cgrTbWsQ9CqrK3f0iG',
        "access_token_secret":'ZmjDVFHZgYKNvI0Cr2bKQfSYue2tOh4R6uLBWblRUndvN'
    }

    grovepi.pinMode(button, "INPUT")
    print "Waiting for button to be pressed"

    while True:
        try:
            # get value of button status
            button_status = grovepi.digitalRead(button)

            # if button pressed
            if button_status == 1:
                api = get_api(cfg)
                print "I am posting a tweet via GrovePi!"
                
                # captures distance between ultrasonic sensor and the closest object
                distance = grovepi.ultrasonicRead(ultrasonic_ranger)
                tweet = "There is currently an object " + str(distance) + " cm away from my$
                status = api.update_status(status=tweet)
                # immediately print tweet
                print(tweet)
        except IOError:
            print("Error")
        except KeyboardInterrupt:
            exit()

# run program
main()
