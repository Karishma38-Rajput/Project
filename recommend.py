import pandas as pd

# Load the movie dataset
data = pd.read_csv('movies.csv')

# Get user input
fav_movie = input("Enter your favorite movie: ")

# Get the genre of the favorite movie
if fav_movie in data['title'].values:
    genre = data[data['title'] == fav_movie]['genre'].values[0]
    print(f"\nBecause you like '{fav_movie}', you might also like these {genre} movies:\n")

    # Recommend movies of the same genre (excluding the input)
    recommendations = data[(data['genre'] == genre) & (data['title'] != fav_movie)]
    for title in recommendations['title'].values:
        print("- " + title)
else:
    print("Movie not found in database.")
