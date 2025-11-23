# backend/config.py

import os
from dotenv import load_dotenv

load_dotenv()

# Keys

GEMINI_API_KEY = "your API key here"

# Database URI (not used yet but fine)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/meeting_summarizer")

# File paths
UPLOAD_FOLDER = "uploads"

TRANSCRIPTS_FOLDER = "data/transcripts"