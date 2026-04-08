# Day 19 - Logistic Regression, Model Tuning, and ROC Analysis

Today I implemented and evaluated Logistic Regression for binary classification, then improved it using hyperparameter tuning and validated performance with ROC-AUC analysis.

---

## Key Learnings

- Built a baseline Logistic Regression classifier and evaluated it with:
	- Confusion Matrix
	- Accuracy Score
	- Classification Report (Precision, Recall, F1-score)
- Applied cross-validation-based tuning to improve model reliability:
	- GridSearchCV with StratifiedKFold
	- RandomizedSearchCV for faster parameter exploration
- Compared model settings across key Logistic Regression hyperparameters:
	- Regularization strength (`C`)
	- Penalty types (`l1`, `l2`, `elasticnet`, `none`)
	- Solver choices (`lbfgs`, `liblinear`, `newton-cg`, `newton-cholesky`)
- Visualized confusion matrix using a heatmap for clearer error interpretation
- Implemented ROC workflow for classification quality analysis:
	- Computed ROC curve (FPR vs TPR)
	- Calculated ROC-AUC score for quantitative comparison
	- Compared Logistic Regression against a dummy baseline model
	- Reviewed classification thresholds and their impact on model behavior
