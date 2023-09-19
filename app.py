from flask import Flask, render_template, request
import scraper

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_year = request.form["year"]
        user_genre = request.form["genre"]
        top_n_str = request.form["top_n"]

        # Check if the "Top N" field is not empty
        if top_n_str.strip():  # This ensures there's at least one non-space character
            top_n = int(top_n_str)
        else:
            # Handle the case where "Top N" is empty or contains only spaces
            top_n = 5  # Default value (you can choose a different default)

        # Call the scrape_movies function with user preferences
        movie_data = scraper.scrape_movies(user_year, user_genre)
        # Sort the scraped movie data by rating
        movie_data.sort(key=lambda x: float(x["rating"]), reverse=True)
        top_movies = movie_data[:top_n]

        # Create a list of movie recommendations with titles and ratings
        recommendations = [
            f"{i + 1}. {movie['title']} - Rating: {movie['rating']}"
            for i, movie in enumerate(top_movies)
        ]

        return render_template("index.html", recommendations=recommendations)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
