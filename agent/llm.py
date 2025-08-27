from typing import Any, Dict, List
from tenacity import retry, stop_after_attempt, wait_exponential_jitter
from langchain_google_genai import ChatGoogleGenerativeAI

from .config import load_config


_config = load_config()


def _make_llm():
    return ChatGoogleGenerativeAI(
        model=_config.model_name,
        temperature=_config.temperature,
    )


llm = _make_llm()


@retry(stop=stop_after_attempt(3), wait=wait_exponential_jitter(initial=1, max=6))
def call_llm(messages: List[Dict[str, str]]) -> str:
    response = llm.invoke(messages)
    if isinstance(response, str):
        return response
    try:
        # LangChain ChatMessage
        return response.content
    except Exception:
        return str(response)

