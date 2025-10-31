class VoiceAssistantError(Exception):
    pass

def handle_error(error_type, message):
    print(f"Error [{error_type}]: {message}")
    return f"Sorry, I encountered an {error_type} error: {message}"