#!/usr/bin/python3
"""0-subs"""

import requests


def number_of_subscribers(subreddit):
    """number of subscribers"""
    r = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if r.status_code != 200:
        return 0
    else:
        return r.json().get("data").get("subscribers")
