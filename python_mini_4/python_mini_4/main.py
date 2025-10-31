import sys
from core.speech_recognition import SpeechRecognizer
from core.text_to_speech import TextToSpeech
from core.config import Config
from features.time_manager import TimeManager
from features.web_operations import WebOperations
from features.file_operations import FileOperations
from features.conversation import Conversation

class VoiceAssistant:
    def __init__(self):
        self.speech = SpeechRecognizer()
        self.voice = TextToSpeech()
        self.time = TimeManager()
        self.web = WebOperations()
        self.files = FileOperations()
        self.chat = Conversation(Config.ASSISTANT_NAME)

    def start(self):
        greeting = f"{self.time.get_greeting()}! I am {Config.ASSISTANT_NAME}"
        self.voice.speak(greeting)
        
        while True:
            audio = self.speech.listen()
            command = self.speech.recognize(audio)
            
            if command == "none":
                self.voice.speak("I didn't understand that")
                continue
            if command == "error":
                self.voice.speak("Speech service is unavailable")
                continue
                
            self.process_command(command)

    def process_command(self, command):
        if "exit" in command or "bye" in command:
            self.voice.speak("Goodbye")
            sys.exit()
            
        elif "time" in command:
            time = self.time.get_current_time()
            self.voice.speak(f"The current time is {time}")
            
        elif "open" in command:
            for site in ["google", "youtube"]:
                if site in command:
                    self.web.open_website(site)
                    self.voice.speak(f"Opening {site}")
                    break
                    
        elif "search for" in command:
            query = command.replace("search for", "").strip()
            self.web.search_web(query)
            self.voice.speak(f"Searching for {query}")
            
        elif "create file" in command:
            if self.files.create_file():
                self.voice.speak("File created successfully")
            else:
                self.voice.speak("Failed to create file")
                
        else:
            response = self.chat.get_response(command)
            self.voice.speak(response or "I don't understand that command")

if __name__ == "__main__":
    assistant = VoiceAssistant()
    try:
        assistant.start()
    except KeyboardInterrupt:
        assistant.voice.speak("Shutting down")