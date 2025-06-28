import json
import argparse
from sklearn.feature_extraction.text import TfidfVectorizer

def compute_tfidf(files, stop_words):
    data = []
    file_names = []
    for file in files:
        with open(file, "r") as f:
            posts = json.load(f)
            titles = " ".join(post["title"] for post in posts if "title" in post)
            data.append(titles)
            file_names.append(file)

    # Pass stop words directly as a list to the TfidfVectorizer.
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    tfidf_matrix = vectorizer.fit_transform(data)
    feature_names = vectorizer.get_feature_names_out()

    results = {}
    for i, file in enumerate(file_names):
        scores = zip(feature_names, tfidf_matrix[i].toarray().flatten())
        sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[:10]
        results[file] = [(word, score) for word, score in sorted_scores]

    return results

def load_stop_words(stop_word_file):
    if stop_word_file:
        with open(stop_word_file, "r") as f:
            # Ensure stop words are read line by line and stripped of extra spaces.
            return [line.strip() for line in f.readlines()]
    return None


if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Build a TF-IDF word list.")
    parser.add_argument("-o", "--output", required=True, help="Output file for word scores.")
    parser.add_argument("-s", "--stop_words", help="Optional stop word file.")
    parser.add_argument("files", nargs="+", help="List of input JSON files.")
    args = parser.parse_args()

    stop_words = load_stop_words(args.stop_words)
    results = compute_tfidf(args.files, stop_words)

    with open(args.output, "w") as f:
        json.dump(results, f, indent=4)

