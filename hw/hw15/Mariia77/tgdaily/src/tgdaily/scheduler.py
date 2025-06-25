from datetime import datetime

from utilsprog import load_tasks, parse_time
from notifier import send_message

TASKS_FILE = "tasks.json"


def format_task(task):
    return f"🗓 {task['description']} @ {task['time']}"


def send_daily_summary():
    tasks = load_tasks(TASKS_FILE)
    today = datetime.now().date()

    for task in tasks:
        task_time = parse_time(task["time"])
        if task_time.date() == today:
            send_message(f"📌 Задача на сегодня: {format_task(task)}")


if __name__ == "__main__":
    send_daily_summary()
