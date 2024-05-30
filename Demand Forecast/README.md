# Demand Prediction Project

## Executive Summary
This project involves predicting the total price of sold units using historical sales data. By utilizing a Decision Tree Regressor, we achieved a Root Mean Squared Error (RMSE) of 23.70. The project showcases skills in data preprocessing, visualization, and machine learning, specifically regression analysis. The insights gained can help businesses in demand forecasting and pricing strategy optimization. We recommend leveraging this model to enhance pricing decisions and inventory management.

## Business Problem
Effective demand forecasting is crucial for optimizing inventory levels and pricing strategies. Incorrect pricing or inventory can lead to lost sales or excess stock. This project aims to predict the total price of sold units based on historical sales data, helping businesses make informed decisions about pricing and inventory management.

![Demand Prediction](https://via.placeholder.com/600x300) 

## Methodology
1. **Data Collection and Preprocessing**:
   - Imported the dataset and performed initial exploration using pandas.
   - Removed any missing values from the dataset.
2. **Data Visualization**:
   - Created scatter plots using Plotly Express to visualize the relationship between units sold and total price.
   - Generated a heatmap using seaborn to display the correlation matrix of the dataset features.
3. **Feature Engineering**:
   - Selected relevant features (`Store ID`, `Base Price`, `Units Sold`) for modeling.
   - Split the data into training and testing sets using `train_test_split` from scikit-learn.
4. **Model Training and Prediction**:
   - Trained a Decision Tree Regressor on the training data.
   - Made predictions on the testing data.
5. **Model Evaluation**:
   - Evaluated the model performance using Root Mean Squared Error (RMSE).
   - Visualized the actual vs predicted prices using matplotlib.

## Skills
- **Programming Languages**: Python
- **Data Manipulation**: pandas, numpy
- **Data Visualization**: Plotly Express, seaborn, matplotlib
- **Machine Learning**: scikit-learn (Decision Tree Regressor, train_test_split)
- **Evaluation Metrics**: Mean Squared Error, Root Mean Squared Error

## Results & Business Recommendation
### Results:
- Achieved a Root Mean Squared Error (RMSE) of 23.70, indicating the model's accuracy in predicting total prices.
- Visualized the correlation between features and the relationship between actual and predicted prices.

### Business Recommendations:
- **Price Optimization**: Use the model to optimize pricing strategies by predicting the impact of different price points on total revenue.
- **Inventory Management**: Improve inventory management by forecasting demand more accurately, reducing stockouts and overstock situations.
- **Marketing Strategies**: Tailor marketing strategies based on predicted demand, focusing efforts on high-demand periods or products.
- **Sales Performance Monitoring**: Continuously monitor and adjust the model with new data to maintain and improve its accuracy.

## Next Steps
1. **Model Improvement**: Experiment with more advanced regression models such as Random Forest or Gradient Boosting to improve prediction accuracy.
2. **Feature Enhancement**: Include additional features like promotional discounts, seasonal effects, and customer demographics to enhance the model.
3. **Cross-Validation**: Implement cross-validation techniques to ensure the model's robustness and generalizability.
4. **Integration with Business Systems**: Integrate the prediction model with business systems for real-time pricing and inventory management.
5. **Continuous Monitoring**: Set up a pipeline for continuous monitoring and updating of the model to adapt to market changes and new data trends.

By pursuing these next steps, businesses can further refine their demand forecasting capabilities and make more data-driven decisions.
