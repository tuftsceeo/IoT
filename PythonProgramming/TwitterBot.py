# TwitterBot.py
# purp: to send a user-input tweet whenever the user presses a touch sensor (in port '1')
# last updated: by J.F on July 25, '16 to add comments
# created by: Juliana Furgala

from ev3dev import *
import ev3dev.ev3 as ev3
from multiprocessing import Pool
import time
import tweepy


# information for this demo function and code outline came from an online tutorial at:
# nodotcom.org/python-twitter-tutorial.html
def sendTweet():
    def get_api(cfg):
        auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
        auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
        return tweepy.API(auth)

    cfg = {
        "consumer_key": "JoSQnthNuxFuNDANF7gLKHAhg",
        "consumer_secret": "Hu0ShH3pU5Ejxp2HR6njwxRjVDVoKrp34G4vt9RF4pq5Tn7Yv7",
        "access_token": "4386651495-uBBJfHnhegqqZE6XFPC8eYre8CZtTJYBkTo3hVy",
        "access_token_secret": "dZPNiJpxiz6gaKg4GBPVoxudfWulo5bunvgGEdvOHNaJK"
    }

    api = get_api(cfg)
    tweet = "Is it ironic"  # your message
    print(tweet)
    status = api.update_status(status=tweet)
    print(status)


def main():

    ts = ev3.TouchSensor('in1')

    tm_start = time.time()

    p = Pool()

    while time.time() < tm_start + 5:

        if ts.value():
            # message = raw_input("What message would you like to post? : ")
            sendTweet()
            results = p.map(sendTweet())
            print('Took {}'.format(tm_start - time.time()))

    p.close()
    p.join()


main()
