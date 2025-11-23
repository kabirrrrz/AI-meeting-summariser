# backend/utils.py
import os
from datetime import datetime
from pymongo import MongoClient
from config import MONGO_URI

def ensure_folder(path):
    os.makedirs(path, exist_ok=True)

def save_transcript(filename, text, folder):
    ensure_folder(folder)
    path = os.path.join(folder, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path

def get_db():
    client = MongoClient(MONGO_URI)
    # default DB from URI; fallback to meeting_summarizer
    db = client.get_database()
    return db