#!/usr/bin/python3
"""export to json"""

import json
import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + str(employeeId)

    username = requests.get(url).json().get('username')

    url += "/todos"
    tasks = requests.get(url).json()

    dic = {str(employeeId): []}
    for t in tasks:
        dic[str(employeeId)].append({
            "task": t.get('title'),
            "completed": t.get('completed'),
            "username": username
        })
    with open('{}.json'.format(str(employeeId)), 'w') as f:
        json.dump(dic, f)
