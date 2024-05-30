import pandas as pd
from surprise import Reader, Dataset, SVD, accuracy
from surprise.model_selection import cross_validate, GridSearchCV, train_test_split

# Load ratings dataset
ratings = pd.read_csv('ml-latest-small/ratings.csv')
# Load movies dataset
movies = pd.read_csv('ml-latest-small/movies.csv')

# Initialize Reader object
reader = Reader()

# Load the dataset into the Surprise data structure
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)

# Define parameter grid for hyperparameter tuning
param_grid = {
    'n_factors': [50, 100, 150],
    'n_epochs': [20, 30, 40],
    'lr_all': [0.002, 0.005, 0.01],
    'reg_all': [0.02, 0.1, 0.4]
}

# Perform grid search cross-validation
gs = GridSearchCV(SVD, param_grid, measures=['rmse', 'mae'], cv=5)
gs.fit(data)

# Get the best model
best_algo = gs.best_estimator['rmse']

# Evaluate the best model with cross-validation
cross_validate(best_algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

# Train the best algorithm on the full dataset
trainset = data.build_full_trainset()
best_algo.fit(trainset)

# Function to get top n movie recommendations for a user
def get_top_n_recommendations(user_id, n=10):
    # Get a list of all movie ids
    movie_ids = ratings['movieId'].unique()
    # Remove the movies the user has already rated
    movies_unrated = [movie_id for movie_id in movie_ids if
                      movie_id not in ratings[ratings['userId'] == user_id]['movieId'].unique()]

    # Predict ratings for all unrated movies
    predictions = [best_algo.predict(user_id, movie_id) for movie_id in movies_unrated]

    # Sort predictions by estimated rating in descending order
    predictions.sort(key=lambda x: x.est, reverse=True)

    # Get top n recommendations
    top_n = predictions[:n]

    # Get movie ids and titles for the recommendations
    movie_ids = [pred.iid for pred in top_n]
    movie_titles = [movies[movies['movieId'] == movie_id]['title'].values[0] for movie_id in movie_ids]

    return movie_titles

# Example: Get top 10 recommendations for user with ID 1
user_id = 1
recommendations = get_top_n_recommendations(user_id)
print(f"Top 10 recommendations for user {user_id}:")
for i, movie_title in enumerate(recommendations, start=1):
    print(f"{i}. {movie_title}")
