# 🎙 AI Meeting Summariser  
Transform audio/video meetings into clean transcripts, summaries, keywords & action items — powered by Google Gemini AI.

## 🚀 Overview  
AI Meeting Summariser is a full-stack application that allows users to upload *audio/video files*, automatically:

✔ Converts speech → text  
✔ Generates a clean meeting *summary*  
✔ Extracts *keywords*  
✔ Detects *sentiment*  
✔ Creates *action items*  
✔ Supports *Hindi + English*  
✔ Works on any audio/video file format  

Built using *Flask backend, **Gemini AI for NLP + STT, and a **responsive web UI*.

---

## 📦 Features

### 🎧 1. Upload Audio/Video  
Supports:  
- mp3, wav, m4a, ogg  
- mp4, mov, mkv  

### 📝 2. Speech-to-Text Transcription  
Uses *Google Gemini Flash* model for accurate and fast transcription.  
Supports *Hindi, **English*, and mixed Hinglish conversations.

### 🤖 3. AI Meeting Analysis  
Gemini generates:  
- Summary  
- Action items  
- Keywords  
- Sentiment analysis  

### 🗂 4. Auto-save Transcripts  
Transcripts are saved locally inside:


data/transcripts/


### 💻 5. Clean Frontend UI  
A lightweight modern UI with:  
✔ Drag & drop upload  
✔ Progress indicator  
✔ Clean output display (not JSON)

---

## 🧠 Tech Stack

### *Frontend*
- HTML5  
- CSS3  
- JavaScript  

### *Backend*
- Python 3  
- Flask  
- Gemini API  
- Werkzeug  
- Flask-CORS  

---

## 🧱 Project Structure


AI-meeting-summariser/
│
├── backend/
│   ├── app.py
│   ├── config.sample.py        # template for config
│   ├── processors/
│   │   ├── stt.py              # speech-to-text
│   │   ├── nlp.py              # AI summary & analysis
│   │   └── transcribers.py
│   ├── requirements.txt
│   └── utils.py
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── data/
│   └── transcripts/            # auto-generated transcripts
│
├── uploads/                    # uploaded files (ignored)
│
├── .gitignore
└── README.md


---

## ⚙ Installation & Setup

### 1. Clone the repo


git clone https://github.com/kabirrrrz/AI-meeting-summariser.git
cd AI-meeting-summariser


### 2. Create a virtual environment


python -m venv .venv


### 3. Activate it

Windows:


.venv\Scripts\activate


### 4. Install dependencies


pip install -r backend/requirements.txt


### 5. Add your Gemini API key

Create:


backend/config.py


Paste:

python
GEMINI_API_KEY = "YOUR_API_KEY"
UPLOAD_FOLDER = "uploads"
TRANSCRIPTS_FOLDER = "data/transcripts"


### 6. Run backend server


python backend/app.py


### 7. Open the frontend

Open:


frontend/index.html


in your browser.

---

## 📌 API Flow

1. User uploads audio/video file  
2. Backend receives file  
3. Gemini STT transcribes  
4. Gemini NLP analyses  
5. Backend returns structured JSON  
6. UI displays summary/action items cleanly  

---

## 🧪 Sample Output


Summary:
- The meeting discussed the deadline...

Keywords:
- deadline, schedule, November

Action Items:
- Prepare draft (Kabir, due TBD)

Sentiment:
- Neutral


---

## 🔮 Future Enhancements

- Live meeting notes  
- Speaker diarization  
- Multi-language UI  
- Cloud deployment  
- DB integration (MongoDB)  

---

## 📝 License  
MIT License — free for personal & commercial use.

---

## 👤 Author  
*Kabir Sattyani*  
AI Developer | Student | Tech Enthusiast  

---

## ⭐ Contribute  
Feel free to submit issues, feature requests, or PRs!
