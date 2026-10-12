"""Command-line interface."""
from __future__ import annotations

import argparse

from taskcli import __version__
from taskcli.storage import TaskStore


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="taskcli", description="Simple task tracker")
    parser.add_argument("--version", action="version", version=__version__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Add a task")
    p_add.add_argument("title", help="Task title")

    sub.add_parser("list", help="List tasks")

    p_done = sub.add_parser("done", help="Mark a task as done")
    p_done.add_argument("id", type=int)

    p_del = sub.add_parser("delete", help="Delete a task")
    p_del.add_argument("id", type=int)

    return parser


def main(argv: list[str] | None = None, store: TaskStore | None = None) -> int:
    args = build_parser().parse_args(argv)
    store = store or TaskStore()

    if args.command == "add":
        task = store.add(args.title)
        print(f"Added #{task['id']}: {task['title']}")
    elif args.command == "list":
        tasks = store.load()
        if not tasks:
            print("No tasks yet.")
        for t in tasks:
            mark = "x" if t["done"] else " "
            print(f"[{mark}] {t['id']}. {t['title']}")
    elif args.command == "done":
        print("Done." if store.complete(args.id) else "Task not found.")
    elif args.command == "delete":
        print("Deleted." if store.delete(args.id) else "Task not found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
