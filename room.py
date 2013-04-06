class Room:
	def __init__(self):
		self.participants = []
	
	def add_participant(self, participant):
		self.participants.append(participant)
	
	def say(self, msg):
		for p in self.participants:
			p.heard(msg)
