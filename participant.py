import sys
import Pyro4
import threading
from message import Message

username = raw_input("What's your username?")

class Participant:
	def __init__(self, room):
		self.room = room
	
	def say(self, message):
		self.room.say(message)
	
	def heard(self, message):
	  if not message.get_username() == username:
			print message.get_username() + ": " + message.get_message_text() + "\n"

sys.excepthook=Pyro4.util.excepthook
room=Pyro4.Proxy("PYRONAME:example.room")
daemon = Pyro4.Daemon(host=Pyro4.socketutil.getInterfaceAddress("www.google.com"))
me=Participant(room)
uri = daemon.register(me)
room.add_participant(uri)

t = threading.Thread(target=lambda: daemon.requestLoop())
t.daemon = True
t.start()

while True:
	text = raw_input().strip()
	message = Message(text, username)
	me.say(message)
