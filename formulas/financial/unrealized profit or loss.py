current_value = float(input("Input the current position value:\n"))
avg_buy_price = float(input("Input the average price:\n"))
amount = float(input("Input the current position amount:\n"))
current_unrealized_profit_or_loss = current_value - (avg_buy_price * amount)
print(f"Your unrealized returns are: {round(current_unrealized_profit_or_loss, 2)}")
