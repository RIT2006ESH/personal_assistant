class Conversation:
    def __init__(self, assistant_name):
        self.name = assistant_name
        self.responses = {
            "how are you": "I'm doing great, thank you! How about you?",
            "what's your name": f"I am {self.name}, your personal assistant"
        }

    def get_response(self, command):
        for key in self.responses:
            if key in command:
                return self.responses[key]
        return None