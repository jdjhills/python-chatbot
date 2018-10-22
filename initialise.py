from Socket import sendMessage
def joinRoom(s):
    readBuffer = ""
    Loading = True
    while Loading:
        readBuffer = readBuffer + (s.recv(1024)).decode()
        temp = readBuffer.split("\r\n")
        readBuffer = temp.pop()

        for line in temp:
            print(line)
            Loading = loadingComplete(line)
    sendMessage(s, "Successfully joined chat")

def loadingComplete(line):
    if("End of /NAMES list" in line):
        return False
    else:
        return True
