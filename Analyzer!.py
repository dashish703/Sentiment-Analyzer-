import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()


# Function to analyze sentiment
def analyze_sentiment(text):
    # Perform sentiment analysis
    sentiment_scores = sia.polarity_scores(text)

    # Determine sentiment based on compound score
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return sentiment, sentiment_scores


# Get user input for text
user_input = input("Enter text for sentiment analysis: ")

# Analyze sentiment
sentiment, scores = analyze_sentiment(user_input)

# Output results
print(f"\nSentiment: {sentiment}")
print(f"Sentiment Scores: {scores}")
