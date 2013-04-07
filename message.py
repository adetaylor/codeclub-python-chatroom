class Message:
	def __init__(self, message_text, username):
		self.message_text = message_text
		self.username = username

	def get_message_text(self):
		return self.message_text

	def get_username(self):
		return self.username
