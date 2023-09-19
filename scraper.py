import requests
from bs4 import BeautifulSoup

def scrape_movies(year, genre):
    # Define the URL for IMDb's search page with user-selected parameters
    url = f"http://www.imdb.com/search/title?release_date={year}&title_type=feature&genres={genre}"

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract movie data, including title, rating, and other details
    movie_data = []
    for movie in soup.find_all("div", class_="lister-item mode-advanced"):
        title = movie.h3.a.text
        rating = movie.strong.text
        movie_data.append({"title": title, "rating": rating})

    return movie_data
