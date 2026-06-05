import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for visualizations
plt.style.use('ggplot')
sns.set_palette("Set2")

def load_happiness_data(file_path):
    """Load the World Happiness Report dataset."""
    try:
        df = pd.read_csv(file_path)
        print("World Happiness Dataset loaded successfully!")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def analyze_and_visualize(df):
    """Create advanced visualizations for Happiness factors."""
    print("\n--- Visualizing Happiness Data ---")
    
    # 1. Top 10 Happiest Countries
    top_10 = df.sort_values(by='Happiness Score', ascending=False).head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Happiness Score', y='Country', data=top_10, palette='viridis')
    plt.title('Top 10 Happiest Countries in the World')
    plt.savefig('../output/top_10_happiest.png')
    plt.close()

    # 2. Correlation Heatmap
    # Dropping non-numeric columns for correlation
    numeric_df = df.select_dtypes(include=[np.number])
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='RdYlGn', fmt='.2f')
    plt.title('Correlation Heatmap of Happiness Factors')
    plt.savefig('../output/correlation_heatmap.png')
    plt.close()

    # 3. GDP vs Happiness Score (Scatter plot with Regression Line)
    plt.figure(figsize=(10, 6))
    sns.regplot(x='Economy (GDP per Capita)', y='Happiness Score', data=df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
    plt.title('Impact of GDP on Happiness Score')
    plt.savefig('../output/gdp_vs_happiness.png')
    plt.close()

    # 4. Regional Comparison
    if 'Region' in df.columns:
        plt.figure(figsize=(12, 8))
        sns.boxplot(x='Happiness Score', y='Region', data=df, palette='Set3')
        plt.title('Happiness Score Distribution by Region')
        plt.savefig('../output/regional_distribution.png')
        plt.close()

    print("All visualizations saved in 'output/' folder.")

if __name__ == "__main__":
    # Recommended Dataset: World Happiness Report 2019 or 2021
    # URL: https://www.kaggle.com/datasets/unsdsn/world-happiness
    # Using a generic path for the user to place their file
    FILE_PATH = '../data/world_happiness.csv'
    
    import os
    if not os.path.exists(FILE_PATH):
        print(f"Dataset not found at {FILE_PATH}. Please place 'world_happiness.csv' in the 'data/' folder.")
        # Minimal dummy data for structure demo
        data = {
            'Country': ['Finland', 'Denmark', 'Switzerland', 'Iceland', 'Norway', 'Netherlands', 'Sweden', 'New Zealand', 'Austria', 'Luxembourg'],
            'Happiness Score': [7.8, 7.6, 7.5, 7.5, 7.4, 7.4, 7.3, 7.2, 7.2, 7.2],
            'Economy (GDP per Capita)': [1.2, 1.3, 1.4, 1.3, 1.4, 1.3, 1.3, 1.2, 1.3, 1.5],
            'Region': ['Western Europe', 'Western Europe', 'Western Europe', 'Western Europe', 'Western Europe', 'Western Europe', 'Western Europe', 'North America and ANZ', 'Western Europe', 'Western Europe']
        }
        df_dummy = pd.DataFrame(data)
        print("Running with dummy data for demonstration...")
        analyze_and_visualize(df_dummy)
    else:
        happiness_df = load_happiness_data(FILE_PATH)
        if happiness_df is not None:
            analyze_and_visualize(happiness_df)
