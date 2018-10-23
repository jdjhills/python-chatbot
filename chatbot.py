import string
from Socket import openSocket, sendMessage
from initialise import joinRoom
from Read import getUser, getMessage

s = (openSocket())
joinRoom(s)
readBuffer = ""

while True:
    readBuffer = readBuffer + (s.recv(1024)).decode()
    temp = readBuffer.split("\r\n")
    readBuffer = temp.pop()

    for line in temp:
        print(line)
        user = getUser(line)
        message = getMessage(line)
        if "PING" in line:
            sendMessage(s, line.replace("PING", "PONG"))
            print("PONG sent")
        if "!name" in line:
            nameResponse = "Your name is: " + user
            sendMessage(s, nameResponse)
        print(user + " typed: " + message)



