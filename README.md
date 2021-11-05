# Customer_Churn_Prediction
Kaggle competition is about predicting whether a customer will change telecommunications provider, something known as "churning".
The training dataset contains 4250 samples. Each sample contains 19 features and 1 boolean variable "churn" which indicates the class of the sample. The 19 input features and 1 target

# This repository contains :

1**Exploratory Data Analysis (EDA) and pandas profiling for the dataset**

For each column the following statistics - if relevant for the column type - are presented in an interactive HTML report:
Type inference: detect the types of columns in a dataframe.
Essentials: type, unique values, missing values
Quantile statistics like minimum value, Q1, median, Q3, maximum, range, interquartile range
Descriptive statistics like mean, mode, standard deviation, sum, median absolute deviation, coefficient of variation, kurtosis, skewness
Most frequent values
Histogram
Correlations highlighting of highly correlated variables, Spearman, Pearson and Kendall matrices
Missing values matrix, count, heatmap and dendrogram of missing values
Text analysis learn about categories (Uppercase, Space), scripts (Latin, Cyrillic) and blocks (ASCII) of text data.
File and Image analysis extract file sizes, creation dates and dimensions and scan for truncated images or those containing EXIF information.

2-Machine learning model to classify wether the castomer will churn or not 
Here I will give data to different machine learning models and then decide which is better 

But before that, the data  need to be splited into train, test 

from EDA we find that the data is unbalanced so we will upsampling data 
 
**compare between classifcation models to choose the best one**

1-random forest

2-Support Vector classifier 

3-Logistic Regression
 
we care about false negative and false positive 

false negative means that the model predict that the client won't chrun but it chrun 

so we care aboout recall 

Here is the highest value for **recall** find in **Random Forest** 
 
**Last step**

Save the model parameter in a packle file to use the model in FastAPI

**3-Model deployment using FastAPI**

