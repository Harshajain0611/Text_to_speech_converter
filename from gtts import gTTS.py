
from gtts import gTTS
import os
import platform
import subprocess

def text_to_speech(text, lang='en', slow=False):
    tts = gTTS(text=text, lang=lang, slow=slow)
    tts.save("output.mp3")
    
    play_audio()

def play_audio():
    system_platform = platform.system().lower()
    if system_platform == 'darwin':
        subprocess.run(['afplay', 'output.mp3'], check=True)  # macOS
    elif system_platform == 'linux':
        subprocess.run(['xdg-open', 'output.mp3'], check=True)  # Linux
    elif system_platform == 'windows':
        subprocess.run(['start', 'output.mp3'], check=True)  # Windows
    else:
        print("Unsupported operating system")

if __name__ == "__main__":
    user_text = input("Enter the text you want to convert to speech: ")
    text_to_speech(user_text)
