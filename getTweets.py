import api_key_config as config
from listener import StdOutListener
from tweepy import OAuthHandler
from tweepy import Stream

import sys

consumer_key = config.api_key
consumer_secret = config.api_secret
access_token = config.access_token
access_secret = config.token_secret
 

if __name__ == '__main__':
    args=sys.argv
    del args[0]
    listener=StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth,listener)

    stream.filter(track=args)


