#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
from requests import get
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
