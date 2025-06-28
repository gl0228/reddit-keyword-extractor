import praw
import json
import argparse
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def fetch_reddit_data(subreddits, post_limit=200, output_folder="data"):
    # Load credentials from environment variables
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    user_agent = os.getenv("REDDIT_USER_AGENT", "script:reddit_data_collector:v1.0")

    if not client_id or not client_secret:
        raise ValueError("Missing Reddit API credentials. Set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET in .env")

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )

    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        posts = [{"title": post.title} for post in subreddit.new(limit=post_limit)]

        os.makedirs(output_folder, exist_ok=True)
        with open(f"{output_folder}/{subreddit_name}.json", "w") as f:
            json.dump(posts, f, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch Reddit data.")
    parser.add_argument("subreddits", nargs="+", help="List of subreddit names.")
    args = parser.parse_args()
    fetch_reddit_data(args.subreddits)

