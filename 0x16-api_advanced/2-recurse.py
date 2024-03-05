#!/usr/bin/python3
"""Queries the Reddit API and returns a list of titles of all hot articles
for a given subreddit"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Queries Reddit API and returns all hot posts
    of the subreddit"""
    from requests import get

    sub_info = get("https://www.reddit.com/r/{}/hot.json"
                   .format(subreddit),
                   params={"count": count, "after": after},
                   headers={"User-Agent": "My-User-Agent"},
                   allow_redirects=False)
    if sub_info.status_code >= 400:
        return None

    hot_l = hot_list + [child.get("data").get("title")
                        for child in sub_info.json()
                        .get("data")
                        .get("children")]

    info = sub_info.json()
    if not info.get("data").get("after"):
        return hot_l

    return recurse(subreddit, hot_l, info.get("data").get("count"),
                   info.get("data").get("after"))
