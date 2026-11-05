# Personal Finance Tracker

A Python-based command-line application that helps users manage their income and expenses, analyze spending patterns, and visualize their financial data.

## Features

- Add income transactions.
- Add expense transactions.
- View complete transaction history.
- Calculate total income, expenses, and balance.
- Analyze expenses by category.
- Search expenses using a specified amount threshold.
- Check data quality, including missing values and potential duplicate transactions.
- Visualize expenses using bar charts and pie charts.
- Compare total income and expenses graphically.

## Technologies Used

- **Python** – Core programming language.
- **Pandas** – Data manipulation and analysis.
- **Matplotlib** – Data visualization.
- **CSV** – Transaction data storage.

## Project Structure

```text
Personal_Finance_Tracker/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

The `transaction.csv` file is automatically generated when the application runs for the first time.

## Constants Used Throughout the Application

- `FIELDNAMES`: Defines the column names used in the transaction CSV file.
- `CSV_FILE`: Stores the CSV filename used for transaction storage.

## Functions Used in the Application

- `initialize_csv()`: Creates the transaction CSV file with column headers if it does not exist.
- `add_transaction(transaction_type)`: Adds income or expense transactions after validating user input.
- `calculate_totals(df)`: Calculates and returns total income and total expenses.
- `main()`: Controls the application menu and handles user selections.

## Data Storage

All transactions are stored in a CSV file named `transaction.csv`.

The CSV file contains the following columns:

| Column | Description |
|---|---|
| Type | Income or Expense |
| Amount | Transaction amount |
| Category | Transaction category |
| Description | Optional transaction description |

The application automatically creates the CSV file if it does not exist.

## Installation and Setup

**1. Navigate to the project directory**

```bash
cd Personal_Finance_Tracker
```

**2. Install the required libraries**

```bash
pip install -r requirements.txt
```

## How to Run

Execute the following command in your terminal:

```bash
python main.py
```

Follow the displayed menu to select the required operation.

## Data Visualization

The application provides visual representations of financial data, including:

- Expense distribution by category.
- Category-wise expense comparison.
- Income versus expense comparison.

## Future Improvements

- Add transaction dates.
- Generate monthly and yearly financial reports.
- Implement budget tracking.
- Develop a graphical user interface.

## Author

[@mohdtusi](https://github.com/mohdtusi)

## License

This project is available for educational and personal use.