#!/usr/bin/python3
"""
The requests module allows
you to send HTTP requests
using Python.
"""
import requests


def top_ten(subreddit):
    """ Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
    """
    base_url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Too Many Requests'}
    response = requests.get(base_url, headers=headers)

    tenhot_post = response.json().get("data", {}).get("children")
    if not tenhot_post:
        print(None)
    else:
        for x in tenhot_post:
            print(x.get('data').get('title'))
