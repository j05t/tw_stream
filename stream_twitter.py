#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "429332942-XNoIEqAv03SOdS65tLPPaGld3LSJJ94qNh8SIgM4"
access_token_secret = "dZuVkQzz0s0HEQL1PWqOvifBjl2I7j9Jhq9ioiachypcy"
consumer_key = "CzyZhmfUtaQTULpkdT3iIUC8C"
consumer_secret = "5idjIb32uPQdfr5EIO60BVPTGyWCJyMebe02tiKizncNBbUeYj"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['data mining'])
