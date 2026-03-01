import whisper
import tempfile
import os

# Ensure ffmpeg is visible (Windows fix)
FFMPEG_PATH = r"C:\ffmpeg\bin"
os.environ["PATH"] = FFMPEG_PATH + os.pathsep + os.environ.get("PATH", "")

# Load Whisper model once
model = whisper.load_model("base")

def transcribe_audio(audio_file):
    """
    Transcribe audio locally using Whisper (MP3 / WAV supported).
    """

    # Get original file extension
    ext = os.path.splitext(audio_file.name)[1]

    # Reset pointer
    audio_file.seek(0)

    # Save temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        tmp.write(audio_file.read())
        temp_path = tmp.name

    # Transcribe
    result = model.transcribe(temp_path)

    # Cleanup
    os.remove(temp_path)

    return result["text"]
