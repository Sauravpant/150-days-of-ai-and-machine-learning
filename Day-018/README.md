# Day 18 – Ridge, Lasso & ElasticNet Regression with Cross Validation

Today I worked on implementing regularized regression techniques (Lasso, Ridge, and ElasticNet) along with cross-validation to improve model performance and reduce overfitting.

---

## Key Learnings

- Loaded and cleaned the Algerian Forest Fire dataset  
- Handled missing values and corrected data types  
- Performed feature engineering and encoding of categorical variables  
- Removed highly correlated features using correlation thresholding  
- Standardized features using `StandardScaler`  
- Split dataset into training and testing sets  
- Trained multiple regression models:  
  - Linear Regression  
  - Lasso Regression (L1)  
  - Ridge Regression (L2)  
  - ElasticNet Regression (L1 + L2)  
- Applied cross-validation versions of all regularized models:  
  - LassoCV  
  - RidgeCV  
  - ElasticNetCV  
- Compared models using MAE and R² score  
- Visualized predictions using scatter plots (Actual vs Predicted)  
- Compared model performance with and without cross-validation using bar plots  