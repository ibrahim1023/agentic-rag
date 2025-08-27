from dataclasses import dataclass
from typing import List

from .config import load_config
from .llm import call_llm
from . import tools


SYSTEM_PROMPT = (
    "You are an autonomous coding agent operating on a filesystem. "
    "You write clear, runnable code with careful edits. "
    "Respond with a short plan followed by the exact edits to apply."
)


@dataclass
class EditProposal:
    path: str
    content: str


def propose_edits(goal: str, context_files: List[str]) -> List[EditProposal]:
    file_list = "\n".join(context_files[:50])
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": (
                f"Goal:\n{goal}\n\n"
                f"Relevant files (first 50):\n{file_list}\n\n"
                "Return a minimal set of edits as blocks: \n"
                "```path:relative/path\n<full new file content>\n```"
            ),
        },
    ]
    content = call_llm(messages)

    edits: List[EditProposal] = []
    # Simple parse: look for blocks starting with ```path:
    for block in content.split("```"):
        if block.strip().startswith("path:"):
            header, *rest = block.split("\n", 1)
            path = header.split("path:", 1)[1].strip()
            body = rest[0] if rest else ""
            edits.append(EditProposal(path=path, content=body))
    return edits


def apply_edits(edits: List[EditProposal], workspace_dir: str) -> List[str]:
    applied: List[str] = []
    for e in edits:
        full_path = tools.Path(workspace_dir) / e.path
        tools.write_file(str(full_path), e.content)
        applied.append(str(full_path))
    return applied


def run_agent(goal: str) -> None:
    cfg = load_config()
    files = tools.list_files(cfg.workspace_dir)
    proposals = propose_edits(goal, files)
    if not proposals:
        print("No edits proposed.")
        return
    applied = apply_edits(proposals, cfg.workspace_dir)
    print("Applied edits:")
    for p in applied:
        print(f"- {p}")

