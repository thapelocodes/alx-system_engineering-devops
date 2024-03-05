#!/usr/bin/python3
"""queries reddit API for the first 10 host posts on a subreddit"""
import requests


def top_ten(subreddit):
    """prints the titles of the 10 hottest posts on a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0\
        Safari/537.36"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
