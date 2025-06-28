# Reddit Keyword Extractor

A simple NLP pipeline that extracts the most frequent and most meaningful words from Reddit post titles across multiple subreddits using:

- Naive word frequency
- TF-IDF (term frequency–inverse document frequency)

This project demonstrates API usage, data preprocessing, basic NLP, and TF-IDF scoring with Python.

## What It Does

1. **Fetches Reddit post titles** from specified subreddits using the Reddit API (`praw`)
2. **Cleans and tokenizes text**
3. **Builds two word lists**:
   - Most frequent words (naive count)
   - Top-scoring TF-IDF keywords


