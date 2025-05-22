Recommendation System

This project is a simple user-based collaborative filtering recommendation system built using Python, Pandas, and NumPy. It recommends movies to a user based on the preferences of similar users.

## Files

- `main.py` – Contains the Python code for generating movie recommendations.
- `ratings.csv` – A CSV file containing user ratings for movies.
- `movies.csv` – A CSV file containing movie metadata.

## Data Format

### ratings.csv

| user_id | movie_id | rating |
|---------|----------|--------|
| 1       | 10       | 4.5    |
| 2       | 20       | 3.0    |
| ...     | ...      | ...    |

### movies.csv

| movie_id | title               |
|----------|---------------------|
| 10       | The Matrix          |
| 20       | Inception           |
| ...      | ...                 |

## How It Works

1. **User-Item Matrix Creation**: Builds a matrix with users as rows and movies as columns, with ratings as values.
2. **User Similarity Calculation**: Computes the correlation between the target user and all other users.
3. **Movie Recommendation**: Recommends movies rated by similar users that the target user hasn't rated yet.

## How to Run

1. Install dependencies:
   ```bash
   pip install pandas numpy
Place ratings.csv, movies.csv, and main.py in the same directory.

Run the program:

bash
Copy
Edit
python main.py
The script will print movie recommendations for the specified user_id.

Notes
You can change the user_id variable in main.py to get recommendations for a different user.

The current recommendation logic selects one movie from each similar user.

Future Improvements
Recommend top-N movies based on a weighted average of ratings.

Implement item-based collaborative filtering.

Add support for a web interface or interactive CLI.
