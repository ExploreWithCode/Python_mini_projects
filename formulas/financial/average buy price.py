current_value = float(input("Input the current position value:"))
current_unrealized_profit_or_loss = float(input("Input the current profit or loss:"))
amount = float(input("Input the current position amount:"))
avg_buy_price = (current_value - current_unrealized_profit_or_loss) / amount
print(f"Your average buy price is {round(avg_buy_price, 2)}")
