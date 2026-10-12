"""JSON file storage for tasks."""
from __future__ import annotations

import json
from pathlib import Path

DEFAULT_PATH = Path.home() / ".taskcli.json"


class TaskStore:
    def __init__(self, path: Path | str = DEFAULT_PATH):
        self.path = Path(path)

    def load(self) -> list[dict]:
        if not self.path.exists():
            return []
        with self.path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def save(self, tasks: list[dict]) -> None:
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2)

    def add(self, title: str) -> dict:
        tasks = self.load()
        next_id = max((t["id"] for t in tasks), default=0) + 1
        task = {"id": next_id, "title": title, "done": False}
        tasks.append(task)
        self.save(tasks)
        return task

    def complete(self, task_id: int) -> bool:
        tasks = self.load()
        for t in tasks:
            if t["id"] == task_id:
                t["done"] = True
                self.save(tasks)
                return True
        return False

    def delete(self, task_id: int) -> bool:
        tasks = self.load()
        remaining = [t for t in tasks if t["id"] != task_id]
        if len(remaining) == len(tasks):
            return False
        self.save(remaining)
        return True
