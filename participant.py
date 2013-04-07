class Participant:
	def __init__(self, room):
		self.room = room
	
	def say(self, msg):
		self.room.say(msg)
	
	def heard(self, msg):
		print "%s\n" % msg.get_msg()

