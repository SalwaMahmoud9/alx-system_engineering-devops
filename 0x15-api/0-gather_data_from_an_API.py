#!/usr/bin/python3
"""gather data from an API"""
import requests
import sys

if __name__ == "__main__":
    EMPLOYEE_ID = sys.argv[1]
    EMPLOYEE_NAME = requests.get(
        "https://jsonplaceholder.typicode.com/users/{:d}"
        .format(int(EMPLOYEE_ID))).json().get("name")
    DONE_TASKS = []
    TOTAL_NUMBER_OF_TASKS = 0
    r = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    for task in r:
        if (task.get("userId") == int(EMPLOYEE_ID)):
            TOTAL_NUMBER_OF_TASKS += 1
            if (task.get("completed")):
                DONE_TASKS.append(task.get("title"))

    print("Employee {:s} is done with tasks({:d}/{:d}):".format
          (EMPLOYEE_NAME, len(DONE_TASKS), TOTAL_NUMBER_OF_TASKS))

    for task in DONE_TASKS:
        print("\t {:s}".format(task))
