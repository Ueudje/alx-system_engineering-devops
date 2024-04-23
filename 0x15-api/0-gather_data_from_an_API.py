#!/usr/bin/python3
"""import module
"""
import re
import requests
import sys


def GET(id):
    """GET : is function that get requests and print with right format"""
    URL = f'https://jsonplaceholder.typicode.com'
    USERS = requests.get(f"{URL}/users/{id}").json()
    TODOS = requests.get(f"{URL}/todos").json()
    EMPLOYEE_NAME = USERS.get('name')
    TOTAL_NUMBER_OF_TASKS = list(filter(
        lambda x: x.get('userId') == id,
        TODOS))
    NUMBER_OF_DONE_TASKS = list(filter(
        lambda x: x.get('completed'),
        TOTAL_NUMBER_OF_TASKS))
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, len(NUMBER_OF_DONE_TASKS),
        len(TOTAL_NUMBER_OF_TASKS)))
    for TASK_TITLE in NUMBER_OF_DONE_TASKS:
        print("\t {}".format(TASK_TITLE.get('title')))


if __name__ == "__main__":
    if len(sys.argv) > 1 and re.fullmatch(r'\d+', sys.argv[1]):
        id = int(sys.argv[1])
        GET(id)
