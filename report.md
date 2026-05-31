# Project Report: Customer Sentiment & Satisfaction Analysis

## 1. Introduction
Sentiment analysis is a critical tool for businesses to understand the "voice of the customer." This report summarizes the NLP-driven analysis of Amazon product reviews to gauge sentiment trends.

## 2. Methodology
- **Library**: `TextBlob` for rule-based sentiment analysis.
- **Metric**: Polarity Score (ranging from -1.0 to 1.0).
- **Process**: Data Cleaning -> Sentiment Scoring -> Labeling -> Visualization.

## 3. Results & Discussion
### 3.1 Sentiment Volume
The majority of reviewed products exhibit a positive sentiment, suggesting high satisfaction levels within the sampled dataset.

### 3.2 Score to Rating Alignment
A clear trend was observed where reviews with scores > 0.5 were almost exclusively 5-star ratings. However, 1-star ratings occasionally had neutral scores due to "sarcastic" or "curt" feedback, highlighting the limitations of simple rule-based NLP.

### 3.3 Text Distribution
The polarity histogram shows a peak at 0.0 (neutral) and another at 0.7-0.8 (highly positive), common in e-commerce datasets.

## 4. Conclusion
Automated sentiment analysis provides a fast and scalable way to monitor brand reputation. For future improvements, moving towards Deep Learning models (like BERT) could better handle nuance and sarcasm in customer feedback.

---
*Internship: CodeAlpha Data Analytics*
*Project: Task 3 - Sentiment Analysis*
