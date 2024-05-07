#!/usr/bin/python3
"""
1-main
"""
import requests
import sys


def top_ten(subreddit):
    """This function queries the Reddit API to get the titles of the top 10"""
    url = f"https://reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "My Cool Custom User Agent"}
    try:
        response = requests.get(url, allow_redirects=False, headers=headers)
        response.raise_for_status()

        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts[:10]:  # Limit to top 10
            title = post.get("data", {}).get("title")
            if title:
                print(title)
    except (requests.exceptions.RequestException, KeyError):
        print(None)


if __name__ == "__main__":
    number_of_subscribers = __import__("1-top_ten").top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
