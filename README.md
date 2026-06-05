# Amazon Product Reviews Sentiment Analysis

## Project Overview
This project applies **Natural Language Processing (NLP)** techniques to analyze customer sentiment from product reviews. Using Python and the TextBlob library, we extract emotional tone from text and compare it with user ratings.

## Objective
- Clean and preprocess raw text data.
- Quantify customer sentiment as Positive, Neutral, or Negative.
- Visualize the distribution of sentiment across hundreds of reviews.
- Validate if user ratings align with the textual sentiment.

## Dataset
- **Name**: Amazon Product Reviews
- **Source**: [Kaggle - Amazon Reviews](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)
- **Format**: CSV (`amazon_reviews.csv`)

## Implementation Steps
1. **Text Preprocessing**: Lowercasing, removing special characters, and tokenization.
2. **Sentiment Scoring**: Calculating Polarity using `TextBlob`.
3. **Categorization**: Grouping reviews based on their scores.
4. **Statistical Visualization**: Plotting distributions and boxplots to see the relationship between scores and ratings.

## Key Insights
- High ratings (4 and 5 stars) strongly correlate with positive polarity scores.
- "Neutral" reviews often contain mixed feedback (e.g., "Good product but late shipping").
- Polarity histograms usually show a right-skew, indicating that Amazon customers tend to leave positive feedback or "all-or-nothing" extreme reviews.

## How to Run
1. Install requirements: `pip install pandas matplotlib seaborn textblob`
2. Download `nltk` data (optional for simple usage): `python -m textblob.download_corpora`
3. Place your dataset in `data/amazon_reviews.csv`.
4. Run: `python notebooks/sentiment_analysis.py`

## Folder Structure
```
Project_3_Sentiment_Analysis/
├── data/           # Dataset
├── notebooks/      # NLP script
├── output/         # Sentiment plots
└── README.md
```
 "Your most unhappy customers are your greatest source of learning." – Bill Gates. This tool helps you find them!
