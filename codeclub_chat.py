import sys
import Pyro4
import select
import threading
from participant import Participant
from message import Message 

sys.excepthook=Pyro4.util.excepthook
room=Pyro4.Proxy("PYRONAME:example.room")
room._pyroOneway.add("say")
daemon = Pyro4.Daemon()
me=Participant(room)
uri = daemon.register(me)
room.add_participant(uri)

def run_daemon():
	daemon.requestLoop()

t = threading.Thread(target=run_daemon)
t.daemon = True
t.start()

while True:
	text = raw_input("Enter your message: ").strip()
	message = Message(text)
	me.say(message)
