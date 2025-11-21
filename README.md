# Miami-gentrification-forecast

This project aims to build a **machine learning model** that predicts which Miami-Dade neighborhoods are currently experiencing, or are at risk of experiencing, **gentrification**. Our approach leverages prior research on urban change and predictive modeling.

We will build a **Random Forest classification model**, chosen because prior research (Yoo, 2023) shows that Random Forests perform especially well in gentrification prediction tasks. This model works effectively with large datasets, handles nonlinear patterns, and can capture the complex interactions found in neighborhood-level socioeconomic data.

## Dataset

The dataset is created by combining multiple public sources:

- **Primary data:** Miami-Dade County ACS datasets from 2019 and 2024
- **Information included:** Household characteristics, education levels, housing conditions, income distributions
- **Processing:** After preprocessing and cleaning, the dataset includes:
  - Predictive variables (features)
  - Target label indicating whether a neighborhood is gentrified or at risk

## Features

Each neighborhood is represented by multiple input features, such as:

- Median rent  
- Median household income  
- Home values  
- Vacancy rates  
- Poverty rate  
- Levels of educational attainment  

These features are used to predict a **single gentrification label**, making this a **many-to-one classification problem**.

## Model Evaluation

To measure performance, we will evaluate the model using **accuracy, precision, recall, and F1-score**. These metrics will help us understand how reliably the model identifies neighborhoods experiencing or likely to experience gentrification, while also addressing potential class imbalances in the data.

