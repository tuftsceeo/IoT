# button_tweet.py
# Purpose: to send a tweet when you press the button sensor
# Date: August 3rd, 2016
# By: Bianca capretta
# used python twitter tutorial for assistance: nodotcom.org/python-twitter-tutorial.html

from setuptools import setup
import tweepy
import time
import grovepi
import math

# connections
led = 4
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

        grovepi.pinMode(led, "OUTPUT")
        grovepi.pinMode(button, "INPUT")

        while True:
                try:
                        button_status = grovepi.digitalRead(button) # get value of button status

                        if button_status == 1:
                                api = get_api(cfg)
                                tweet = "I am posting my first tweet via GrovePi!"
                                status = api.update_status(status=tweet)
                                print(tweet)
                        else:
                                print "Button not pressed"
                except IOError:
                        print("Error")
                except KeyboardInterrupt:
                        exit()

main()

