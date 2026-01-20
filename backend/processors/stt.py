# backend/processors/stt.py

import google.generativeai as genai
from config_sample import GEMINI_API_KEY


genai.configure(api_key=GEMINI_API_KEY)

def transcribe_file(file_path):
    """
    Transcribes audio using Gemini multimodal (universal) model.
    This works on ALL accounts without needing 'native audio' support.
    """

    model = genai.GenerativeModel("models/gemini-2.5-flash")

    # Read the audio file in bytes
    with open(file_path, "rb") as f:
        audio_bytes = f.read()

    # Detect mime type
    ext = file_path.split(".")[-1].lower()
    mime = "audio/mp3" if ext in ("mp3",) else f"audio/{ext}"

    response = model.generate_content(
        [
            { "mime_type": mime, "data": audio_bytes },
            "Transcribe this audio into clean English text. If there is noise, ignore it."
        ]
    )

    return response.text.strip()