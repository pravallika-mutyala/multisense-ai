import pyttsx3
import tempfile

engine = pyttsx3.init()

def text_to_speech(text):
    """
    Convert text to speech safely.
    """
    if not text or not text.strip():
        return None  # Prevent TTS crash

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        audio_path = f.name

    engine.save_to_file(text, audio_path)
    engine.runAndWait()

    return audio_path
