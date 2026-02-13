from openai import OpenAI, APIConnectionError, APITimeoutError, APIError
from typing import Optional
from flask import current_app

from ..errors import LLMConnectionError, LLMServiceError

SYS_PROMPT = """
You are a supportive, empathetic AI assistant for a web app that generates personalized affirmations.

# ALIGNMENT
- Always greet the user warmly by name when provided.
- Focus on encouraging, uplifting, and validating responses based on the user's mood and details.
- Keep responses short (2-4 sentences), specific, and positive.
- Do NOT provide medical or legal advice, diagnose conditions, or give instructions for treatment.
- If the user mentions self-harm or expresses distress that could be unsafe, respond with a safe, supportive message and encourage seeking professional help (e.g., contacting a trained counselor, doctor, or crisis line).
- Tailor affirmations to the user's mood and details while maintaining safety and positivity.

# RESPONSE STRUCTURE
"(Warm greeting) (User) - (Short, positive acknowledgement of mood) \\n (2nd Person Affirmation)"
""".strip()

client = OpenAI()

def callLLM(name: str, mood: str, details: Optional[str] = None) -> str:
    prompt_text = f"User Name: {name} User Mood: {mood}"
    if details:
        prompt_text += f" Details: {details}"

    try:
        response=client.responses.create(
            model="gpt-5-mini",
            input=[
                {"role": "system", "content": SYS_PROMPT},
                {"role": "user", "content": prompt_text}
            ]
        )

        return response.output_text

    except (APIConnectionError, APITimeoutError) as e:
        current_app.logger.error(f"LLM Connection Error -> {str(e)}")
        raise LLMConnectionError(str(e))

    except APIError as e:
        current_app.logger.error(f"LLM Client Error -> {str(e)}")
        raise LLMServiceError(str(e))

    except Exception as e:
        current_app.logger.error(f"LLM Unexpected Error -> {str(e)}")
        raise LLMServiceError("Unknown LLM failure", exc_info=e)
