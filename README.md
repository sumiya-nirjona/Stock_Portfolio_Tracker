
# 📈 Smart Stock Portfolio Tracker

A Python-based stock portfolio management application developed as part of the CodeAlpha Python Programming Internship (Task 2).

The application allows users to manage stock quantities, calculate investment values using predefined stock prices, view their portfolio, and export investment reports to CSV files.

## ✨ Features

- **Stock Price Listing:** View available stock symbols and their predefined prices.
- **Add or Update Stocks:** Add stock quantities to your portfolio.
- **Automatic Quantity Update:** Adding the same stock again increases its existing quantity.
- **Investment Calculation:** Calculate the total value of each stock holding.
- **Portfolio Summary:** Display stock symbols, quantities, prices, and investment values.
- **CSV Report Export:** Save portfolio details and total investment to a CSV file.
- **Input Validation:** Handle invalid stock symbols and quantities.
- **Error Handling:** Display an error message if the report cannot be saved.
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
CodeAlpha_Stock_Portfolio_Tracker/
│
├── stock_tracker.py
├── README.md
└── portfolio_report.csv
```

The `portfolio_report.csv` file is generated when the user saves a portfolio report.

## 🚀 Getting Started

### Prerequisites

- Python 3 installed on your computer.
- A code editor such as Visual Studio Code.

No external Python packages are required.

### Installation and Execution

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the integrated terminal.
4. Run the following command:

```bash
python stock_tracker.py
```

## 💻 How to Use

When the application starts, the following menu appears:

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
- **Option 4:** Export the portfolio to `portfolio_report.csv`.
- **Option 5:** Exit the application.

## 🧮 Example

If a user adds 5 shares of AAPL at $180.00 per share:

```text
Stock Symbol: AAPL
Quantity: 5
Price per Share: $180.00
Investment Value: $900.00
```

Calculation:

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

- Stock prices are predefined and manually maintained.
- The application does not retrieve live market data.
- Portfolio data is stored in memory and resets when the application restarts.
- CSV export saves the current portfolio; it does not automatically restore previously saved data.

## 🎯 Learning Outcomes

This project demonstrates practical use of Python dictionaries, functions, input validation, basic financial calculations, exception handling, and CSV file operations.

## 👩‍💻 Internship

**Program:** CodeAlpha Python Programming Internship  
**Project:** Task 2 — Stock Portfolio Tracker
