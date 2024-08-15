#!/usr/bin/python3
"""
    function Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"user-agent": "request"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get("data")
    subscribers = data.get("subscribers")

    return subscribers
