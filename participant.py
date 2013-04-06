class Participant:
	def __init__(self, room):
		self.room = room
		self.room.add_participant(self)
	
	def say(self, msg):
		self.room.say(msg)
	
	def heard(self, msg):
		print msg + "\n"
