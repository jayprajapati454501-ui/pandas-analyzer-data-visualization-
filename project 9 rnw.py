import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:
    """
    Pandas Analyzer & Data Visualization Project

    This class provides functionality for:
    - Loading CSV data
    - Exploring and cleaning data
    - NumPy array operations
    - Mathematical operations
    - Searching, sorting and filtering
    - Statistical analysis
    - Aggregation
    - Pivot tables
    - Data visualization
    """

    def __init__(self, file_path=None):
        self.data = pd.DataFrame()

        if file_path:
            self.load_data(file_path)

    def __del__(self):
        """Destructor."""
        pass

    # ---------------------------------------------------------
    # LOAD DATA
    # ---------------------------------------------------------

    def load_data(self, file_path):
        """Load sales data from CSV file."""

        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(
                    f"File not found: {file_path}"
                )

            self.data = pd.read_csv(file_path)

            print("\nData loaded successfully!")
            print(f"Rows: {self.data.shape[0]}")
            print(f"Columns: {self.data.shape[1]}")

            self.clean_data()

        except FileNotFoundError as error:
            print(f"\nError: {error}")

        except pd.errors.EmptyDataError:
            print("\nError: CSV file is empty.")

        except pd.errors.ParserError:
            print("\nError: Unable to parse CSV file.")

        except Exception as error:
            print(f"\nUnexpected error: {error}")

    # ---------------------------------------------------------
    # EXPLORE DATA
    # ---------------------------------------------------------

    def explore_data(self):
        """Display basic information about the dataset."""

        if self.data.empty:
            print("\nNo data available.")
            return

        print("\n========== DATA PREVIEW ==========")
        print(self.data.head())

        print("\n========== DATA INFO ==========")
        print(self.data.info())

        print("\n========== STATISTICS ==========")
        print(self.data.describe(include="all"))

        print("\n========== MISSING VALUES ==========")
        print(self.data.isnull().sum())

        print("\n========== DATA TYPES ==========")
        print(self.data.dtypes)

    # ---------------------------------------------------------
    # CLEAN DATA
    # ---------------------------------------------------------

    def clean_data(self):
        """Clean missing values and convert data types."""

        if self.data.empty:
            return

        # Remove duplicate records
        self.data.drop_duplicates(inplace=True)

        # Convert Date column if available
        if "Date" in self.data.columns:
            self.data["Date"] = pd.to_datetime(
                self.data["Date"],
                errors="coerce"
            )

        # Convert numeric columns
        numeric_columns = [
            "Sales",
            "Revenue",
            "Profit",
            "Quantity",
            "Unit_Price",
            "Cost"
        ]

        for column in numeric_columns:
            if column in self.data.columns:
                self.data[column] = pd.to_numeric(
                    self.data[column],
                    errors="coerce"
                )

        # Fill numeric missing values with median
        numeric_cols = self.data.select_dtypes(
            include=np.number
        ).columns

        for column in numeric_cols:
            self.data[column] = self.data[column].fillna(
                self.data[column].median()
            )

        # Fill text missing values
        text_cols = self.data.select_dtypes(
            exclude=np.number
        ).columns

        for column in text_cols:
            self.data[column] = self.data[column].fillna("Unknown")

        print("\nData cleaning completed.")

    # ---------------------------------------------------------
    # NUMPY ARRAY
    # ---------------------------------------------------------

    def numpy_operations(self):
        """Demonstrate NumPy conversion, indexing and slicing."""

        if self.data.empty:
            print("\nNo data available.")
            return

        numeric_data = self.data.select_dtypes(
            include=np.number
        )

        if numeric_data.empty:
            print("\nNo numeric columns found.")
            return

        column = numeric_data.columns[0]

        array = numeric_data[column].to_numpy()

        print("\n========== NUMPY ARRAY ==========")
        print(array)

        print("\nFirst value:")
        print(array[0])

        print("\nFirst five values:")
        print(array[:5])

        print("\nLast five values:")
        print(array[-5:])

        print("\nElement-wise multiplication by 2:")
        print(array * 2)

        print("\nElement-wise addition by 10:")
        print(array + 10)

    # ---------------------------------------------------------
    # MATHEMATICAL OPERATIONS
    # ---------------------------------------------------------

    def mathematical_operations(self):
        """Perform mathematical calculations."""

        if self.data.empty:
            print("\nNo data available.")
            return

        numeric_columns = self.data.select_dtypes(
            include=np.number
        ).columns

        print("\n========== MATHEMATICAL OPERATIONS ==========")

        for column in numeric_columns:
            values = self.data[column].dropna().to_numpy()

            if len(values) == 0:
                continue

            print(f"\nColumn: {column}")
            print(f"Sum: {np.sum(values):.2f}")
            print(f"Mean: {np.mean(values):.2f}")
            print(f"Minimum: {np.min(values):.2f}")
            print(f"Maximum: {np.max(values):.2f}")

    # ---------------------------------------------------------
    # COMBINE DATA
    # ---------------------------------------------------------

    def combine_data(self, other_dataframe):
        """Combine another DataFrame with current data."""

        if not isinstance(other_dataframe, pd.DataFrame):
            print("\nInvalid DataFrame.")
            return

        self.data = pd.concat(
            [self.data, other_dataframe],
            ignore_index=True
        )

        print("\nDataFrames combined successfully.")

    # ---------------------------------------------------------
    # SPLIT DATA
    # ---------------------------------------------------------

    def split_data(self):
        """Split data by Region or Product."""

        if self.data.empty:
            print("\nNo data available.")
            return

        if "Region" in self.data.columns:
            groups = dict(tuple(self.data.groupby("Region")))

            print("\n========== DATA SPLIT BY REGION ==========")

            for region, dataframe in groups.items():
                print(
                    f"{region}: {len(dataframe)} records"
                )

        elif "Product" in self.data.columns:
            groups = dict(tuple(self.data.groupby("Product")))

            print("\n========== DATA SPLIT BY PRODUCT ==========")

            for product, dataframe in groups.items():
                print(
                    f"{product}: {len(dataframe)} records"
                )

        else:
            print(
                "\nRegion or Product column not found."
            )

    # ---------------------------------------------------------
    # SEARCH
    # ---------------------------------------------------------

    def search_data(self):
        """Search records by Product or Region."""

        if self.data.empty:
            print("\nNo data available.")
            return

        column = input(
            "\nEnter column name to search: "
        ).strip()

        if column not in self.data.columns:
            print("\nColumn not found.")
            return

        value = input(
            "Enter search value: "
        ).strip()

        result = self.data[
            self.data[column].astype(str).str.contains(
                value,
                case=False,
                na=False
            )
        ]

        print("\n========== SEARCH RESULT ==========")

        if result.empty:
            print("No matching records found.")
        else:
            print(result.to_string(index=False))

    # ---------------------------------------------------------
    # SORT
    # ---------------------------------------------------------

    def sort_data(self):
        """Sort data using a selected column."""

        if self.data.empty:
            print("\nNo data available.")
            return

        column = input(
            "\nEnter column name for sorting: "
        ).strip()

        if column not in self.data.columns:
            print("\nColumn not found.")
            return

        order = input(
            "Sort descending? (y/n): "
        ).lower()

        descending = order == "y"

        result = self.data.sort_values(
            by=column,
            ascending=not descending
        )

        print("\n========== SORTED DATA ==========")
        print(result.head(20).to_string(index=False))

    # ---------------------------------------------------------
    # FILTER
    # ---------------------------------------------------------

    def filter_data(self):
        """Filter data using a user-selected value."""

        if self.data.empty:
            print("\nNo data available.")
            return

        column = input(
            "\nEnter column name for filtering: "
        ).strip()

        if column not in self.data.columns:
            print("\nColumn not found.")
            return

        value = input(
            "Enter value: "
        ).strip()

        result = self.data[
            self.data[column].astype(str).str.contains(
                value,
                case=False,
                na=False
            )
        ]

        print("\n========== FILTERED DATA ==========")

        if result.empty:
            print("No matching records.")
        else:
            print(result.to_string(index=False))

    # ---------------------------------------------------------
    # AGGREGATE FUNCTIONS
    # ---------------------------------------------------------

    def aggregate_functions(self):
        """Apply sum, mean, count, minimum and maximum."""

        if self.data.empty:
            print("\nNo data available.")
            return

        numeric_columns = self.data.select_dtypes(
            include=np.number
        ).columns

        if len(numeric_columns) == 0:
            print("\nNo numeric columns found.")
            return

        print("\n========== AGGREGATE FUNCTIONS ==========")

        for column in numeric_columns:
            print(f"\nColumn: {column}")
            print(f"Sum   : {self.data[column].sum():.2f}")
            print(f"Mean  : {self.data[column].mean():.2f}")
            print(f"Count : {self.data[column].count()}")
            print(f"Min   : {self.data[column].min():.2f}")
            print(f"Max   : {self.data[column].max():.2f}")

    # ---------------------------------------------------------
    # STATISTICAL ANALYSIS
    # ---------------------------------------------------------

    def statistical_analysis(self):
        """Calculate standard deviation, variance and percentiles."""

        if self.data.empty:
            print("\nNo data available.")
            return

        numeric_columns = self.data.select_dtypes(
            include=np.number
        ).columns

        print("\n========== STATISTICAL ANALYSIS ==========")

        for column in numeric_columns:

            values = self.data[column].dropna().to_numpy()

            if len(values) == 0:
                continue

            print(f"\nColumn: {column}")

            print(
                f"Standard Deviation: "
                f"{np.std(values):.2f}"
            )

            print(
                f"Variance: "
                f"{np.var(values):.2f}"
            )

            print(
                f"25th Percentile: "
                f"{np.percentile(values, 25):.2f}"
            )

            print(
                f"50th Percentile: "
                f"{np.percentile(values, 50):.2f}"
            )

            print(
                f"75th Percentile: "
                f"{np.percentile(values, 75):.2f}"
            )

    # ---------------------------------------------------------
    # PIVOT TABLE
    # ---------------------------------------------------------

    def create_pivot_table(self):
        """Create a pivot table for sales analysis."""

        if self.data.empty:
            print("\nNo data available.")
            return

        if "Region" not in self.data.columns:
            print("\nRegion column not available.")
            return

        numeric_column = None

        for column in ["Sales", "Revenue", "Profit"]:
            if column in self.data.columns:
                numeric_column = column
                break

        if numeric_column is None:
            print("\nNo Sales, Revenue or Profit column.")
            return

        pivot = pd.pivot_table(
            self.data,
            values=numeric_column,
            index="Region",
            aggfunc=["sum", "mean", "count"]
        )

        print("\n========== PIVOT TABLE ==========")
        print(pivot)

    # ---------------------------------------------------------
    # VISUALIZATION
    # ---------------------------------------------------------

    def visualize_data(self):
        """Display visualization menu."""

        if self.data.empty:
            print("\nNo data available.")
            return

        while True:

            print("\n========== VISUALIZATION MENU ==========")
            print("1. Bar Chart")
            print("2. Line Chart")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Stack Plot")
            print("7. Subplots")
            print("8. Exit Visualization Menu")

            choice = input(
                "\nEnter your choice: "
            ).strip()

            if choice == "1":
                self.bar_chart()

            elif choice == "2":
                self.line_chart()

            elif choice == "3":
                self.scatter_plot()

            elif choice == "4":
                self.pie_chart()

            elif choice == "5":
                self.histogram()

            elif choice == "6":
                self.stack_plot()

            elif choice == "7":
                self.create_subplots()

            elif choice == "8":
                break

            else:
                print("\nInvalid choice.")

    # ---------------------------------------------------------
    # BAR CHART
    # ---------------------------------------------------------

    def bar_chart(self):

        if "Product" not in self.data.columns:
            print("\nProduct column not found.")
            return

        numeric_column = self.get_numeric_column()

        if numeric_column is None:
            return

        grouped = self.data.groupby(
            "Product"
        )[numeric_column].sum()

        plt.figure(figsize=(10, 6))
        grouped.plot(kind="bar")

        plt.title(
            f"{numeric_column} by Product"
        )
        plt.xlabel("Product")
        plt.ylabel(numeric_column)
        plt.xticks(rotation=45)
        plt.tight_layout()

        self.save_plot("bar_chart.png")
        plt.show()

    # ---------------------------------------------------------
    # LINE CHART
    # ---------------------------------------------------------

    def line_chart(self):

        numeric_column = self.get_numeric_column()

        if numeric_column is None:
            return

        if "Date" in self.data.columns:

            grouped = self.data.groupby(
                "Date"
            )[numeric_column].sum()

            grouped = grouped.sort_index()

            plt.figure(figsize=(10, 6))
            plt.plot(
                grouped.index,
                grouped.values,
                marker="o"
            )

            plt.title(
                f"{numeric_column} Trend"
            )
            plt.xlabel("Date")
            plt.ylabel(numeric_column)

        elif "Product" in self.data.columns:

            grouped = self.data.groupby(
                "Product"
            )[numeric_column].sum()

            plt.figure(figsize=(10, 6))
            plt.plot(
                grouped.index,
                grouped.values,
                marker="o"
            )

            plt.title(
                f"{numeric_column} by Product"
            )
            plt.xlabel("Product")
            plt.ylabel(numeric_column)

        else:
            print("\nSuitable column not found.")
            return

        plt.xticks(rotation=45)
        plt.tight_layout()

        self.save_plot("line_chart.png")
        plt.show()

    # ---------------------------------------------------------
    # SCATTER PLOT
    # ---------------------------------------------------------

    def scatter_plot(self):

        numeric_columns = self.data.select_dtypes(
            include=np.number
        ).columns

        if len(numeric_columns) < 2:
            print(
                "\nAt least two numeric columns required."
            )
            return

        x_column = numeric_columns[0]
        y_column = numeric_columns[1]

        plt.figure(figsize=(10, 6))

        sns.scatterplot(
            data=self.data,
            x=x_column,
            y=y_column
        )

        plt.title(
            f"{x_column} vs {y_column}"
        )
        plt.tight_layout()

        self.save_plot("scatter_plot.png")
        plt.show()

    # ---------------------------------------------------------
    # PIE CHART
    # ---------------------------------------------------------

    def pie_chart(self):

        if "Product" not in self.data.columns:
            print("\nProduct column not found.")
            return

        numeric_column = self.get_numeric_column()

        if numeric_column is None:
            return

        grouped = self.data.groupby(
            "Product"
        )[numeric_column].sum()

        plt.figure(figsize=(8, 8))

        plt.pie(
            grouped.values,
            labels=grouped.index,
            autopct="%1.1f%%"
        )

        plt.title(
            f"{numeric_column} Distribution by Product"
        )

        self.save_plot("pie_chart.png")
        plt.show()

    # ---------------------------------------------------------
    # HISTOGRAM
    # ---------------------------------------------------------

    def histogram(self):

        numeric_column = self.get_numeric_column()

        if numeric_column is None:
            return

        plt.figure(figsize=(10, 6))

        plt.hist(
            self.data[numeric_column].dropna(),
            bins=10
        )

        plt.title(
            f"{numeric_column} Distribution"
        )
        plt.xlabel(numeric_column)
        plt.ylabel("Frequency")

        plt.tight_layout()

        self.save_plot("histogram.png")
        plt.show()

    # ---------------------------------------------------------
    # STACK PLOT
    # ---------------------------------------------------------

    def stack_plot(self):

        if "Region" not in self.data.columns:
            print("\nRegion column not found.")
            return

        if "Product" not in self.data.columns:
            print("\nProduct column not found.")
            return

        numeric_column = self.get_numeric_column()

        if numeric_column is None:
            return

        pivot = pd.pivot_table(
            self.data,
            values=numeric_column,
            index="Region",
            columns="Product",
            aggfunc="sum",
            fill_value=0
        )

        plt.figure(figsize=(10, 6))

        pivot.plot(
            kind="bar",
            stacked=True,
            figsize=(10, 6)
        )

        plt.title(
            f"Stacked {numeric_column} by Region and Product"
        )
        plt.xlabel("Region")
        plt.ylabel(numeric_column)
        plt.xticks(rotation=45)
        plt.tight_layout()

        self.save_plot("stack_plot.png")
        plt.show()

    # ---------------------------------------------------------
    # SUBPLOTS
    # ---------------------------------------------------------

    def create_subplots(self):

        numeric_columns = self.data.select_dtypes(
            include=np.number
        ).columns

        if len(numeric_columns) == 0:
            print("\nNo numeric columns found.")
            return

        column = numeric_columns[0]

        fig, axes = plt.subplots(
            2,
            2,
            figsize=(12, 9)
        )

        # Histogram
        axes[0, 0].hist(
            self.data[column].dropna(),
            bins=10
        )
        axes[0, 0].set_title(
            f"{column} Histogram"
        )

        # Boxplot
        axes[0, 1].boxplot(
            self.data[column].dropna()
        )
        axes[0, 1].set_title(
            f"{column} Boxplot"
        )

        # Line
        axes[1, 0].plot(
            self.data[column].reset_index(drop=True)
        )
        axes[1, 0].set_title(
            f"{column} Line Chart"
        )

        # Area
        axes[1, 1].plot(
            self.data[column].reset_index(drop=True)
        )
        axes[1, 1].fill_between(
            range(len(self.data)),
            self.data[column].reset_index(drop=True),
            alpha=0.3
        )
        axes[1, 1].set_title(
            f"{column} Area Chart"
        )

        plt.tight_layout()

        self.save_plot("subplots.png")
        plt.show()

    # ---------------------------------------------------------
    # HELPER METHODS
    # ---------------------------------------------------------

    def get_numeric_column(self):

        numeric_columns = self.data.select_dtypes(
            include=np.number
        ).columns

        if len(numeric_columns) == 0:
            print("\nNo numeric columns found.")
            return None

        # Prefer Sales, Revenue or Profit
        for column in [
            "Sales",
            "Revenue",
            "Profit"
        ]:
            if column in numeric_columns:
                return column

        return numeric_columns[0]

    def save_plot(self, filename):

        os.makedirs(
            "visualizations",
            exist_ok=True
        )

        path = os.path.join(
            "visualizations",
            filename
        )

        plt.savefig(
            path,
            dpi=300,
            bbox_inches="tight"
        )

        print(
            f"\nVisualization saved: {path}"
        )

    # ---------------------------------------------------------
    # REPORT
    # ---------------------------------------------------------

    def generate_report(self):

        if self.data.empty:
            print("\nNo data available.")
            return

        print("\n")
        print("=" * 60)
        print("       PANDAS SALES DATA ANALYZER REPORT")
        print("=" * 60)

        print(
            f"\nTotal Records: {len(self.data)}"
        )

        print(
            f"Total Columns: {len(self.data.columns)}"
        )

        print(
            f"Duplicate Records: "
            f"{self.data.duplicated().sum()}"
        )

        print("\nColumns:")
        print(", ".join(self.data.columns))

        numeric_columns = self.data.select_dtypes(
            include=np.number
        ).columns

        for column in numeric_columns:

            print(f"\n{column}:")

            print(
                f"  Total: "
                f"{self.data[column].sum():.2f}"
            )

            print(
                f"  Average: "
                f"{self.data[column].mean():.2f}"
            )

            print(
                f"  Maximum: "
                f"{self.data[column].max():.2f}"
            )

            print(
                f"  Minimum: "
                f"{self.data[column].min():.2f}"
            )

        if "Product" in self.data.columns:
            print("\nProduct Summary:")

            print(
                self.data["Product"]
                .value_counts()
                .to_string()
            )

        if "Region" in self.data.columns:
            print("\nRegion Summary:")

            print(
                self.data["Region"]
                .value_counts()
                .to_string()
            )

        print("\n" + "=" * 60)


# =============================================================
# MAIN MENU
# =============================================================

def main():

    print("=" * 60)
    print("       PANDAS ANALYZER & DATA VISUALIZATION")
    print("=" * 60)

    file_path = input(
        "\nEnter CSV file path: "
    ).strip()

    analyzer = SalesDataAnalyzer()

    analyzer.load_data(file_path)

    if analyzer.data.empty:
        print(
            "\nProgram stopped because no data was loaded."
        )
        return

    while True:

        print("\n")
        print("=" * 50)
        print("              MAIN MENU")
        print("=" * 50)

        print("1. Explore Data")
        print("2. Clean Data")
        print("3. NumPy Array Operations")
        print("4. Mathematical Operations")
        print("5. Search Data")
        print("6. Sort Data")
        print("7. Filter Data")
        print("8. Aggregate Functions")
        print("9. Statistical Analysis")
        print("10. Create Pivot Table")
        print("11. Split Data")
        print("12. Data Visualization")
        print("13. Generate Report")
        print("14. Exit")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":
            analyzer.explore_data()

        elif choice == "2":
            analyzer.clean_data()

        elif choice == "3":
            analyzer.numpy_operations()

        elif choice == "4":
            analyzer.mathematical_operations()

        elif choice == "5":
            analyzer.search_data()

        elif choice == "6":
            analyzer.sort_data()

        elif choice == "7":
            analyzer.filter_data()

        elif choice == "8":
            analyzer.aggregate_functions()

        elif choice == "9":
            analyzer.statistical_analysis()

        elif choice == "10":
            analyzer.create_pivot_table()

        elif choice == "11":
            analyzer.split_data()

        elif choice == "12":
            analyzer.visualize_data()

        elif choice == "13":
            analyzer.generate_report()

        elif choice == "14":
            print(
                "\nThank you for using Pandas Analyzer!"
            )
            break

        else:
            print(
                "\nInvalid choice. Please try again."
            )


if __name__ == "__main__":
    main()
    