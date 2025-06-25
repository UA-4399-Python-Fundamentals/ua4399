import argparse

from scheduler import send_daily_summary
from utilsprog import load_tasks, save_tasks, parse_time

import json

TASKS_FILE = "tasks.json"


def add_task(description, time_str):
    tasks = load_tasks(TASKS_FILE)
    task = {
        "description": description,
        "time": time_str
    }
    tasks.append(task)
    save_tasks(TASKS_FILE, tasks)
    print(" Задача добавлена!")


def list_tasks():
    tasks = load_tasks(TASKS_FILE)
    if not tasks:
        print(" Нет задач.")
        return
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task['description']} @ {task['time']}")


def main():
    parser = argparse.ArgumentParser(description="TgDaily Task Manager")
    parser.add_argument("--add", help="Добавить задачу")
    parser.add_argument("--time", help="Время задачи в формате YYYY-MM-DD HH:MM")
    parser.add_argument("--list", action="store_true", help="Показать все задачи")
    parser.add_argument("--daily", action="store_true", help="Отправить задачи на сегодня")

    args = parser.parse_args()

    if args.add and args.time:
        add_task(args.add, args.time)
    elif args.list:
        list_tasks()
    elif args.daily:
        send_daily_summary()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
