#!/usr/bin/python3
"""2-recurse"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """recurse"""
    r = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if r.status_code != 200:
        return None
    else:
        for data in r.json().get("data").get("children"):
            title = data.get("data").get("title")
            hot_list.append(title)
        after = r.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
