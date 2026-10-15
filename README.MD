Spotify Music Data Analysis | Python, Pandas & Seaborn

Project Overview

This project explores Spotify track data using Python to understand music popularity, genre performance, track information, and relationships between audio features.

The goal of this project is to practice Exploratory Data Analysis (EDA), data cleaning, statistical analysis, and data visualization to extract meaningful insights from music data.

Tech Stack

Python — Data analysis

Pandas — Data manipulation and cleaning

Matplotlib — Data visualization

Seaborn — Statistical visualization

Jupyter Notebook / Python Script — Analysis workflow

Dataset

The dataset contains Spotify track information, including track IDs, track names, artists, genres, popularity scores, explicit-content indicators, duration, and audio features.

Audio features analyzed include:

Energy

Danceability

Loudness

Speechiness

Acousticness

Instrumentalness

Liveness

Valence

Tempo

Note: Add the original dataset source and license here before publishing.

Project Objectives

Explore dataset structure, columns, and data types.

Identify missing values and duplicate records.

Investigate unique tracks, track names, and genres.

Analyze the most frequent track IDs and track names.

Identify the top 10 genres by average popularity.

Compare average popularity between explicit and non-explicit tracks.

Examine track duration, including zero-duration records.

Explore relationships between popularity and audio features.

Visualize correlations among numerical audio features.

Analysis & Visualizations

The project includes analysis and visualization techniques such as:

Bar Plot: Top 10 genres by average popularity.

Histogram: Distribution of track popularity.

Box Plot: Distribution and potential outliers in popularity and audio features.

Scatter Plots: Relationships between energy, danceability, and popularity.

Correlation Heatmap: Correlations between numerical audio features.

Pairplot: Pairwise relationships between selected audio features and popularity.

Data Cleaning

The analysis investigates:

Missing values in track names, artists, and album names.

Duplicate rows and repeated track IDs.

Records with zero-duration tracks.

Differences between the original dataset and filtered datasets.

Cleaning operations are evaluated to understand their impact on the data.

Key Learning Outcomes

Through this project, I practiced:

Exploratory Data Analysis (EDA)

Data cleaning with Pandas

Grouping and aggregation

Sorting and filtering datasets

Correlation analysis

Data visualization using Matplotlib and Seaborn

Interpreting patterns and limitations in real-world datasets

How to Run

Clone this repository.

Install the required Python libraries.

Place the dataset in the expected Data Set/ directory.

Run the Python analysis script.

Install dependencies:

pip install pandas matplotlib seaborn

Run the script:

python EDA.py

Ensure that the dataset path in the script matches your local folder structure.

Future Improvements

Add a concise summary of verified analytical findings.

Improve visualizations with consistent styling and labels.

Compare popularity across genres and audio features in greater detail.

Add a reproducible notebook and document the dataset source.

Explore an interactive dashboard for music analytics.

Author

Muhammad Areeb

Aspiring Data Engineer | Python | SQL | Data Analysis | ETL | Cloud Technologies

This project is part of my hands-on learning journey in data analytics and data engineering.

If you find this project useful, feel free to explore the repository and share feedback.
