# Netflix-Data-Cleaning-Project-

# Netflix Data Cleaning and Preprocessing

## Objective

The objective of this project is to clean and preprocess the Netflix Movies and TV Shows dataset by handling missing values, removing duplicates, standardizing data formats, and preparing the dataset for further analysis.

## Dataset

Netflix Movies and TV Shows Dataset from Kaggle.

## Tools Used

* Python
* Pandas
* Visual Studio Code

## Dataset Information

* Records: 8,807
* Columns: 12

## Data Quality Issues Identified

| Column     | Missing Values |
| ---------- | -------------- |
| director   | 2634           |
| cast       | 825            |
| country    | 831            |
| date_added | 10             |
| rating     | 4              |
| duration   | 3              |

## Data Cleaning Steps

### 1. Loaded Dataset

The dataset was loaded using Pandas.

### 2. Checked Missing Values

Missing values were identified using:

```python
df.isnull().sum()
```

### 3. Removed Duplicate Records

Duplicate rows were removed using:

```python
df.drop_duplicates()
```

### 4. Handled Missing Values

Missing values were replaced with appropriate placeholder values such as "Unknown" and "Not Rated".

### 5. Standardized Column Names

Column names were converted to lowercase and spaces were replaced with underscores.

### 6. Converted Date Format

The `date_added` column was converted into datetime format using Pandas.

### 7. Cleaned Text Fields

Extra spaces were removed from text columns.

### 8. Saved Cleaned Dataset

The cleaned dataset was exported as:

`cleaned_netflix_titles.csv`

## Results

* Missing values handled successfully.
* Dataset standardized and cleaned.
* Dataset prepared for further analysis and visualization.

## Project Structure

```text
dataset/
├── netflix_titles.csv
├── cleaned_netflix_titles.csv

screenshots/
├── code.png
├── output.png
├── missing_values.png

task1.py
README.md
```

## Author

Himadri Singh
