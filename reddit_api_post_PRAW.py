import praw
import os
from dotenv import load_dotenv
import sys

"""
Structure:
0. Imports and global variables
1. Function: Authenticate with Reddit API
2. Function: Fetch and display posts
3. Main script (calls 1st and 2nd point in order)
"""

# Load global params from dotenv file (FILL OUT BEFORE USAGE)
load_dotenv("api_credentials.env")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USER_AGENT = os.getenv("USER_AGENT")
LIMIT = os.getenv("LIMIT_POSTS", 5)  # Default limit if not set in .env
DEFAULT_SUBREDDIT = os.getenv("DEFAULT_SUBREDDIT", "python")


def authenticate():
    """
    Authenticate using PRAW to access Reddit API.
    Returns a Reddit instance.
    ->
    :param CLIENT_ID, CLIENT_SECRET, USER_AGENT from global scope
    <-
    :returns reddit_instance
    (should have access_token to access subreddit)
    """
    try:
        # Ensure required environment variables are present
        if not CLIENT_ID or not CLIENT_SECRET or not USER_AGENT:
            print("CLIENT_ID, CLIENT_SECRET, or USER_AGENT is missing in .env. "
                  "Make sure to fill out this information in api_credentials.env.")
            sys.exit(1)

        # Create Reddit instance
        reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_agent=USER_AGENT
        )
        #PRAW calls error when auth is failed
        print("Auth Success!")
        return reddit

    except Exception as e:
        print(f"An error occurred during authentication. Please check your credentials and try again. Ref: {e}")
        sys.exit(1)


def fetch_latest_posts(subreddit, reddit_instance):
    """
    Using PRAW.
    ->
    :param subreddit: Name of the subreddit to fetch posts from
    :param reddit_instance: Authenticated Reddit instance
    <-
    Display latest posts from the specified subreddit.
    Returns None (final function)
    """
    try:
        subreddit_object = reddit_instance.subreddit(subreddit)
        print(f"\nLatest {LIMIT} posts from r/{subreddit}:\n")

        for post in subreddit_object.new(limit=int(LIMIT)):
            print(f"Title: {post.title}")
            print(f"Author: {post.author}")
            print(f"Upvotes: {post.ups}\n")

    except Exception as e:
        print(f"An error occurred during fetching posts: {e}")

# Only when the file is executed as a script
if __name__ == "__main__":
    # Request subreddit name from the user
    subreddit_name = input("Enter subreddit name: ").strip()
    if not subreddit_name:
        subreddit_name = DEFAULT_SUBREDDIT
        print(f"Subreddit name is required. Defaulting to: r/{DEFAULT_SUBREDDIT}")

    # Step 1: Authenticate with Reddit API
    reddit_instance = authenticate()

    # Step 2: Fetch and display posts
    fetch_latest_posts(subreddit_name, reddit_instance)