import pandas as pd
import numpy as np

def create_user_item_matrix(ratings_df):
    """Creates a user-item matrix from the ratings dataframe."""
    user_item_matrix = ratings_df.pivot_table(
        index='user_id', columns='movie_id', values='rating', fill_value=0
    )
    return user_item_matrix

def get_similar_users(user_id, user_item_matrix):
    """Gets the most similar users to the given user."""
    similarities = user_item_matrix.corrwith(user_item_matrix.loc[user_id, :])
    similarities = similarities.sort_values(ascending=False)
    return similarities[1:]

def recommend_movies(user_id, user_item_matrix, movies_df):
    """Recommends movies to the given user."""
    similar_users = get_similar_users(user_id, user_item_matrix)
    recommended_movies = []
    for i, (_, similarity) in enumerate(similar_users.items()):
        for movie_id, rating in user_item_matrix.loc[i].items():
            if rating > 0 and movie_id not in recommended_movies:
                recommended_movies.append(movie_id)
                break
    return movies_df[movies_df['movie_id'].isin(recommended_movies)]

if __name__ == '__main__':
    # Load the ratings data
    ratings_df = pd.read_csv('ratings.csv')

    # Create the user-item matrix
    user_item_matrix = create_user_item_matrix(ratings_df)

    # Get the user id
    user_id = 1

    # Get the recommended movies
    recommended_movies = recommend_movies(user_id, user_item_matrix, movies_df)

    # Print the recommended movies
    print(recommended_movies)
