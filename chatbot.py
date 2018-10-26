import string
from Socket import openSocket, sendMessage
from initialise import joinRoom
from Read import getUser, getMessage

s = (openSocket())
joinRoom(s)
readBuffer = ""
'''look at NLTM'''
#############################################################
''' Confusing IRC stuff '''
while True:  # Infinite loop
    readBuffer = readBuffer + (s.recv(1024)).decode()
    temp = readBuffer.split("\r\n")
    readBuffer = temp.pop()
#############################################################
    ''' Main code goes in here. "Line" is the text typed in to chat '''
    for line in temp:
        print(line)
        user = getUser(line)
        message = getMessage(line)
        if "PING" in line:  # Responds to PINGs from Twitch IRC, checks bot is active
            sendMessage(s, line.replace("PING", "PONG"))
            print("PONG sent")
        if "!name" in line:  # Tells user their username
            nameResponse = "Your name is: " + user
            sendMessage(s, nameResponse)
        if "!weather" in line:
            locationList = line.split("-")
            location = locationList[1]
            print(location)
            sendMessage(s, location)
            if location == "":
                errorMessage = user + ", use the command like !weather -location"
                sendMessage(s, errorMessage)
            else:
                pass


        print(user + " typed: " + message)




