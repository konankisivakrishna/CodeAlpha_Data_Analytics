# Netflix Content Analysis - Exploratory Data Analysis (EDA)

## Project Overview
This project performs an Exploratory Data Analysis (EDA) on the Netflix Titles dataset to uncover insights about content distribution, trends over time, and regional availability.

## Objective
To understand Netflix's content strategy by analyzing:
- The ratio of Movies vs. TV Shows.
- Content growth over the last decade.
- Top producing countries and popular genres.

## Dataset
- **Name**: Netflix Movies and TV Shows
- **Source**: [Kaggle - Netflix Titles](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **Format**: CSV (`netflix_titles.csv`)

## Step-by-Step Implementation
1. **Data Loading**: Using Pandas to read the raw CSV.
2. **Data Cleaning**: Handling missing values in `director`, `cast`, and `country`. Converting `date_added` to datetime objects.
3. **Exploratory Analysis**:
   - Analysis of Content Type distribution.
   - Time-series analysis of content additions.
   - Categorical analysis of Genres and Countries.
4. **Visualization**: Creating charts using Matplotlib and Seaborn.

## Key Insights
- Netflix focuses more on **Movies** than TV Shows (approx. 70/30 split).
- Significant growth in content addition observed post-2015.
- The **United States** is the leading content producer, followed by India.
- **International Movies** and **Dramas** are the most frequent genres.

## How to Run
1. Install requirements: `pip install pandas numpy matplotlib seaborn`
2. Place `netflix_titles.csv` in the `data/` folder.
3. Run the script: `python notebooks/netflix_eda.py`

## Folder Structure
```
Project_1_EDA_Netflix/
├── data/           # Raw dataset
├── notebooks/      # Python implementation scripts
├── output/         # Saved visualizations
└── README.md       # Project documentation
```
