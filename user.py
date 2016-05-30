from tweepy import  *
from sender import *
import tkinter
consumer_key = "djcotfrrPRyfHLkm9o43pBDe0"
consumer_secret = "dXgae46hj07iEqSbAfzZPjaJoEGmTFv26fajOACRgdy2XtWjIC"
access_token = "391827504-GSrkTvuWSK97uVpobrtCm3yKu3Axr3DEoouuFm2q"
access_tokenes_secret = "2oI8BPykczrmerNNFPb0WhFyTmEoB0sxQmkFL2p0sBSYD"
sender = Sender(consumer_key,consumer_secret,access_token,access_tokenes_secret)
def senderBtn(screenName,text):
    sender.sendMessage(screenName,text)
if __name__ == "__main__":
    pass




































