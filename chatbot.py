from Socket import openSocket
from initialise import joinRoom
s = (openSocket())
joinRoom(s)

while True:
    persist = True


