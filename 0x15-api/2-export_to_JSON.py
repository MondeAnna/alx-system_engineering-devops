#!/usr/bin/python3
"""
Save employee task data to csv
"""


import json
import requests
import sys


def get_tasks(employee_id):
    """extracts all tasks from employee id"""

    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)

    if not response.ok:
        return {
            "completed": [],
            "count_completed": 0,
            "count_total": 0,
        }

    tasks = []

    for task in response.json():
        if task.get("userId") == employee_id:
            task.pop("userId")
            task.pop("id")
            tasks.append(task)

    return tasks


def get_employee_username(employee_id):
    """extracts employee username from response"""

    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    if response.ok:
        for employee in response.json():
            if employee.get("id") == employee_id:
                return employee.get("username")

    return ""


def main(employee_id):
    """coordinates executing stitching the response with stdout"""

    username = get_employee_username(employee_id)
    tasks = get_tasks(employee_id)
    reformatted_tasks = []

    for task in tasks:
        reformatted_tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username,
        })

    with open(f"{employee_id}.json", "w") as file:
        json.dump({employee_id: reformatted_tasks}, file)


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    main(employee_id)
