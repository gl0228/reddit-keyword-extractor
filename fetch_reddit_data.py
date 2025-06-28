import praw
import json
import argparse

def fetch_reddit_data(subreddits, post_limit=200, output_folder="data"):
    reddit = praw.Reddit(
        client_id="n1crjoV6ZJ92H_-0_1QdmQ",
        client_secret="BSlOdNlAXz-Q2ohdeWf03RWGwsSqGw",
        user_agent="script:my_reddit_fetcher:v1.0 (by u/Appropriate-Tutor791)"
    )

    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        posts = [{"title": post.title} for post in subreddit.new(limit=post_limit)]
        with open(f"week11/{output_folder}/{subreddit_name}.json", "w") as f:
            json.dump(posts, f, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch Reddit data.")
    parser.add_argument("subreddits", nargs="+", help="List of subreddit names.")
    args = parser.parse_args()
    fetch_reddit_data(args.subreddits)
