# twitterSentiments.py
# Author: Santiago Lizarraga
# May 11, 2025
#
# This script processes a CSV file of tweets about Netflix shows,
# calculates a sentiment score for each tweet using NLTK's VADER sentiment analyzer,
# and outputs two CSV files:
#   - One with sentiment scores per tweet
#   - One with the average sentiment score per show

import nltk
import csv
from collections import defaultdict
from nltk.sentiment import SentimentIntensityAnalyzer

def write_per_tweet_output(data):
    filename = "tweetSentimentScores.csv"
    columnNames = ["TweetID", "Text", "Show", "SentimentScore"]

    with open(filename, 'w', newline='', encoding='utf-8') as outputFile:
        writer = csv.writer(outputFile)
        writer.writerow(columnNames)
        writer.writerows(data)

def write_per_show_summary(aggregated_scores):
    filename = "averageSentimentPerShow.csv"
    columnNames = ["Show", "AverageSentimentScore"]

    with open(filename, 'w', newline='', encoding='utf-8') as summaryFile:
        writer = csv.writer(summaryFile)
        writer.writerow(columnNames)
        for show, scores in aggregated_scores.items():
            average = sum(scores) / len(scores)
            writer.writerow([show, round(average, 4)])

def main():
    input_file = 'TweetSentimentInput.csv'
    sia = SentimentIntensityAnalyzer()
    per_tweet_output = []
    show_sentiment_map = defaultdict(list)

    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  

        for i, row in enumerate(reader, start=2):  
            if len(row) < 3:
                print(f"Skipping row {i}: {row}")
                continue  

            tweet_id, tweet_text, show_name = row[0], row[1], row[2]
            score = sia.polarity_scores(tweet_text)["compound"]
            per_tweet_output.append([tweet_id, tweet_text, show_name, score])
            show_sentiment_map[show_name].append(score)

    write_per_tweet_output(per_tweet_output)
    write_per_show_summary(show_sentiment_map)

if __name__ == "__main__":
    main()

