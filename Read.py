import string

def getUser(line):
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user



def getMessage(line):
    separate = line.split(":", 2)

    if "PING" in separate[0]:
        message = separate[0]
    else:
        message = separate[2]

    return message