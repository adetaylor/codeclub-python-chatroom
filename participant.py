class Participant:
	def __init__(self, room):
		self.room = room
	
	def say(self, message):
		self.room.say(message)
	
	def heard(self, message):
		print message.get_message_text() + "\n"
