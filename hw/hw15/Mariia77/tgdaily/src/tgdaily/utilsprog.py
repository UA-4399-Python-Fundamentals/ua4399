import json
from datetime import datetime


def load_tasks(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(filepath, tasks):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def parse_time(time_str):
    """parsing string in obj"""
    return datetime.strptime(time_str, "%Y-%m-%d %H:%M")
