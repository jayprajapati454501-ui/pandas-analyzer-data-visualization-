def create_csv_file():
    """Create sales_data.csv with sample sales data."""

    data = {
        "Date": [
            "2026-01-01",
            "2026-01-02",
            "2026-01-03",
            "2026-01-04",
            "2026-01-05",
            "2026-01-06",
            "2026-01-07",
            "2026-01-08",
            "2026-01-09",
            "2026-01-10"
        ],

        "Product": [
            "Laptop",
            "Mobile",
            "Tablet",
            "Laptop",
            "Mobile",
            "Tablet",
            "Laptop",
            "Mobile",
            "Tablet",
            "Laptop"
        ],

        "Region": [
            "North",
            "South",
            "East",
            "West",
            "North",
            "South",
            "East",
            "West",
            "North",
            "South"
        ],

        "Sales": [
            75000,
            45000,
            30000,
            82000,
            50000,
            28000,
            90000,
            47000,
            32000,
            78000
        ],

        "Profit": [
            15000,
            9000,
            6000,
            18000,
            11000,
            5500,
            21000,
            9500,
            7000,
            16000
        ],

        "Quantity": [
            5,
            10,
            8,
            6,
            12,
            7,
            7,
            11,
            9,
            5
        ]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # CSV path
    csv_path = os.path.join(
        os.getcwd(),
        "sales_data.csv"
    )

    # Save DataFrame as CSV
    df.to_csv(
        csv_path,
        index=False
    )

    print("\nCSV file created successfully!")
    print("CSV File Path:")
    print(csv_path)

    return csv_path


def main():

    print("=" * 60)
    print("       PANDAS ANALYZER & DATA VISUALIZATION")
    print("=" * 60)

    # Automatically create CSV and get its path
    file_path = create_csv_file()

    # Create analyzer
    analyzer = SalesDataAnalyzer()

    # Load CSV using automatically generated path
    analyzer.load_data(file_path)

    if analyzer.data.empty:
        print("\nProgram stopped because no data was loaded.")
        return

    while True:

        print("\n" + "=" * 50)
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

        choice = input("\nEnter your choice: ").strip()

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
            print("\nThank you for using Pandas Analyzer!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()