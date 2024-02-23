#!/usr/bin/python3
"""
Queries Reddit API and returns the number of total subscribers
for a givensubreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries Reddit API and returns the number of total subscribers for
    a given subreddit.
    """
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Python/1.0(Holberton School 0x16 task 0)'}
    response = requests.get(url, headers=headers)
    if (not response.ok):
        return 0
    subscriber_count = response.json().get('data').get('subscribers')
    return subscriber_count
