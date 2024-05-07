#!/usr/bin/python3
""" Script to get the first 10 hot
    posts on Reddit
"""

import requests


def top_ten(subreddit):
    """get first 10 hot post for a subreddit"""
    if subreddit and type(subreddit) is str:
        
        r = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10}, allow_redirects=False,
        )

        if r.status_code == 200:
            data = r.json()
            posts = data.get('data', {}).get('children', {})
            for post in posts:
                print(post.get('data').get('title'))
        else:
            print(None)
