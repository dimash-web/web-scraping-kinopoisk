from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random
import re
import math

# Function to scrape movies from a given URL using Selenium
def scrape_movies_for_pages(url):  #plus scrapes the first page
    try:
        # Set up the WebDriver (Chrome in this case)
        service = Service('C:\Program Files\chromedriver-win64\chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        
        # Open the URL with the Selenium WebDriver
        driver.get(url)
        
        # Wait for the page to fully load
        time.sleep(20)  #long because sometimes the website requires to verify that user is not a robot
        
        # Get the page source
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        len_movies = soup.find('div', {'data-tid': 'c97bf23b'})
        len_movies_a = len_movies.find('a', {'class': 'styles_root__o_aAP styles_rootActive__xFaoQ'}) 
        len_movies_span = len_movies_a.find('span', {'class': 'styles_subtitle__V93vt'})
        if len_movies_span:
            len_movies_text = len_movies_span.text.strip()
            # Extract digits using regular expression
            len_movies_num = re.findall(r'\d+', len_movies_text)
            print(f"Found {len_movies_num[0]} movies")

            movies_per_page = 50
            num_pages = math.ceil(int(len_movies_num[0])/movies_per_page)
            # print(num_pages)
        
        # Find all movie blocks by their 'data-test-id' identifier
        top_movies = soup.find_all('div', {'data-test-id': 'movie-list-item'})

        # Print the extracted movie elements for verification
        print(f"Scanned {len(top_movies)} movies in page 1")

        # Loop through each movie block and extract the title
        movies_info = []
        for movie in top_movies:
            title_element = movie.find('span', {'class': 'desktop-list-main-info_secondaryTitle__ighTt'})
            link_element = movie.find('a', {'class': 'base-movie-main-info_link__YwtP1'})
            if title_element and link_element:
                title = title_element.text.strip()
                link = link_element['href'].strip()
                movies_info.append((title, link))
        # Close the browser after scraping
        driver.quit()
        return num_pages, movies_info
    
    
    except Exception as e:
        print(f"An error has occurred: {e}")
        return 0, []

def scrape_movies_list(url, page):
    try:
        # Set up the WebDriver (Chrome in this case)
        service = Service('C:\Program Files\chromedriver-win64\chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        
        # Open the URL with the Selenium WebDriver
        driver.get(url+f"&page={page}")
        
        # Wait for the page to fully load
        time.sleep(20)  #long because sometimes the website requires to verify that user is not a robot

        # Get the page source
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find all movie blocks by their 'data-test-id' identifier
        top_movies = soup.find_all('div', {'data-test-id': 'movie-list-item'})

        # Print the extracted movie elements for verification
        print(f"Scanned {len(top_movies)} movies in page {page}")

        # Loop through each movie block and extract the title
        movies_info = []
        for movie in top_movies:
            title_element = movie.find('span', {'class': 'desktop-list-main-info_secondaryTitle__ighTt'})
            link_element = movie.find('a', {'class': 'base-movie-main-info_link__YwtP1'})
            if title_element and link_element:
                title = title_element.text.strip()
                link = link_element['href'].strip()
                movies_info.append((title, link))

        # Close the browser after scraping
        driver.quit()
        return movies_info
    except Exception as e:
        print(f"An error has occurred: {e}")
        return []


# Function to choose a genre for filtering movies
def choose_genre():
    status = False
    genre_dict = {
        "1": "anime", "2": "biography", "3": "action", "4": "western", "5": "war",
        "6": "mystery", "7": "drama", "8": "history", "9": "comedy", "10": "crime",
        "11": "romance", "12": "animation", "13": "musical", "14": "adventure",
        "15": "sport", "16": "thriller", "17": "horror", "18": "sci-fi", "19": "fantasy"
    }
   
    while status == False:
        genre = input('''
        Genres list:
            1. Anime
            2. Biography
            3. Action
            4. Western
            5. War
            6. Mystery
            7. Drama
            8. History
            9. Comedy
            10. Crime
            11. Romance
            12. Animation
            13. Musical
            14. Adventure
            15. Sport
            16. Thriller
            17. Horror
            18. Sci-fi
            19. Fantasy
        Enter your choice (1-19): ''')

        if genre in genre_dict:
            status = True
            return genre_dict[genre]
        else:
            print("Invalid input! Try again!")

# Main function to prompt the user and fetch movies based on selection
def main():
    status = False
    while status == False:
        filter_enable = input('''Would you like to choose the genre?
                            1. All genres
                            2. Choose genre
Enter 1 or 2: ''')

        movies_list = []
        if filter_enable == '1':
            status = True
            url = "https://www.kinopoisk.ru/lists/movies/top250/genre--all/?utm_referrer=www.kinopoisk.ru"
            pages_num, movies_info = scrape_movies_for_pages(url)
            movies_list.extend(movies_info)
        elif filter_enable == '2':
            status = True
            selected_genre = choose_genre()
            url = f"https://www.kinopoisk.ru/lists/movies/top250/genre--{selected_genre}/?utm_referrer=www.kinopoisk.ru"
            pages_num, movies_info = scrape_movies_for_pages(url)
            movies_list.extend(movies_info)

        else:
            print("Enter a valid input!")

    
    page = 2
    while (page <= pages_num):
        print(f"There are {pages_num} pages of movies for this genre. Scraping page #{page}. Please wait...")
        movies = scrape_movies_list(url, page)
        movies_list.extend(movies)
        page += 1

    # Choose a random movie
    random_movie = random.choice(movies_list)
    print(f"Random Movie Selected: {random_movie[0]}")
    print(f"Link: https://www.kinopoisk.ru{random_movie[1]}")
    
# Entry point
if __name__ == "__main__":
    main()