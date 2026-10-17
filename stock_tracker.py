
import csv
from datetime import datetime

# Predefined stock prices (sample prices in USD)
stock_prices = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 175.00,
    "MSFT": 420.00,
    "AMZN": 190.00,
    "NVDA": 135.00
}

portfolio = []

def display_stocks():
    print("\n========== AVAILABLE STOCKS ==========")
    print(f"{'Symbol':<12}{'Price (USD)':>15}")
    print("-" * 27)

    for symbol, price in stock_prices.items():
        print(f"{symbol:<12}${price:>14.2f}")

def add_stock():
    symbol = input("\nEnter stock symbol: ").strip().upper()

    if symbol not in stock_prices:
        print("Stock not found. Please choose an available symbol.")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

    except ValueError:
        print("Invalid quantity. Please enter a whole number.")
        return

    price = stock_prices[symbol]
    value = price * quantity

    portfolio.append({
        "symbol": symbol,
        "quantity": quantity,
        "price": price,
        "value": value
    })

    print(f"{quantity} shares of {symbol} added successfully.")
    print(f"Investment value: ${value:,.2f}")

def view_portfolio():
    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    total_investment = sum(item["value"] for item in portfolio)

    print("\n================ YOUR PORTFOLIO ================")
    print(f"{'Symbol':<10}{'Quantity':>10}{'Price':>12}{'Value':>15}")
    print("-" * 47)

    for item in portfolio:
        print(
            f"{item['symbol']:<10}"
            f"{item['quantity']:>10}"
            f"${item['price']:>11.2f}"
            f"${item['value']:>14,.2f}"
        )

    print("-" * 47)
    print(f"{'TOTAL INVESTMENT:':<32}${total_investment:,.2f}")

def save_report():
    if not portfolio:
        print("\nNothing to save. Add a stock first.")
        return

    filename = "portfolio_report.csv"

    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Stock Symbol",
                "Quantity",
                "Price (USD)",
                "Investment Value (USD)"
            ])

            for item in portfolio:
                writer.writerow([
                    item["symbol"],
                    item["quantity"],
                    f"{item['price']:.2f}",
                    f"{item['value']:.2f}"
                ])

            total = sum(item["value"] for item in portfolio)
            writer.writerow([])
            writer.writerow(["TOTAL INVESTMENT", "", "", f"{total:.2f}"])
            writer.writerow([
                "Report Generated",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ])

        print(f"\nReport saved successfully as {filename}.")

    except OSError as error:
        print(f"Could not save report: {error}")

def main():
    while True:
        print("\n====================================")
        print("     SMART STOCK PORTFOLIO TRACKER")
        print("====================================")
        print("1. View available stocks")
        print("2. Add stock to portfolio")
        print("3. View portfolio")
        print("4. Save portfolio report")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            display_stocks()
        elif choice == "2":
            add_stock()
        elif choice == "3":
            view_portfolio()
        elif choice == "4":
            save_report()
        elif choice == "5":
            print("Thank you for using Stock Portfolio Tracker!")
            break
        else:
            print("Invalid option. Please choose from 1 to 5.")

if __name__ == "__main__":
    main()
