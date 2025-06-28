import json
import re
import argparse
from collections import Counter

def clean_text(text):
    return re.sub(r'[^\w\s]', '', text).lower()

def compute_word_counts(files):
    results = {}
    for file in files:
        with open(file, "r") as f:
            data = json.load(f)
        words = Counter()
        for post in data:
            words.update(clean_text(post["title"]).split())
        results[file] = words.most_common(10)
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build a naive frequent word list.")
    parser.add_argument("-o", "--output", required=True, help="Output file for word counts.")
    parser.add_argument("files", nargs="+", help="List of input JSON files.")
    args = parser.parse_args()

    results = compute_word_counts(args.files)
    with open(args.output, "w") as f:
        json.dump(results, f, indent=4)
