import Pyro4

class Room:
	def __init__(self):
		self.participants = []

	def add_participant(self, participant):
		self.participants.append(Pyro4.Proxy(participant))

	def say(self, msg):
		for p in self.participants:
			p.heard(msg)

room = Room()
Pyro4.Daemon.serveSimple(
  {
    room: "example.room"
  },
  ns=True)
