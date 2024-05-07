#!/usr/bin/python3
"""1-top-ten"""

import requests


def top_ten(subreddit):
    """top Ten"""
    r = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if r.status_code != 200:
        print(None)
        
    else:
        for data in r.json().get("data").get("children"):
            title = data.get("data").get("title")
            print(title)
