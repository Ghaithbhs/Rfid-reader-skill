from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft import MycroftSkill, intent_file_handler
import json
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()



class login(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)


    @intent_handler(IntentBuilder("").require("querry"))
    def handle_login(self):


        try:
            id, text = reader.read()
            self.speak_dialog("login", data={"text": text})
        finally:
            GPIO.cleanup()


def create_skill():
    return login()
