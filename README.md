# World Happiness Data Visualization

## Project Overview
This project focuses on **Data Visualization** to explore the factors that contribute to global happiness. Using the World Happiness Report dataset, we visualize how economy, social support, and health influence a country's happiness score.

## Objective
- Visualize the ranking of the happiest countries.
- Identify correlations between GDP, Life Expectancy, and Happiness.
- Compare happiness distributions across different world regions.

## Dataset
- **Name**: World Happiness Report
- **Source**: [Kaggle - World Happiness](https://www.kaggle.com/datasets/unsdsn/world-happiness)
- **Format**: CSV (`world_happiness.csv`)

## Implementation Steps
1. **Data Preparation**: Cleaning column names and handling region-specific data.
2. **Correlation Analysis**: Using heatmaps to find the strongest drivers of happiness.
3. **Scatter Analysis**: Visualizing the relationship between wealth (GDP) and well-being.
4. **Regional Insights**: Using Boxplots to see which regions are consistently happier.

## Key Insights
- **GDP and Social Support** have the strongest positive correlation with Happiness scores.
- **Western Europe** and **North America** consistently rank higher in happiness.
- Sub-Saharan African countries often have lower scores but show interesting outliers in social support.

## How to Run
1. Install requirements: `pip install pandas numpy matplotlib seaborn`
2. Place your CSV in `data/world_happiness.csv`.
3. Run: `python notebooks/happiness_viz.py`

## Folder Structure
```
Project_2_Data_Viz_Happiness/
├── data/           # Raw CSV
├── notebooks/      # Visualization code
├── output/         # Visualization images (PNG)
└── README.md
```
 Eleanor Roosevelt once said, "Happiness is not a goal... it's a by-product of a life well lived." This project quantifies that by-product!
