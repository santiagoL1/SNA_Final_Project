# Netflix vs. Twitter: Social Network Analytics Project

Final group project for Social Network Analytics at Creighton University.

We analyzed how the Top 10 Netflix shows compared to user interactions on X (formerly Twitter). Using scraped data from both platforms, we examined engagement patterns and sentiment to understand how social media conversations reflect (or differ from) platform popularity.

## Features

- Scraped JSON data for Netflix’s Top 10 and related tweets
- Sentiment analysis using NLTK’s VADER
- Engagement comparison graphs included as PNG screenshots

## Files

- `/JSON Data Top10 Shows`: JSON files with collected data
- `/NetflixGraph`: Netflix data files, screenshot, and .py file that creates visualization of data
- `/TwitterSentiments`: Script to calculate sentiment scores for tweets, one input file, and two output files

## Tools Used

- Python (NLTK, pandas, matplotlib)
- VADER Sentiment Analyzer
- Apify for data scraping

## How to Run

Install dependencies:

pip install nltk pandas matplotlib

Run sentiment analysis:

python sentiment_analysis.py

## Author

Santiago Lizarraga  
Creighton University, Spring 2025  
