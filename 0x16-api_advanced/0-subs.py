#!/usr/bin/python3
"""
0-main
"""
import requests
import sys

def number_of_subscribers(subreddit):
  """
  This function queries the Reddit API to get the subscriber count for a subreddit.

  Args:
      subreddit: The name of the subreddit to query.

  Returns:
      The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
  """
  url = f"https://reddit.com/r/{subreddit}/about.json?limit=0"
  headers = {"User-Agent": "My Cool Custom User Agent"}  # Replace with your own user agent

  try:
    response = requests.get(url, allow_redirects=False, headers=headers)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    data = response.json()
    return data.get("data", {}).get("subscribers", 0)
  except (requests.exceptions.RequestException, KeyError):
    return 0  # Handle request errors and missing data keys

if __name__ == '__main__':
  number_of_subscribers = __import__('0-subs').number_of_subscribers
  if len(sys.argv) < 2:
    print("Please pass an argument for the subreddit to search.")
  else:
    print("{:d}".format(number_of_subscribers(sys.argv[1])))
