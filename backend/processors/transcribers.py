import google.generativeai as genai
from config_sample import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def transcribe_audio(file_path):
    # Gemini model that supports audio
    model = genai.GenerativeModel("models/gemini-2.5-flash-native-audio-latest")

    with open(file_path, "rb") as f:
        audio_data = f.read()

    # Send audio to Gemini
    response = model.generate_content(
        [
            {"mime_type": "audio/mp3", "data": audio_data},
            "Transcribe this audio into clear English text."
        ]
    )

    transcript = response.text.strip()
    return transcript