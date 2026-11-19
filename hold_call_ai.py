"""The two small judgments a hold call needs from Gemini: which menu digit, and is this a live person or a recording.
Each falls back to simple rules when Gemini can't be reached, and never guesses a person: when unsure, keep holding."""

import logging
import re

import config
import scanner
from google.genai import types

log = logging.getLogger(__name__)
RECORDING_WORDS = ("your call is important", "please hold", "all of our representatives", "next available", "estimated wait",
                   "stay on the line", "thank you for calling", "press ", "for billing", "para espa", "this call may be recorded")
MENU_WORDS = ("press", "say ", "for ", "option")


def _ask(prompt: str) -> str:
    client = scanner._get_client()
    response = client.models.generate_content(model=config.GEMINI_MODEL, contents=[prompt],
                                              config=types.GenerateContentConfig(temperature=0, max_output_tokens=10))
    return (response.text or "").strip()


def classify_menu(text: str) -> str:
    """One digit for patient billing or account questions, or WAIT when this is not a menu or has no billing option."""
    if not any(word in text.lower() for word in MENU_WORDS):
        return "WAIT"
    try:
        answer = _ask("This is a hospital phone menu prompt. Pick the digit for patient billing or account questions. "
                      f"Reply with one digit or WAIT.\n\nPrompt: {text}")
    except Exception as exc:
        log.warning("Menu classification failed: %s", exc)
        return "WAIT"
    return answer if re.fullmatch(r"[0-9*#]", answer) else "WAIT"


def classify_person(text: str) -> bool:
    """True only for a live person starting a conversation ("this is Maria, how can I help"), never for a recording."""
    lowered = text.lower()
    if len(text.split()) < 3 or any(word in lowered for word in RECORDING_WORDS):
        return False
    try:
        answer = _ask("Is this a live person starting a conversation (for example 'this is Maria, how can I help'), "
                      f"or a recording (for example 'your call is important to us')? Reply PERSON or RECORDING.\n\nText: {text}")
    except Exception as exc:
        log.warning("Person classification failed: %s", exc)
        return False
    return answer.upper().startswith("PERSON")
