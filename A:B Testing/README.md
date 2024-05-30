
# Cookie Cats Game AB Test Analysis

## Executive Summary
This project analyzes an A/B test conducted in the Cookie Cats mobile game to determine whether moving a key game feature (the gate) from level 30 to level 40 impacts user retention and engagement. Using Python, data analysis, and statistical testing, the study finds no significant difference between the two groups. The key skills demonstrated include data wrangling, exploratory data analysis, hypothesis testing, and data visualization. The business recommendation is to keep the gate at level 30, as moving it to level 40 does not significantly improve user retention or engagement.

## Business Problem
Cookie Cats, a popular mobile puzzle game, introduced a gate feature that players need to pass to continue playing. The game's developers want to test if moving the gate from level 30 to level 40 impacts player retention and game rounds played. The goal is to determine which gate level leads to better player retention and engagement, thereby optimizing the user experience and potentially increasing revenue.

## Methodology
1. **Data Loading and Initial Analysis**: Imported the dataset and explored its structure and summary statistics.
2. **Data Cleaning**: Identified and removed outliers to ensure robust statistical analysis.
3. **Exploratory Data Analysis (EDA)**: Analyzed distributions and summaries of key metrics such as game rounds played and retention rates.
4. **Hypothesis Testing**: Conducted A/B testing using parametric and non-parametric tests to compare the two groups (gate at level 30 vs. gate at level 40).
5. **Visualization**: Created visualizations to illustrate the distribution of game rounds and retention rates between the two groups.

## Skills
- **Programming Languages**: Python
- **Data Analysis Libraries**: Pandas, NumPy
- **Data Visualization Libraries**: Matplotlib, Seaborn
- **Statistical Testing**: Scipy (Shapiro-Wilk test, Levene's test, T-test, Mann-Whitney U test)
- **Methodologies**: Data wrangling, exploratory data analysis (EDA), hypothesis testing

## Results & Business Recommendation
- **Findings**: The A/B test results indicate no significant difference in game rounds played or retention rates between users with the gate at level 30 and those with the gate at level 40.
  - Retention after 1 day: Gate 30 (44.82%) vs. Gate 40 (44.23%)
  - Retention after 7 days: Gate 30 (19.02%) vs. Gate 40 (18.20%)
  - A/B test p-value: 0.0509 (fail to reject the null hypothesis)
- **Business Impact**: Moving the gate from level 30 to level 40 does not improve player retention or engagement. 
- **Recommendation**: Maintain the gate at level 30. Focus on other game elements to improve user retention and engagement.

## Next Steps
1. **Further Analysis**: Explore other segments of players (e.g., new vs. returning users) to see if specific groups are impacted differently.
2. **Feature Testing**: Test additional game features and their placement to optimize player experience.
3. **Long-term Retention**: Analyze long-term retention beyond the first 7 days to gain deeper insights into player behavior.
4. **Qualitative Feedback**: Collect and analyze qualitative feedback from users to complement quantitative findings and guide future feature adjustments.
