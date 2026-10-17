# 📈 Smart Stock Portfolio Tracker

A Python-based stock portfolio management application that allows users to manage stock holdings, calculate investment values using predefined stock prices, view portfolio summaries, and export investment reports to CSV files.

## ✨ Features

- **Stock Price Listing:** View available stock symbols and their predefined prices.
- **Add or Update Stocks:** Add stock quantities to your portfolio.
- **Automatic Quantity Update:** Adding the same stock again increases its existing quantity.
- **Investment Calculation:** Calculate the value of individual stock holdings and total investment.
- **Portfolio Summary:** Display stock symbols, quantities, prices, and investment values.
- **CSV Report Export:** Export portfolio details and total investment to a CSV file.
- **Input Validation:** Handle invalid stock symbols and quantities.
- **Error Handling:** Display helpful messages when invalid input is provided or a report cannot be saved.
- **Menu-Driven Interface:** Navigate through the application using a simple console menu.

## 🛠️ Technologies Used

- Python 3
- `csv` module
- `datetime` module
- Dictionaries
- Functions
- Loops and conditional statements
- Exception handling
- File handling

## 📊 Available Stocks

| Stock Symbol | Price (USD) |
|---|---:|
| AAPL | $180.00 |
| TSLA | $250.00 |
| GOOGL | $175.00 |
| MSFT | $420.00 |
| AMZN | $190.00 |
| NVDA | $135.00 |

**Note:** These are predefined sample prices, not real-time stock market prices.

## 📂 Project Structure

```text
Python_Stock_Portfolio_Tracker/
├── stock_tracker.py
├── README.md
└── portfolio_report.csv
```

The `portfolio_report.csv` file is generated when a user saves a portfolio report. It may not exist until the report is generated.

## 🚀 Getting Started

### Prerequisites

- Python 3 installed on your computer.
- A code editor such as Visual Studio Code.

No external Python packages are required.

### Installation and Execution

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Open the integrated terminal.
4. Run the following command:

```bash
python stock_tracker.py
```

## 💻 How to Use

When the application starts, a menu appears:

```text
SMART STOCK PORTFOLIO TRACKER

1. View available stocks
2. Add/Update stock
3. View portfolio
4. Save portfolio report
5. Exit
```

- **Option 1:** Display available stocks and prices.
- **Option 2:** Enter a stock symbol and quantity to add shares.
- **Option 3:** View the portfolio and total investment value.
- **Option 4:** Export the current portfolio to `portfolio_report.csv`.
- **Option 5:** Exit the application.

## 🧮 Example

If a user adds 5 shares of AAPL at $180.00 per share:

```text
Stock Symbol: AAPL
Quantity: 5
Price per Share: $180.00
Investment Value: $900.00
```

**Calculation:**

```text
Total Investment = Quantity × Price per Share
                 = 5 × 180
                 = $900.00
```

If the user adds 3 more AAPL shares, the portfolio quantity becomes 8 shares.

## 📄 CSV Report

The exported report contains:

- Stock Symbol
- Quantity
- Price (USD)
- Investment Value (USD)
- Total Investment
- Report Generation Timestamp

The report can be opened using Microsoft Excel, Google Sheets, or other spreadsheet applications.

## ⚠️ Limitations

- Stock prices are predefined sample values and are not updated automatically.
- The application does not retrieve live stock market data.
- Portfolio data is stored in memory and resets when the program restarts.
- CSV export saves the current portfolio but does not automatically restore a previously saved portfolio.

## 🎯 Learning Outcomes

This project demonstrates practical use of Python dictionaries, functions, input validation, arithmetic operations, exception handling, and CSV file handling.

## 👩‍💻 Author

Developed as a personal Python programming project to practice programming fundamentals, data management, and file handling.
