#!/usr/bin/python3
"""queries Reddit API for number of subscribers on given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """returns the total number of subscribers on a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "ubuntu:0x16.api.advanced:v1.0.0 (by thapelocodes)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
