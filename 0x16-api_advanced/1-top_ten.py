#!/usr/bin/python3
"""1-top_ten"""

import requests


def top_ten(subreddit):
    """top ten"""
    if subreddit and type(subreddit) is str:
        r = requests.get(
            "https://www.reddit.com/r/{}/hot.json".format(subreddit),
            headers={"User-Agent": "Custom"},
            params={"limit": 10},
        )

        if r.status_code != 200:
            print(None)
        else:
            data = r.json()
            posts = data.get('data', {}).get('children', {})
            for post in posts:
                print(post.get('data').get('title'))
