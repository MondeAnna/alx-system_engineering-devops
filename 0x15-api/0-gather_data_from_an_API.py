#!/usr/bin/python3
"""
Fetch info about an employee tasks
"""


import requests
import sys


def get_task_stats(employee_id):
    """extracts tasks related stats from employee id"""

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

    completed = [task for task in tasks if task.get("completed")]

    return {
        "completed": completed,
        "count_completed": len(completed),
        "count_total": len(tasks),
    }


def get_employee_name(employee_id):
    """extracts employee name from response"""

    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    if response.ok:
        for employee in response.json():
            if employee.get("id") == employee_id:
                return employee.get("name")

    return ""


def main(employee_id):
    """coordinates executing stitching the response with stdout"""

    name = get_employee_name(employee_id)
    stats = get_task_stats(employee_id)

    completed = stats.get("count_completed")
    total = stats.get("count_total")
    message = f"Employee {name} is done with tasks({completed}/{total}): "

    print(message)

    for task in stats.get("completed"):
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    main(employee_id)
