# backend/app.py
import os
from flask_cors import CORS
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from backend.config_sample import UPLOAD_FOLDER, TRANSCRIPTS_FOLDER


from backend.utils import ensure_folder, save_transcript, get_db
from backend.processors.stt import transcribe_file
from backend.processors.nlp import analyze_transcript


ALLOWED_EXT = {'wav', 'mp3', 'm4a', 'mp4', 'mov', 'ogg'}

app = Flask(__name__)
CORS(app)
app.config_sample['UPLOAD_FOLDER'] = os.path.abspath(UPLOAD_FOLDER)
app.config_sample['TRANSCRIPTS_FOLDER'] = os.path.abspath(TRANSCRIPTS_FOLDER)
ensure_folder(app.config['UPLOAD_FOLDER'])
ensure_folder(app.config['TRANSCRIPTS_FOLDER'])

def allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "no file part"}), 400
    f = request.files['file']
    if f.filename == '':
        return jsonify({"error": "no filename"}), 400
    if not allowed(f.filename):
        return jsonify({"error": "file type not allowed"}), 400

    filename = secure_filename(f.filename)
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    f.save(save_path)

    # Transcribe (placeholder)
    transcript = transcribe_file(save_path)
    # Save transcript to file
    ts_filename = filename + ".txt"
    ts_path = save_transcript(ts_filename, transcript, app.config['TRANSCRIPTS_FOLDER'])

    # Analyze transcript (placeholder)
    analysis = analyze_transcript(transcript)

    result = {
        "filename": filename,
        "transcript_path": ts_path,
        "transcript": transcript,
        **analysis
    }

    # Optional: store in DB (uncomment when DB configured)
    # db = get_db()
    # db.meetings.insert_one(result)

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)