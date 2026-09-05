 Pandas Analyzer & Data Visualization

 Project Overview

**Pandas Analyzer & Data Visualization** is a Python-based data analysis
project designed to load, clean, analyze, manipulate, and visualize
sales data stored in a CSV file.

The project uses **Pandas** for DataFrame operations, **NumPy** for
numerical and array operations, **Matplotlib** and **Seaborn** for data
visualization, and **Object-Oriented Programming (OOP)** to organize the
complete application.

The project provides a menu-driven interface so users can perform
different analysis operations without writing additional code.

------------------------------------------------------------------------

## Objectives

The main objectives of this project are:

-   Load sales data from a CSV file.
-   Explore and understand the dataset.
-   Detect and handle missing values.
-   Remove duplicate records.
-   Perform data type conversions.
-   Perform mathematical and numerical operations.
-   Demonstrate NumPy array creation, indexing, and slicing.
-   Search, sort, and filter records.
-   Apply aggregation and statistical functions.
-   Create pivot tables for data summarization.
-   Split data using categories such as Region or Product.
-   Generate useful charts and visualizations.
-   Save visualizations as image files.
-   Generate a summary analysis report.
-   Demonstrate Object-Oriented Programming concepts.
-   Provide a simple menu-driven user interface.

------------------------------------------------------------------------

## Technologies Used

  Technology         Purpose
  ------------------ ----------------------------------------------------
  Python             Main programming language
  Pandas             Data loading, cleaning, manipulation, and analysis
  NumPy              Numerical calculations and array operations
  Matplotlib         Data visualization
  Seaborn            Statistical visualization
  Jupyter Notebook   Development and documentation environment
  CSV                Input data format

------------------------------------------------------------------------

## Project Structure

``` text
Pandas_Analyzer/
│
├── pandas_analyzer.py
├── sales_data.csv
├── requirements.txt
├── README.md
│
└── visualizations/
    ├── bar_chart.png
    ├── line_chart.png
    ├── scatter_plot.png
    ├── pie_chart.png
    ├── histogram.png
    ├── stack_plot.png
    └── subplots.png
```

> `sales_data.csv` can be generated automatically by the Python program
> when using the built-in sample data section.

------------------------------------------------------------------------

## Class Structure

The project is organized around the following class:

### `SalesDataAnalyzer`

This class encapsulates the main data analysis and visualization
functionality.

### Attribute

``` python
self.data
```

`self.data` stores the sales information in a Pandas DataFrame.

### Main Methods

``` text
__init__()
__del__()
load_data()
explore_data()
clean_data()
numpy_operations()
mathematical_operations()
combine_data()
split_data()
search_data()
sort_data()
filter_data()
aggregate_functions()
statistical_analysis()
create_pivot_table()
visualize_data()
bar_chart()
line_chart()
scatter_plot()
pie_chart()
histogram()
stack_plot()
create_subplots()
generate_report()
```

------------------------------------------------------------------------

## CSV Data

The project uses sales data with columns such as:

``` text
Date
Product
Region
Sales
Profit
Quantity
```

Example:

``` csv
Date,Product,Region,Sales,Profit,Quantity
2026-01-01,Laptop,North,75000,15000,5
2026-01-02,Mobile,South,45000,9000,10
2026-01-03,Tablet,East,30000,6000,8
2026-01-04,Laptop,West,82000,18000,6
2026-01-05,Mobile,North,50000,11000,12
2026-01-06,Tablet,South,28000,5500,7
2026-01-07,Laptop,East,90000,21000,7
2026-01-08,Mobile,West,47000,9500,11
2026-01-09,Tablet,North,32000,7000,9
2026-01-10,Laptop,South,78000,16000,5
```

------------------------------------------------------------------------

## CSV File Path

The program can automatically create and use the CSV file.

The path is generated using:

``` python
csv_path = os.path.join(
    os.getcwd(),
    "sales_data.csv"
)
```

Therefore, the CSV file is stored in the current project directory.

Example:

``` text
Pandas_Analyzer/sales_data.csv
```

The program also prints the complete CSV path when the file is created.

------------------------------------------------------------------------

## Installation

Make sure Python is installed on your computer.

Install the required packages:

``` bash
pip install pandas numpy matplotlib seaborn jupyter
```

Or install them from `requirements.txt`:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## How to Run

Open a terminal in the project directory and run:

``` bash
python pandas_analyzer.py
```

The program will create/load the sales CSV data and display the main
menu.

------------------------------------------------------------------------

## Main Menu

The application provides the following options:

``` text
1. Explore Data
2. Clean Data
3. NumPy Array Operations
4. Mathematical Operations
5. Search Data
6. Sort Data
7. Filter Data
8. Aggregate Functions
9. Statistical Analysis
10. Create Pivot Table
11. Split Data
12. Data Visualization
13. Generate Report
14. Exit
```

------------------------------------------------------------------------

## Data Exploration

The **Explore Data** option displays:

-   First few records using `head()`
-   Dataset information using `info()`
-   Descriptive statistics using `describe()`
-   Missing-value information
-   Column data types

Example:

``` python
self.data.head()
self.data.info()
self.data.describe()
self.data.isnull().sum()
self.data.dtypes
```

------------------------------------------------------------------------

## Data Cleaning

The project performs basic data cleaning operations:

-   Removes duplicate records.
-   Converts the Date column to datetime.
-   Converts numeric columns to numeric data types.
-   Handles missing numeric values using the median.
-   Handles missing text values using `"Unknown"`.

------------------------------------------------------------------------

## NumPy Operations

The project converts numeric Pandas columns into NumPy arrays.

It demonstrates:

-   Array creation
-   Indexing
-   Slicing
-   Element-wise addition
-   Element-wise multiplication
-   Minimum and maximum values
-   Mean calculations

Example:

``` python
array = self.data["Sales"].to_numpy()

print(array[0])
print(array[:5])
print(array * 2)
print(array + 10)
```

------------------------------------------------------------------------

## Mathematical Operations

The project performs calculations such as:

-   Sum
-   Mean
-   Minimum
-   Maximum

Example:

``` python
np.sum(values)
np.mean(values)
np.min(values)
np.max(values)
```

------------------------------------------------------------------------

## Searching

Users can search for specific records by entering:

-   Column name
-   Search value

The search is case-insensitive and can find partial text matches.

------------------------------------------------------------------------

## Sorting

The user can select a column and sort the dataset in:

-   Ascending order
-   Descending order

Example:

``` python
self.data.sort_values(
    by=column,
    ascending=True
)
```

------------------------------------------------------------------------

## Filtering

The project allows users to filter records according to a selected
column and value.

For example:

``` text
Region = North
```

or

``` text
Product = Laptop
```

------------------------------------------------------------------------

## Aggregation

The project applies common aggregation functions:

-   `sum()`
-   `mean()`
-   `count()`
-   `min()`
-   `max()`

These functions can be used to understand overall sales, profit,
quantity, and other numeric values.

------------------------------------------------------------------------

## Statistical Analysis

The project calculates:

-   Standard deviation
-   Variance
-   25th percentile
-   50th percentile
-   75th percentile

NumPy functions used include:

``` python
np.std()
np.var()
np.percentile()
```

------------------------------------------------------------------------

## Pivot Table

A Pandas pivot table is created to summarize numeric data by region.

Example:

``` python
pd.pivot_table(
    self.data,
    values="Sales",
    index="Region",
    aggfunc=["sum", "mean", "count"]
)
```

This makes it easier to compare sales performance between regions.

------------------------------------------------------------------------

## Data Splitting

The project can split the DataFrame according to categories such as:

-   Region
-   Product

For example:

``` python
self.data.groupby("Region")
```

This allows separate groups of data to be analyzed.

------------------------------------------------------------------------

# Data Visualization

The visualization module uses **Matplotlib** and **Seaborn**.

The project supports:

### 1. Bar Chart

Used to compare sales or another numeric metric between products.

### 2. Line Chart

Used to show trends over dates or categories.

### 3. Scatter Plot

Used to examine the relationship between two numeric columns.

### 4. Pie Chart

Used to show the proportional distribution of a numeric metric by
product.

### 5. Histogram

Used to understand the distribution of numeric values.

### 6. Stack Plot / Stacked Chart

Used to compare products across different regions.

### 7. Subplots

Multiple visualizations are displayed in a single figure.

------------------------------------------------------------------------

## Saving Visualizations

Generated charts are automatically saved in:

``` text
visualizations/
```

Example files:

``` text
bar_chart.png
line_chart.png
scatter_plot.png
pie_chart.png
histogram.png
stack_plot.png
subplots.png
```

Charts are saved with high resolution for reporting purposes.

------------------------------------------------------------------------

## Program Flow

``` text
Start
  |
  v
Create / Load CSV Data
  |
  v
Create SalesDataAnalyzer Object
  |
  v
Load Data
  |
  v
Clean Data
  |
  v
Display Main Menu
  |
  +--> Explore Data
  |
  +--> NumPy Operations
  |
  +--> Mathematical Operations
  |
  +--> Search / Sort / Filter
  |
  +--> Aggregation
  |
  +--> Statistical Analysis
  |
  +--> Pivot Table
  |
  +--> Split Data
  |
  +--> Visualization
  |
  +--> Generate Report
  |
  v
Exit
```

------------------------------------------------------------------------

## Object-Oriented Programming Concepts

The project demonstrates several OOP concepts.

### Class

``` python
class SalesDataAnalyzer:
```

### Constructor

``` python
def __init__(self, file_path=None):
```

### Destructor

``` python
def __del__(self):
```

### Encapsulation

All major data analysis functionality is organized inside the
`SalesDataAnalyzer` class.

### Methods

The class contains separate methods for loading, cleaning, analyzing,
and visualizing data.

### Inheritance

Inheritance can be added later if the project is extended with
specialized analyzer classes.

### `super()`

If inheritance is implemented in an extended version, `super()` can be
used to call parent-class methods.

### Operator Overloading

Operator overloading can optionally be added to provide custom behavior
for analyzer objects.

------------------------------------------------------------------------

## Error Handling

The project handles common errors such as:

-   Missing CSV file
-   Empty CSV file
-   Invalid CSV format
-   Invalid column names
-   Missing numeric columns
-   Invalid menu choices

Example:

``` python
try:
    self.data = pd.read_csv(file_path)
except FileNotFoundError:
    print("File not found.")
except pd.errors.EmptyDataError:
    print("CSV file is empty.")
except pd.errors.ParserError:
    print("Unable to parse CSV file.")
```

------------------------------------------------------------------------

## Features

-   CSV data input
-   Automatic CSV path
-   Pandas DataFrame analysis
-   NumPy array operations
-   Data cleaning
-   Data searching
-   Data sorting
-   Data filtering
-   Aggregation
-   Statistical analysis
-   Pivot tables
-   Data splitting
-   Multiple visualizations
-   Visualization export
-   Automatic report generation
-   OOP implementation
-   Menu-driven interface
-   Error handling

------------------------------------------------------------------------

## Learning Outcomes

After completing this project, a student can understand:

-   How to work with CSV files in Python.
-   How to use Pandas DataFrames.
-   How to clean real-world datasets.
-   How to use NumPy arrays.
-   How indexing and slicing work.
-   How to perform mathematical calculations.
-   How to search, sort, and filter data.
-   How to calculate descriptive statistics.
-   How to create pivot tables.
-   How to visualize data using Matplotlib and Seaborn.
-   How to save charts as image files.
-   How to structure a Python project using OOP.
-   How to build a menu-driven data-analysis application.

------------------------------------------------------------------------

## Future Improvements

Possible future enhancements include:

-   Add a graphical user interface using Tkinter.
-   Support Excel files.
-   Add interactive Plotly charts.
-   Add date-range filtering.
-   Add advanced correlation analysis.
-   Add automated PDF reports.
-   Add database support.
-   Add more visualization types.
-   Add user authentication.
-   Add dashboard functionality.

------------------------------------------------------------------------

## Author

**Pandas Analyzer & Data Visualization Project**

Developed as a Python data analysis and visualization project for
learning Pandas, NumPy, Matplotlib, Seaborn, and Object-Oriented
Programming.

------------------------------------------------------------------------

## License

This project is intended for educational and learning purposes.
