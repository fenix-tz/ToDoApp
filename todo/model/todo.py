# TODO: Add code here
# todo.py

from typing import List, Dict

class Todo:
    def __init__(self, code_id: int, title: str, description: str) -> None:
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: List[str] = []

