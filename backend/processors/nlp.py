import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

ANALYSIS_PROMPT = """
You are an AI meeting assistant. Read the meeting transcript and generate the following:

1. A concise summary (5–7 sentences).
2. A list of action items in this JSON format:
   [
      {
        "task": "...",
        "assignee": "Name or 'TBD'",
        "due": "Date or 'TBD'",
        "priority": "low/medium/high"
      }
   ]
3. A list of 5 important keywords.
4. Sentiment of the meeting (positive/neutral/negative) with a reason.

Return STRICT JSON with keys:
"summary", "action_items", "keywords", "sentiment"
"""

def analyze_transcript(transcript):
    user_prompt = ANALYSIS_PROMPT + "\n\nTranscript:\n" + transcript

    # Correct stable model
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    
    response = model.generate_content(user_prompt)
    raw_text = response.text

    # Extract JSON safely
    import json, re
    try:
        json_match = re.search(r"\{[\s\S]*\}", raw_text)
        if json_match:
            return json.loads(json_match.group())
    except Exception:
        pass

    return {"raw_response": raw_text}