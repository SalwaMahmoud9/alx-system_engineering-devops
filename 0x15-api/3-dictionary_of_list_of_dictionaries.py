#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    users = response.json()

    dic = {}
    for u in users:
        userId = u.get('id')
        username = u.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(userId)
        url += '/todos/'
        response = requests.get(url)
        tasks = response.json()
        dic[userId] = []
        for t in tasks:
            dic[userId].append({
                "task": t.get('title'),
                "completed": t.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as f:
        json.dump(dic, f)
