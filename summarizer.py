import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(transcript, summary_type):
    style_prompt = {
        "Executive Summary": "Write a concise executive summary highlighting key decisions and action items.",
        "Detailed Notes": "Write detailed meeting minutes covering attendees, discussion points, decisions made, and actions.",
        "Bullet Points Only": "Summarize the meeting in bullet points including key items, decisions and follow-ups."
    }

    prompt = f"""
You are an assistant that writes professional meeting minutes.
{style_prompt[summary_type]}

Here is the transcript:
\"\"\"{transcript}\"\"\"
"""

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=1000
    )

    return response['choices'][0]['message']['content']
