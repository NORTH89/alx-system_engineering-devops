#!/usr/bin/python3
"""
2-main
"""
import requests
import sys


def recurse(subreddit, hot_list=[]):
    """This function recursively retrieves titles of all hot
    articles for a subreddit."""
    url = f"https://reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {
        "User-Agent": "My Cool Custom User Agent"
    }  # Replace with your own user agent

    try:
        response = requests.get(url, allow_redirects=False, headers=headers)
        response.raise_for_status()

        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                hot_list.append(title)

        after = data.get("data", {}).get("after")
        if after:  # Recursive call for next page if available
            return recurse(
                subreddit,
                hot_list + recurse(subreddit, after=after),
            )
        else:
            return hot_list  # No more pages, return accumulated titles

    except (requests.exceptions.RequestException, KeyError):
        return None  # Handle request errors and missing data keys


if __name__ == "__main__":
    number_of_subscribers = __import__("2-recurse").recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
