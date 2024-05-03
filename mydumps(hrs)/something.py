# Python program to perform sentiment analysis on Twitter data using Tweepy and TextBlob

import tweepy
from textblob import TextBlob

# Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to perform sentiment analysis
def analyze_sentiment(keyword, tweet_count):
    tweets = api.search(q=keyword, count=tweet_count)
    positive, neutral, negative = 0, 0, 0

    for tweet in tweets:
        analysis = TextBlob(tweet.text)
        if analysis.sentiment.polarity > 0:
            positive += 1
        elif analysis.sentiment.polarity == 0:
            neutral += 1
        else:
            negative += 1

    total = positive + neutral + negative
    print(f"Total tweets: {total}, Positive: {positive}, Neutral: {neutral}, Negative: {negative}")
    print(f"Positive: {(positive / total) * 100:.2f}%, Neutral: {(neutral / total) * 100:.2f}%, Negative: {(negative / total) * 100:.2f}%")

if __name__ == "__main__":
    keyword = input("Enter keyword to search: ")
    tweet_count = int(input("Enter how many tweets to analyze: "))
    analyze_sentiment(keyword, tweet_count)