from typing import List, TypedDict, Optional
from langchain_core.documents import Document


class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question
        generation: LLM generation
        web_search: whether to add search
        documents: list of documents
    """

    question: str
    documents: List[Document]
    generation: Optional[str]
    web_search: bool  # set True when doc grading says "insufficient"
