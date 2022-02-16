#!/usr/bin/python3
"""
The requests module allows
you to send HTTP requests
using Python.
"""
import requests


def number_of_subscribers(subreddit):
    """ Write a function that queries the Reddit API
    and returns the number of subscribers (not active users,
    total subscribers) for a given subreddit. If an invalid 
    subreddit is given, the function should return 0.
    """
    base_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Too Many Requests'}
    response = requests.get(base_url, headers=headers)

    numbersubs = response.json().get("data", {}).get("subscribers")
    if not numbersubs:
        return 0
    else:
        return numbersubs
