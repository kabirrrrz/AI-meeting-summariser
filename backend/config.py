# # backend/config.py

# import os
# from dotenv import load_dotenv

# load_dotenv()

# # Keys
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
# # GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# # Database URI (not used yet but fine)
# MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/meeting_summarizer")

# # File paths
# UPLOAD_FOLDER = os.getenv(
#     "UPLOAD_FOLDER",
#     os.path.join(os.path.dirname(__file__), "../data/uploads")
# )

# TRANSCRIPTS_FOLDER = os.getenv(
#     "TRANSCRIPTS_FOLDER",
#     os.path.join(os.path.dirname(__file__), "../data/transcripts")
# )

import os
from dotenv import load_dotenv

load_dotenv()

# Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Database
MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb://localhost:27017/meeting_summarizer"
)

# File paths
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")

TRANSCRIPTS_FOLDER = os.getenv("TRANSCRIPTS_FOLDER", "data/transcripts")