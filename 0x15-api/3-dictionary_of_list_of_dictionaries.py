#!/usr/bin/python3
"""dictionary of list of dictionaries"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    users = requests.get(url).json()

    dic = {}
    for u in users:
        userId = u.get('id')
        username = u.get('username')
        url2 = 'https://jsonplaceholder.typicode.com/users/{}'.format(userId)
        tasks = requests.get(url2+'/todos/').json()
        dic[userId] = []
        for t in tasks:
            dic[userId].append({
                "task": t.get('title'),
                "completed": t.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as f:
        json.dump(dic, f)
