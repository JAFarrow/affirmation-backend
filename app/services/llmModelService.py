from openai import OpenAI, APIConnectionError, APITimeoutError, APIError
from typing import Optional
from ..errors import LLMConnectionError, LLMServiceError

client = OpenAI()

SYS_PROMPT = """
Based on the mood and optionally the details provided, generate a motivational affirmation.
"""

def callLLM(mood: str, details: Optional[str] = None) -> str:
    prompt_text = f"User Mood: {mood}"
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
        raise LLMConnectionError(str(e))

    except APIError as e:
        raise LLMServiceError(str(e))

    except Exception as e:
        raise LLMServiceError("Unknown LLM failure")
