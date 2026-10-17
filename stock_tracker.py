import csv
from datetime import datetime

# স্টকের প্রিসেট প্রাইস তালিকা
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 175.00,
    "MSFT": 420.00,
    "AMZN": 190.00,
    "NVDA": 135.00
}

def display_stocks():
    print("\n========== AVAILABLE STOCKS ==========")
    print(f"{'Symbol':<12}{'Price (USD)':>15}")
    print("-" * 27)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<12}${price:>14.2f}")

def add_stock(portfolio):
    symbol = input("\nEnter stock symbol: ").strip().upper()

    if symbol not in STOCK_PRICES:
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

    # একই স্টক পুনরায় যোগ করলে কোয়ান্টিটি আপডেট হবে
    portfolio[symbol] = portfolio.get(symbol, 0) + quantity
    
    current_qty = portfolio[symbol]
    total_val = current_qty * STOCK_PRICES[symbol]
    print(f"\nSuccessfully updated {symbol}.")
    print(f"Total Shares: {current_qty} | Total Holding Value: ${total_val:,.2f}")

def view_portfolio(portfolio):
    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    print("\n================ YOUR PORTFOLIO ================")
    print(f"{'Symbol':<10}{'Quantity':>10}{'Price':>12}{'Value':>15}")
    print("-" * 47)

    total_investment = 0.0
    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total_investment += value
        print(f"{symbol:<10}{qty:>10}${price:>11.2f}${value:>14,.2f}")

    print("-" * 47)
    print(f"{'TOTAL INVESTMENT:':<32}${total_investment:,.2f}")

def save_report(portfolio):
    if not portfolio:
        print("\nNothing to save. Add a stock first.")
        return

    filename = "portfolio_report.csv"

    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow(["Stock Symbol", "Quantity", "Price (USD)", "Investment Value (USD)"])

            total_investment = 0.0
            for symbol, qty in portfolio.items():
                price = STOCK_PRICES[symbol]
                value = price * qty
                total_investment += value
                writer.writerow([symbol, qty, f"{price:.2f}", f"{value:.2f}"])

            writer.writerow([])
            writer.writerow(["TOTAL INVESTMENT", "", "", f"{total_investment:.2f}"])
            writer.writerow(["Report Generated", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

        print(f"\nReport saved successfully as {filename}.")

    except OSError as error:
        print(f"Could not save report: {error}")

def main():
    # গ্লোবালের বদলে লোকাল স্টেট
    portfolio = {}

    while True:
        print("\n====================================")
        print("     SMART STOCK PORTFOLIO TRACKER")
        print("====================================")
        print("1. View available stocks")
        print("2. Add/Update stock")
        print("3. View portfolio")
        print("4. Save portfolio report")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            display_stocks()
        elif choice == "2":
            add_stock(portfolio)
        elif choice == "3":
            view_portfolio(portfolio)
        elif choice == "4":
            save_report(portfolio)
        elif choice == "5":
            print("Thank you for using Stock Portfolio Tracker!")
            break
        else:
            print("Invalid option. Please choose from 1 to 5.")

if __name__ == "__main__":
    main()
