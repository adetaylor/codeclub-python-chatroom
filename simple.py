from room import Room
from message import Message
from participant import Participant

room = Room()
janet = Participant(room)
john = Participant(room)
fred = Participant(room)

janet.say("Hello everyone!")
