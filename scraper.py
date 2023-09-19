import requests
from bs4 import BeautifulSoup

def scrape_movies(year, genre):
    # Check if year is not a number or genre is empty
    if not year.isdigit() or not genre:
        return []

    url = f"http://www.imdb.com/search/title?release_date={year}-01-01,{year}-12-31&title_type=feature&genres={genre}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    movie_data = []

    for movie in soup.find_all("div", class_="lister-item-content"):
        title = movie.h3.a.text
        rating = movie.strong
        if rating:
            rating = rating.text
        else:
            rating = "N/A"

        movie_data.append({
            "title": title,
            "rating": rating,
        })

    return movie_data
