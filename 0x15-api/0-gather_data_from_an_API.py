#!/usr/bin/python3
"""returns information about an employee's TODO list progress"""
from sys import argv
from requests import get

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = get(url + "users/{}".format(argv[1])).json()
    todos = get(url + "todos", params={"userId": argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
