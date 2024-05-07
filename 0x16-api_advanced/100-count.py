#!/usr/bin/python3
"""
100-main
"""
import requests
import sys
from collections import Counter


def split_and_lowercase(text):
    """
    Splits text into words, converting them to lowercase and
    removing punctuation at the end.
    """
    words = [word.strip().lower() for word in text.split()]
    return [
        word for word in words if not word.endswith((".", "!", "?"))
    ]  # Remove trailing punctuation


def count_words(subreddit, word_list, keywords={}, after=None):
    """
    This function recursively retrieves and counts keyword
    occurrences from hot articles.

    Args:
        subreddit: The name of the subreddit to query.
        word_list: The list of keywords to search for.
        keywords (dict, optional): Accumulates keyword
        counts across recursive calls (default: {}).
        after (str, optional): The "after" parameter for pagination
        (default: None).

    Returns:
        None: If no posts match or the subreddit is invalid.
    """
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
                for word in split_and_lowercase(title):
                    if word in word_list:
                        keywords[word] = keywords.get(word, 0) + 1

        after = data.get("data", {}).get("after")
        if after:  # Recursive call for next page if available
            count_words(subreddit, word_list, keywords, after=after)

    except (requests.exceptions.RequestException, KeyError):
        return None  # Handle request errors and missing data keys

    if keywords:  # Print results if keywords were found
        for word, count in sorted(
            keywords.items(), key=lambda item: (-item[1], item[0])
        ):
            print(f"{word}: {count}")


if __name__ == "__main__":
    number_of_subscribers = __import__("100-count").count_words
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print(
            "Ex: {} programming 'python java javascript'".format(sys.argv[0]),
        )
    else:
        count_words(sys.argv[1], sys.argv[2:])
