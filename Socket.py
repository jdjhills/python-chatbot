'''
Everything below this line is from this YouTube video: https://youtu.be/T8DLwACpe3o,
modified slightly so that it works with the current version of Python.
'''
##################################################################################################
'''
The below functions are to do with IRC, which is a complex system in itself. With this script, we can
add anything we want on top of it. This is just how the bot communicates with Twitch.
'''
##################################################################################################

import socket

from settings import HOST, PORT, PASS, IDENT, CHANNEL


def openSocket():
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(bytes("PASS " + PASS + "\r\n",'UTF-8'))
    s.send(bytes("NICK " + IDENT + "\r\n",'UTF-8'))
    s.send(bytes("JOIN #" + CHANNEL + "\r\n",'UTF-8'))
    return s

def sendMessage(s, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send(bytes(messageTemp + "\r\n",'UTF-8'))
    print("Sent: " + messageTemp)

