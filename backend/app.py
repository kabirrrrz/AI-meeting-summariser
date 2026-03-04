# # app.py
# import os
# from flask_cors import CORS
# from flask import Flask, request, jsonify
# from werkzeug.utils import secure_filename

# from config_sample import UPLOAD_FOLDER, TRANSCRIPTS_FOLDER
# from utils import ensure_folder, save_transcript, get_db
# from processors.stt import transcribe_file
# from processors.nlp import analyze_transcript

# ALLOWED_EXT = {'wav', 'mp3', 'm4a', 'mp4', 'mov', 'ogg'}

# app = Flask(__name__)
# CORS(app)

# # ✅ Flask config
# app.config['UPLOAD_FOLDER'] = os.path.abspath(UPLOAD_FOLDER)
# app.config['TRANSCRIPTS_FOLDER'] = os.path.abspath(TRANSCRIPTS_FOLDER)

# # ✅ Ensure folders exist
# ensure_folder(app.config['UPLOAD_FOLDER'])
# ensure_folder(app.config['TRANSCRIPTS_FOLDER'])

# def allowed(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

# @app.route('/upload', methods=['POST'])
# def upload():
#     if 'file' not in request.files:
#         return jsonify({"error": "no file part"}), 400

#     f = request.files['file']

#     if f.filename == '':
#         return jsonify({"error": "no filename"}), 400

#     if not allowed(f.filename):
#         return jsonify({"error": "file type not allowed"}), 400

#     filename = secure_filename(f.filename)
#     save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     f.save(save_path)

#     # ✅ Speech-to-text
#     transcript = transcribe_file(save_path)

#     # ✅ Save transcript file
#     ts_filename = filename + ".txt"
#     ts_path = save_transcript(ts_filename, transcript, app.config['TRANSCRIPTS_FOLDER'])

#     # ✅ NLP analysis
#     analysis = analyze_transcript(transcript)

#     result = {
#         "filename": filename,
#         "transcript_path": ts_path,
#         "transcript": transcript,
#         **analysis
#     }

#     return jsonify(result), 200

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5000, debug=True)

# app.py
import os
from flask_cors import CORS
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

from config import UPLOAD_FOLDER, TRANSCRIPTS_FOLDER
from utils import ensure_folder, save_transcript, get_db
from processors.stt import transcribe_file
from processors.nlp import analyze_transcript

ALLOWED_EXT = {'wav', 'mp3', 'm4a', 'mp4', 'mov', 'ogg'}

app = Flask(__name__)

# ✅ FIXED CORS (allow frontend to talk to backend)
CORS(app, resources={r"/*": {"origins": "*"}})

# ✅ Flask config
app.config['UPLOAD_FOLDER'] = os.path.abspath(UPLOAD_FOLDER)
app.config['TRANSCRIPTS_FOLDER'] = os.path.abspath(TRANSCRIPTS_FOLDER)

# ✅ Ensure folders exist
ensure_folder(app.config['UPLOAD_FOLDER'])
ensure_folder(app.config['TRANSCRIPTS_FOLDER'])


def allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT


@app.route("/")
def home():
    return "AI Meeting Summariser Backend Running"
@app.route('/upload', methods=['POST'])
def upload():
    try:
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

        print("FILE SAVED:", save_path)

        # ✅ Speech-to-text
        transcript = transcribe_file(save_path)
        print("TRANSCRIPT DONE")

        # ✅ Save transcript file
        ts_filename = filename + ".txt"
        ts_path = save_transcript(
            ts_filename,
            transcript,
            app.config['TRANSCRIPTS_FOLDER']
        )

        # ✅ NLP analysis
        analysis = analyze_transcript(transcript)
        print("ANALYSIS DONE")

        result = {
            "filename": filename,
            "transcript_path": ts_path,
            "transcript": transcript,
            **analysis
        }

        return jsonify(result), 200

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)                     
