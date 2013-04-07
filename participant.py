class Participant:
	def __init__(self, room):
		self.room = room
		self.room.add_participant(self)
	
	def say(self, message):
		self.room.say(message)
	
	def heard(self, message):
		print message.get_message_text() + "\n"
