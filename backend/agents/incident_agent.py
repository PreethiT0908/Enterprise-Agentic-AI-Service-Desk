import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_incident(user_issue: str):
    """
    Agent 1 - Incident Understanding Agent

    Responsibilities:
    - Understand user issue
    - Detect category
    - Detect device
    - Detect urgency
    - Generate summary
    """

    prompt = f"""
You are an Enterprise IT Service Desk Incident Classification Agent.

Analyze the user's issue and return ONLY valid JSON.

Required JSON format:

{{
    "category": "",
    "device": "",
    "urgency": "",
    "summary": ""
}}

Rules:
- category examples:
  VPN, Password, Email, Printer, WiFi, Software, Hardware, Server, Database, Cloud, Security

- device examples:
  Laptop, Desktop, Mobile, VPN Client, Email Client, Printer, Server

- urgency values:
  Low
  Medium
  High
  Critical

- summary should be one short sentence.

User Issue:
{user_issue}

Return ONLY JSON.
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        result = response.choices[0].message.content.strip()

        # Try converting to Python dictionary
        try:
            return json.loads(result)
        except Exception:
            return {
                "category": "Unknown",
                "device": "Unknown",
                "urgency": "Medium",
                "summary": result
            }

    except Exception as e:
        return {
            "error": str(e)
        }