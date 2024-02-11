# Netflix TV Shows and Movies Data Analysis

## Description
This project contains a detailed exploratory analysis of the "Netflix TV Shows and Movies" dataset. The goal is to uncover interesting patterns, trends over time, and insights into content ratings and viewer preferences.

## Project Structure

The project is organized as follows:

- `data/`: Contains the datasets used in the project.
  - `raw/`: Raw data downloaded or acquired.
  - `processed/`: Cleaned and processed data ready for analysis.
- `scripts/`: Scripts for data cleaning, preparation, and analysis.
  - `data_preparation.py`: Script for data cleaning and preparation.
  - `utilities.py`: Utility functions for analysis and visualization.
- `figures/`: Charts and figures generated during the analysis.
- `README.md`: This README file with project information.



## Environment Setup
Follow the steps below to set up the necessary environment to run the scripts for this project.

### Setup Steps
1. Clone the repository, install Python 3.8 (if necessary), and the project dependencies.
   ```bash
   git clone https://github.com/yourusername/AED_netflix_IMDB.git
   cd AED_netflix_IMDB
   pip install -r requirements.txt
   # Or for Conda users
   conda env create -f environment.yml
   conda activate AED_netflix_IMDB

## Running the Scripts
To execute the analysis and visualization scripts, navigate to the scripts/ folder and run the corresponding Python files.

## Visualizations
The visualizations generated in the project offer various insights into the Netflix dataset, including:

IMDB Score Distribution: Histograms showing the distribution of ratings for movies and TV shows, helping to understand the overall quality of available content.
Content Trends by Year: Line charts revealing how the quantity of content (movies and TV shows) has changed over the years.
Content Distribution by Age Rating: Bar charts indicating the amount of content available for different age groups.
Word Cloud of Descriptions: A visual representation highlighting the most frequent words in the descriptions of movies and TV shows, giving an idea of prevalent themes and genres.
Each visualization is saved in the figures/ folder, providing a quick and intuitive way to understand the characteristics of the dataset.

## Contributing
Contributions to improve the project are welcome. Feel free to fork the repository and submit your suggestions through pull requests.

## License
ISC License

Copyright (c) 2024 César Henrique Sousa Lima

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
