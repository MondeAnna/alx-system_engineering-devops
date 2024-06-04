#!/usr/bin/python3
"""get titles of 10 hottest posts in subreddit"""


import requests
import sys


def top_ten(subreddit):
    """get titles of 10 hottest posts in subreddit"""

    headers = {"User-agent": "alx-system_engineering-devops-0x16-api_advanced"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 10}

    resp = requests.get(
        url,
        allow_redirects=False,
        headers=headers,
        params=params,
    )

    is_success = resp.ok
    response = resp.json()

    resp.close()

    if not is_success:
        return print("None")

    children = response.get("data").get("children")

    for child in children:
        title = child.get("data").get("title")
        print(title)


if __name__ == "__main__":
    subreddit = sys.argv[2]
    top_ten(subreddit)
