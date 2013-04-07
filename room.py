import Pyro4

class Room:
	def __init__(self):
		self.participants = []

	def add_participant(self, participant):
		self.participants.append(Pyro4.Proxy(participant))

	def say(self, message_text):
		for p in self.participants:
			p.heard(message_text)

room = Room()

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(room)
ns.register("example.room", uri)
print "Chat room available and ready for connections!\n"
daemon.requestLoop()
