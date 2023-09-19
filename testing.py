import unittest
import scraper

class TestScraper(unittest.TestCase):

    def test_scrape_movies(self):
        # Test scraping movies for a specific year and genre
        year = "2020"
        genre = "Action"
        movie_data = scraper.scrape_movies(year, genre)

        # Assert that the scraped data is not empty
        self.assertTrue(len(movie_data) > 0)

        # Check if the data has the expected keys (title, rating)
        for movie in movie_data:
            self.assertIn("title", movie)
            self.assertIn("rating", movie)

    def test_scrape_movies_invalid_input(self):
        # Test scraping movies with invalid input (non-numeric year and empty genre)
        invalid_year = "invalid_year"
        invalid_genre = ""
        movie_data = scraper.scrape_movies(invalid_year, invalid_genre)

        # Assert that the scraped data is empty for invalid input
        self.assertEqual(len(movie_data), 0)


if __name__ == "__main__":
    unittest.main()
