# Movie Recommendation System

## Executive Summary
This project showcases a movie recommendation system leveraging the Surprise library to implement collaborative filtering using Singular Value Decomposition (SVD). The system aims to recommend movies to users based on their past ratings. By tuning hyperparameters and evaluating the model's performance using cross-validation, we ensure optimal recommendations. Key skills demonstrated include Python, data manipulation with pandas, and machine learning techniques. The business impact of this project is significant, potentially enhancing user engagement and retention for streaming platforms by providing personalized content.

## Business Problem
In the competitive streaming industry, user retention and engagement are critical. Personalized movie recommendations can significantly enhance user experience, encouraging longer subscriptions and increased usage. This project addresses the need for a robust recommendation system to suggest movies that users are likely to enjoy based on their previous ratings. By improving recommendation accuracy, the platform can increase user satisfaction and loyalty.


## Methodology
The project involves the following steps:
1. Loading and preprocessing the dataset using pandas.
2. Utilizing the Surprise library to load data into a suitable format.
3. Defining a parameter grid for SVD hyperparameter tuning.
4. Performing GridSearchCV to find the best hyperparameters.
5. Evaluating the best model using cross-validation.
6. Training the final model on the entire dataset.
7. Implementing a function to generate top N movie recommendations for a user.

## Skills
- **Python**: Data manipulation with pandas, machine learning with Surprise.
- **Data Science**: Collaborative filtering, hyperparameter tuning, cross-validation.
- **Libraries**: pandas, Surprise, GridSearchCV.

Specific techniques used include:
- **Surprise library**: For collaborative filtering.
- **GridSearchCV**: For hyperparameter optimization.
- **Cross-validation**: To evaluate model performance.
- **Pandas**: For data loading and preprocessing.

## Results & Business Recommendation
The grid search identified the optimal hyperparameters for the SVD model, resulting in improved recommendation accuracy:
Evaluating RMSE, MAE of algorithm SVD on 5 split(s).

| Metric          | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 | Mean   | Std   |
|-----------------|--------|--------|--------|--------|--------|--------|-------|
| RMSE (testset)  | 0.8557 | 0.8474 | 0.8446 | 0.8538 | 0.8523 | 0.8508 | 0.0042|
| MAE (testset)   | 0.6571 | 0.6521 | 0.6472 | 0.6526 | 0.6531 | 0.6524 | 0.0031|
| Fit time        | 0.93   | 0.94   | 1.09   | 0.93   | 0.94   | 0.97   | 0.06  |
| Test time       | 0.03   | 0.05   | 0.05   | 0.05   | 0.03   | 0.04   | 0.01  |


Top 10 recommendations for a sample user (ID: 1) include:
1. Shawshank Redemption, The (1994)
2. Wallace & Gromit: The Best of Aardman Animation (1996)
3. Patton (1970)
4. In the Name of the Father (1993)
5. North by Northwest (1959)
6. Casablanca (1942)
7. Beautiful Thing (1996)
8. Outlaw Josey Wales, The (1976)
9. L.I.E. (2001)
10. Godfather, The (1972)

### Business Impact
- **Enhanced User Experience**: Personalized recommendations can lead to increased user satisfaction.
- **Increased Retention**: Users are more likely to stay subscribed if they find relevant content easily.
- **Better Engagement**: Personalized content can increase the time users spend on the platform.

### Recommendation
To maximize business impact, integrate this recommendation system into the streaming platform’s backend. Regularly update the model with new user data to maintain recommendation accuracy. Collaborate with the marketing team to promote personalized movie suggestions to users.

## Next Steps
1. **Integrate with Real-Time Data**: Update recommendations based on real-time user interactions.
2. **Explore Hybrid Models**: Combine collaborative filtering with content-based filtering for improved recommendations.
3. **Scalability**: Optimize the system for large-scale data and high user traffic.
4. **A/B Testing**: Conduct experiments to measure the impact of recommendations on user engagement and retention.
5. **Feedback Loop**: Implement a mechanism for users to provide feedback on recommendations to continuously improve the model.

