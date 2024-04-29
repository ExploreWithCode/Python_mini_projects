from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
inp_cur = input("Give me the ticker symbol of a currency to value things in:\n")
co_mar = cg.get_coins_markets(vs_currency=inp_cur)
print("Here is a list of coins and tokens with some info on them:\n")
num = 0
for i in co_mar:
    num = num+1
    print(f"{num}.")
    print(i, "\n")
