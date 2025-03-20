import requests
import sys
from dotenv import load_dotenv
import os
# THIS is legacy variation w/o PRAW
# Load global params from dotenv file (FILL OUT BEFORE USAGE)
config = load_dotenv("api_credentials.env")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USER_AGENT = os.getenv("USER_AGENT")
LIMIT = os.getenv("LIMIT_POSTS")
DEFAULT_SUBREDDIT = os.getenv("DEFAULT_SUBREDDIT")

def authenticate():
    """
    Reddit OUATH2 (w/o pkce, fuh).
    POST -> cridentials: CLIENT_ID, CLIENT_SECRET
    <- access_token
    Returns access token.
    """
    try:
        auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
        data = {
            "grant_type": "client_credentials"
        }
        headers = {
            "User-Agent": USER_AGENT
        }

        response = requests.post("https://www.reddit.com/api/v1/access_token",
                                 auth=auth, data=data, headers=headers)

        if response.status_code == 200:
            token = response.json().get("access_token")
            print("Auth Success!")
            return token
        else:
            print(f"Auth failed! HTTP Code: {response.status_code}")
            print(f"Response: {response.json()}")
            sys.exit(1)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during authentication: {e}")
        sys.exit(1)


def fetch_latest_posts(subreddit, token):
    """
    Get last 5 posts from subreddit.

    :param subreddit: name of subreddit
    :param token: Oauth2 access token (received from authenticate())
    GET -> posts: subreddit, limit=5
    """
    try:
        headers = {
            "Authorization": f"bearer {token}",
            "User-Agent": USER_AGENT
        }

        url = f"https://oauth.reddit.com/r/{subreddit}/new"
        params = {
            "limit": LIMIT
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            posts = response.json().get("data", {}).get("children", [])
            print(f"\nLatest {LIMIT} posts from r/{subreddit}:\n")
            for post in posts:
                post_data = post["data"]
                print(f"Title: {post_data['title']}")
                print(f"Author: {post_data['author']}")
                print(f"Upvotes: {post_data['ups']}\n")
        else:
            print(f"Failed to fetch posts! Status code: {response.status_code}")
            print(f"Response: {response.json()}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during fetching posts: {e}")

# Only when the file is executed as a script
if __name__ == "__main__":
    # State subreddit name
    subreddit_name = input("Enter subreddit name: ")
    if not subreddit_name:
        subreddit_name = DEFAULT_SUBREDDIT
        print(f"Subreddit name is required. Replaced with {DEFAULT_SUBREDDIT}")
    # Fool Proof for empty values
    if not CLIENT_ID or not CLIENT_SECRET or not USER_AGENT:
        print("CLIENT_ID, CLIENT_SECRET, or USER_AGENT is missing in .env. Make sure to fill out this information in api_credentials.env.")
        sys.exit(1)

    # Step 1: Auth
    access_token = authenticate()

    # Step 2: Obtain
    fetch_latest_posts(subreddit_name, access_token)