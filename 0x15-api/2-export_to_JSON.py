#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format"""
import json
from requests import get
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
