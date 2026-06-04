# Project Report: Netflix Content Strategy Analysis

## 1. Executive Summary
This report details the findings of an Exploratory Data Analysis conducted on the Netflix library. The study identifies key trends in content acquisition and highlights the platform's global expansion strategy.

## 2. Methodology
- **Tooling**: Python 3.x, Pandas for data manipulation, Seaborn/Matplotlib for visualization.
- **Process**: Data ingestion -> Cleaning (handling nulls) -> Feature Engineering (date extraction) -> Visualization.

## 3. Data Cleaning Details
- Missing `country` entries were labeled as 'Unknown'.
- Missing `director` and `cast` were filled with placeholders.
- Date formats were standardized for temporal analysis.

## 4. Analysis and Findings
### 4.1 Content Balance
A plurality of Netflix content consists of Feature Films. However, TV Shows show a higher retention potential and are growing steadily in the library.

### 4.2 Content Inflow
Between 2016 and 2019, Netflix aggressively scaled its content library, with 2019 being a peak year for additions.

### 4.3 Geographical Insights
The USA, India, and the UK are the primary contributors. Exploring emerging markets (e.g., South Korea) shows high engagement in specific genres.

## 5. Conclusion & Recommendations
Netflix should continue investing in International Content, as "International Movies" is one of the top categories. Diversifying genres in under-represented countries could further boost global sub-counts.

---
*Internship: CodeAlpha Data Analytics*
*Project: Task 1 - EDA*
