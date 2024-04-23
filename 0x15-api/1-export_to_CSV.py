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
    TODOs = requests.get(f"{URL}/todos").json()
    EMPLOYEE_NAME = USERS.get('username')
    # print(f"{USERS}\n{TODOS}\n{EMPLOYEE_NAME}")
    TODOS = list(filter(
        lambda x: x.get('userId') == id,
        TODOs))
    with open('{}.csv'.format(id), 'w') as file:
        for TODO in TODOS:
            file.write('"{}","{}","{}","{}"\n'.format(
                id,
                EMPLOYEE_NAME,
                TODO.get('completed'),
                TODO.get('title')))


if __name__ == "__main__":
    if len(sys.argv) > 1 and re.fullmatch(r'\d+', sys.argv[1]):
        id = int(sys.argv[1])
        GET(id)
