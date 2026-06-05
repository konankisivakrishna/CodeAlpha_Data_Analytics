import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for visualizations
sns.set(style="whitegrid")

def load_data(file_path):
    """Load the Netflix dataset."""
    try:
        df = pd.read_csv(file_path)
        print("Dataset loaded successfully!")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    """Perform data cleaning."""
    print("\n--- Data Cleaning ---")
    
    # 1. Handle missing values
    print("Missing values before cleaning:\n", df.isnull().sum())
    
    # Filling missing 'country' with 'Unknown'
    df['country'] = df['country'].fillna('Unknown')
    # Filling missing 'director' and 'cast'
    df['director'] = df['director'].fillna('No Director')
    df['cast'] = df['cast'].fillna('No Cast')
    
    # Dropping rows with missing 'date_added' or 'rating' as they are few
    df.dropna(subset=['date_added', 'rating', 'duration'], inplace=True)
    
    # 2. Format 'date_added'
    df['date_added'] = df['date_added'].str.strip()
    df['date_added'] = pd.to_datetime(df['date_added'])
    df['year_added'] = df['date_added'].dt.year
    df['month_added'] = df['date_added'].dt.month_name()
    
    print("Data cleaning complete.")
    return df

def exploratory_analysis(df):
    """Analyze and Visualize the data."""
    print("\n--- Exploratory Analysis ---")
    
    # 1. Content Type Distribution (Movies vs TV Shows)
    plt.figure(figsize=(8, 6))
    sns.countplot(x='type', data=df, palette='viridis')
    plt.title('Distribution of Netflix Content Types')
    plt.savefig('../output/content_distribution.png')
    plt.close()
    
    # 2. Content Added Over Time
    content_by_year = df.groupby('year_added')['show_id'].count().reset_index()
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='year_added', y='show_id', data=content_by_year, marker='o', color='red')
    plt.title('Content Added to Netflix Over Years')
    plt.ylabel('Count')
    plt.xlabel('Year')
    plt.savefig('../output/content_growth.png')
    plt.close()

    # 3. Top 10 Genres
    df['genre'] = df['listed_in'].apply(lambda x: x.split(',')[0])
    top_genres = df['genre'].value_counts().head(10)
    plt.figure(figsize=(10, 8))
    sns.barplot(y=top_genres.index, x=top_genres.values, palette='magma')
    plt.title('Top 10 Genres on Netflix')
    plt.savefig('../output/top_genres.png')
    plt.close()

    # 4. Top 10 Countries with Content
    top_countries = df['country'].value_counts().head(10)
    plt.figure(figsize=(10, 8))
    sns.barplot(y=top_countries.index, x=top_countries.values, palette='coolwarm')
    plt.title('Top 10 Countries Producing Netflix Content')
    plt.savefig('../output/top_countries.png')
    plt.close()

    print("Visualizations saved in 'output/' folder.")

if __name__ == "__main__":
    # Path to dataset (Recommended: download netflix_titles.csv from Kaggle)
    # URL: https://www.kaggle.com/datasets/shivamb/netflix-shows
    FILE_PATH = '../data/netflix_titles.csv'
    
    # For demonstration, if file doesn't exist, we alert the user
    import os
    if not os.path.exists(FILE_PATH):
        print(f"Dataset not found at {FILE_PATH}. Please place 'netflix_titles.csv' in the 'data/' folder.")
    else:
        netflix_df = load_data(FILE_PATH)
        if netflix_df is not None:
            cleaned_df = clean_data(netflix_df)
            exploratory_analysis(cleaned_df)
            print("\nAnalysis Summary:")
            print(f"- Total Titles: {len(cleaned_df)}")
            print(f"- Movies: {len(cleaned_df[cleaned_df['type'] == 'Movie'])}")
            print(f"- TV Shows: {len(cleaned_df[cleaned_df['type'] == 'TV Show'])}")
