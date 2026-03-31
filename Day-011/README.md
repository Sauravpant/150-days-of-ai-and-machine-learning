### Day 11 - Feature Engineering Fundamentals

Today I learned core **feature engineering** techniques that improve data quality and model performance. The focus was on preparing real-world datasets by handling **missing values**, treating **outliers**, applying **encoding techniques** for categorical variables, and working with **imbalanced datasets**.

---

#### **Key Points**

- Understood why feature engineering is essential for building reliable machine learning pipelines
- Explored strategies for **handling missing values**:
	- Removing rows/columns when missingness is high
	- Imputing with mean, median, mode, and constant values based on data type and distribution
- Studied **outlier detection and treatment**:
	- Identifying outliers using statistical methods and visual checks
	- Handling them through capping, transformation, or removal depending on context
- Practiced **encoding techniques** for categorical data:
	- Label Encoding for ordinal-like categories
	- One-Hot Encoding for nominal categories
	- Choosing encoding methods based on model type and cardinality
- Learned **imbalanced dataset handling**:
	- Recognized class imbalance problems and their impact on model bias
	- Applied balancing approaches such as oversampling and undersampling
	- Focused on using proper evaluation metrics instead of only accuracy
- Reinforced the idea that preprocessing decisions should be driven by both data characteristics and business context

---

#### **Files Practiced Today**

- `notebooks/missing_values.ipynb`
- `notebooks/outliers.ipynb`
- `notebooks/encoding.ipynb`
- `notebooks/imbalanced_dataset.ipynb`
