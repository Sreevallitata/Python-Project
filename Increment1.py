Python 2.7.17 (v2.7.17:c2f86d86e6, Oct 19 2019, 20:49:36) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # -- coding: utf-8 --
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

#Variables that contains the user credentials to access Twitter API
access_token = "1010252295441825792-HcqSEtWnegQ5rmtwIpqorlHGLyFecN"
access_token_secret = "iN2vNlXGGQXhIydvcopNK4eno7xaffh07IH3Ya5ZZ3tVk"
consumer_key = "IMg8MqchgXh6cn24JYYnNxH1C"
consumer_secret = "ZesDxiZc9Bt26styNLMzoTp8p2ghZtvz8fbaPL2laF4s0BxxnQ"

# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """

    def _init_(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords:
        stream.filter(languages=["en"], track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    count=0

    def _init_(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            # print(data)
            with open(self.fetched_tweets_filename, 'a', newline='') as tf:
                tweet = json.dumps(data, ensure_ascii=False)
                tf.write(data)
                print(self.count,end=' ')
                self.count=self.count+1

            #		tweet = json.loads(data)
            #      	    with open('your_data.json', 'a') as my_file:
            #                json.dump(tweet, my_file)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        print("error "+str(status))


if _name_ == '_main_':
    # Authenticate using config.py and connect to Twitter Streaming API.
    hash_tag_list = ['stockmarket', 'bitcoin', 'money', 'trading', 'forextrader', 'investment', 'wallstreet', 'stocks', 'entrepreneur', 'forex', 'trader', 'investor', 'investing', 'cryptocurrency', 'invest', 'business', 'daytrader', 'binaryoptions', 'forexsignals', 'profit', 'success', 'finance', 'wealth', 'makemoneyonline', 'forexlifestyle', 'forextrading', 'motivation', 'millionaire', 'entrepreneurship', 'daytrading']
    fetched_tweets_filename = "tweets7.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
