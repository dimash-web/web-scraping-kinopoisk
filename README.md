# Movie Scraper and Randomizer

## Project Overview

This project is a web scraper that collects a list of the top 250 movies from **Kinopoisk**, a popular movie rating platform across post-Soviet countries. The purpose of this scraper is to provide users with a curated list of top-rated movies, which can be filtered by genre and used for random movie selection. This project is designed for educational purposes to demonstrate the use of web scraping and randomization techniques.

## Features

- **Top 250 Movies Scraper**: Scrapes a list of the 250 highest-rated movies from Kinopoisk.
- **Genre Filtering**: Users can scrape all genres or specify a single genre for targeted scraping.
- **Random Movie Selection**: Once the scraping is completed, the tool can randomly select a movie from the scraped data.
- **Web Scraping Tools**: Utilizes **Selenium** to navigate web pages and **BeautifulSoup** to extract relevant movie data.

## Data Description and Purpose

The data uncovered by the scraper includes:
- Movie title
- Link to the movie description
- Genre

The purpose of collecting this data is to provide users with a list of highly rated movies from Kinopoisk and allow them to receive a random movie suggestion from the list. This project serves as an educational tool for demonstrating web scraping and data manipulation techniques.

## Website Used and Why

The scraper collects data from [Kinopoisk](https://www.kinopoisk.ru), a widely used movie rating and review platform in post-Soviet countries. Kinopoisk was chosen because of its extensive and credible database of top-rated movies, making it a valuable resource for building a movie recommendation tool. The data is publicly accessible, and the scraper adheres to ethical practices outlined in our ETHICS.md file such as respecting the site’s `robots.txt` and terms of service.

## How to Run the Project

To run this project on your local machine, follow these steps:

1. Clone the repository
2. Navigate to the project directory (cd movie-scraper-randomizer)
3. Setting up a virtual environment is **NOT** required to run this project
4. Install the required dependencies from requirements.txt
5. Install a ChromeDriver and pass the address (path) of chromedriver on your PC in lines 13, 65
6. Run it!
