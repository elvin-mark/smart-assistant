from speech_recognition import SpeechRecognition
from text_to_speech import Text2Speech
from chatbot import Chatbot
import os


class SmartAssistant:
    def __init__(self):
        self.sr = SpeechRecognition()
        self.tts = Text2Speech()
        self.chatbot = Chatbot()
    