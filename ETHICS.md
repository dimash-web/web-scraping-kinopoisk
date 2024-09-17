# Ethical considerations of web scraping wihtin this project

## Purpose of data collection
The purpose of this project is to scrape a list of the top 250 movies from Kinopoisk.ru to provide users with a randomised option of a highly rated film. The data is used for educational purposes, specifically to explore web scraping techniques, and to offer users random movie suggestions from a reputable movie rating platform. 

## Data sources and robots.txt
Having studied the robots.txt guidelines of Kinopoisk.ru, we ensured that no restricted sections of the website are scraped. Only publicly accessible data (such as movie titles, genres, and ratings) is collected.


## Collection practices
To minimize the load on Kinopoisk’s servers, the scraper operates at a controlled rate, ensuring that excessive requests are not made in a short period of time, which could disrupt their service.

To ensure we do not bypass password protection, no login credentials or password-protected areas are accessed. The scraper only gathers publicly available data that is visible without user authentication.

## Data handling and privacy
The scraper does not collect any personally identifiable information (PII) such as user profiles, comments, or any data that is associated with individual users. The focus is strictly on movie titles, ratings, and genres.

## Data usage

The data collected from Kinopoisk is used solely for educational purposes to demonstrate web scraping techniques and for research on movie recommendations. It will not be used for any commercial purposes, ensuring that all research complies with ethical standards and the honor code of NYU.