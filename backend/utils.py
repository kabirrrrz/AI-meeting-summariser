import os
from datetime import datetime
from pymongo import MongoClient

# ✅ Folder helper
def ensure_folder(path):
    os.makedirs(path, exist_ok=True)

# ✅ Save transcript text file
def save_transcript(filename, text, folder):
    ensure_folder(folder)
    path = os.path.join(folder, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path

# ✅ MongoDB connection (OPTIONAL)
def get_db():
    """
    If MONGO_URI is not set, return None instead of crashing.
    This lets the app run even without MongoDB.
    """
    mongo_uri = os.getenv("MONGO_URI")  # ✅ take from Render env
    if not mongo_uri:
        return None

    client = MongoClient(mongo_uri)
    return client["meeting_summariser"]
