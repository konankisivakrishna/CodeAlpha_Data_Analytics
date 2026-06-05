import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import re

# Set style
sns.set(style="whitegrid")

def clean_text(text):
    """Simple text cleaning function."""
    if isinstance(text, str):
        text = text.lower() # Lowercase
        text = re.sub(r'[^a-zA-Z\s]', '', text) # Remove special characters
        return text
    return ""

def get_sentiment(text):
    """Calculate sentiment polarity using TextBlob."""
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def categorize_sentiment(score):
    """Categorize score into Positive, Neutral, Negative."""
    if score > 0:
        return 'Positive'
    elif score < 0:
        return 'Negative'
    else:
        return 'Neutral'

def analyze_reviews(df, text_column):
    """Main analysis and visualization function."""
    print("Cleaning text and calculating sentiment...")
    df['cleaned_review'] = df[text_column].apply(clean_text)
    df['sentiment_score'] = df['cleaned_review'].apply(get_sentiment)
    df['sentiment_category'] = df['sentiment_score'].apply(categorize_sentiment)
    
    # 1. Sentiment Distribution Plot
    plt.figure(figsize=(8, 6))
    sns.countplot(x='sentiment_category', data=df, palette='pastel', order=['Positive', 'Neutral', 'Negative'])
    plt.title('Sentiment Distribution of Reviews')
    plt.savefig('../output/sentiment_distribution.png')
    plt.close()

    # 2. Sentiment Score Histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(df['sentiment_score'], bins=30, kde=True, color='purple')
    plt.title('Distribution of Sentiment Polarity Scores')
    plt.xlabel('Polarity Score (-1 to 1)')
    plt.savefig('../output/polarity_histogram.png')
    plt.close()

    # 3. Correlation between Ratings and Sentiment (if ratings exist)
    if 'rating' in df.columns:
        plt.figure(figsize=(8, 6))
        sns.boxplot(x='rating', y='sentiment_score', data=df, palette='coolwarm')
        plt.title('Sentiment Score vs User Rating')
        plt.savefig('../output/rating_vs_sentiment.png')
        plt.close()

    print("Analysis complete. Visualizations saved in 'output/' folder.")
    return df

if __name__ == "__main__":
    # Recommended Dataset: Amazon Fine Food Reviews or Amazon Product Reviews
    # Link: https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews
    FILE_PATH = '../data/amazon_reviews.csv'
    
    import os
    if not os.path.exists(FILE_PATH):
        print(f"Dataset not found at {FILE_PATH}. Using dummy data for demonstration...")
        data = {
            'review_text': [
                "I love this product, it works perfectly!",
                "Great quality and fast shipping.",
                "Absolutely terrible experience. It broke within a week.",
                "It's okay, nothing special but does the job.",
                "Worst purchase ever. Do not buy!",
                "Excellent value for money.",
                "The product arrived late and the box was damaged.",
                "Very happy with the overall performance."
            ],
            'rating': [5, 5, 1, 3, 1, 4, 2, 5]
        }
        df_dummy = pd.DataFrame(data)
        analyze_reviews(df_dummy, 'review_text')
    else:
        try:
            df = pd.read_csv(FILE_PATH)
            # Assuming 'review_text' is the column name
            analyze_reviews(df, 'review_text')
        except Exception as e:
            print(f"Error: {e}")
