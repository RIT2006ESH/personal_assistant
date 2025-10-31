import speech_recognition as sr

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = self.recognizer.listen(source)
        return audio

    def recognize(self, audio):
        try:
            command = self.recognizer.recognize_google(audio, language='en-us')
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            return "none"
        except sr.RequestError:
            return "error"