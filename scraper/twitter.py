import snscrape.modules.twitter as sntwitter
import pandas as pd

def scrape_tweets_to_csv(keyword, num_tweets, output_csv):
    # Create an empty list to store the tweets
    tweets_list = []

    # Search for tweets using snscrape and store them in the list
    for tweet in sntwitter.TwitterSearchScraper(keyword + ' since:2020-01-01 lang:en').get_items():
        if len(tweets_list) >= num_tweets:
            break
        tweets_list.append([tweet.date, tweet.content])

    # Convert the list to a DataFrame
    df = pd.DataFrame(tweets_list, columns=['Date', 'Tweet'])

    # Save the DataFrame to a CSV file
    df.to_csv(output_csv, index=False)

# Set the keyword you want to search for (e.g., 'Singapore', '#Singapore', 'Singapore weather', etc.)
keyword = 'Singapore'

# Set the number of tweets you want to scrape
num_tweets = 1000

# Set the name of the output CSV file
output_csv = 'tweets_singapore.csv'

# Call the function
scrape_tweets_to_csv(keyword, num_tweets, output_csv)