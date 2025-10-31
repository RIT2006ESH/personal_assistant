import pyttsx3

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.set_voice()

    def set_voice(self):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)  # Male voice

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()