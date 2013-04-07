from room import Room
from message import Message
from participant import Participant

room = Room()
janet = Participant(room)
room.add_participant(janet)
john = Participant(room)
room.add_participant(john)
fred = Participant(room)
room.add_participant(fred)

first_message = Message("Hello everyone!")

janet.say(first_message)
