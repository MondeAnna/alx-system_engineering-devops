#!/usr/bin/python3
"""
Save all employee task data to csv
"""


import json
import requests


def get_all_tasks():
    """extracts all tasks"""

    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    return response.json() if response.ok else []


def get_all_user_details():
    """extracts all user details"""

    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    return [
        {"id": employee.get("id"), "username": employee.get("username")}
        for employee in response.json()
    ] if response.ok else []


def reformat_tasks(user_details, tasks):
    """reformats tasks as per user id"""

    return [
        {
            "username": user_details.get("username"),
            "task": task.get("title"),
            "completed": task.get("completed"),
        }
        for task in tasks
        if user_details.get("id") == task.get("userId")
    ]


def main():
    """coordinates intermingling user and task data and writing to json"""

    all_user_details = get_all_user_details()
    all_tasks = get_all_tasks()

    reformatted_tasks = {
        user_details.get("id"): reformat_tasks(user_details, all_tasks)
        for user_details in all_user_details
    }

    with open("todo_all_employees.json", "w") as file:
        json.dump(reformatted_tasks, file)


if __name__ == "__main__":
    main()
