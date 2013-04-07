import sys
import Pyro4
import threading
from participant import Participant
from message import Message 

sys.excepthook=Pyro4.util.excepthook
room=Pyro4.Proxy("PYRONAME:example.room")
daemon = Pyro4.Daemon()
me=Participant(room)
uri = daemon.register(me)
room.add_participant(uri)

t = threading.Thread(target=lambda: daemon.requestLoop())
t.daemon = True
t.start()

while True:
	text = raw_input().strip()
	message = Message(text)
	me.say(message)
