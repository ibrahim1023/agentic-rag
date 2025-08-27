import os
from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv()


@dataclass
class AgentConfig:
    workspace_dir: str
    model_name: str
    temperature: float


def load_config() -> AgentConfig:
    workspace_dir = os.getenv("WORKSPACE_DIR", os.getcwd())
    model_name = os.getenv("AGENT_MODEL", "gemini-2.0-flash")
    try:
        temperature = float(os.getenv("AGENT_TEMPERATURE", "0"))
    except ValueError:
        temperature = 0.0
    return AgentConfig(
        workspace_dir=workspace_dir,
        model_name=model_name,
        temperature=temperature,
    )

