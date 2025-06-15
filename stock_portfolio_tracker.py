# stock_tracker.py

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 125,
    "MSFT": 320
}

# Get user input
portfolio = {}
print("Enter stock names and quantity (type 'done' to finish):")
while True:
    stock = input("Stock name: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in price list.")
        continue
    try:
        quantity = int(input("Quantity: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
total_value = 0
print("\n----- Portfolio Summary -----")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_value += investment
    print(f"{stock}: {quantity} x ${price} = ${investment}")

print(f"\nTotal Investment: ${total_value}")

# Optional: Save to a file
save = input("\nDo you want to save this summary to a file? (y/n): ").lower()
if save == 'y':
    with open("portfolio_summary.txt", "w") as file:
        file.write("----- Portfolio Summary -----\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = price * quantity
            file.write(f"{stock}: {quantity} x ${price} = ${investment}\n")
        file.write(f"\nTotal Investment: ${total_value}")
    print("Summary saved to 'portfolio_summary.txt'.")