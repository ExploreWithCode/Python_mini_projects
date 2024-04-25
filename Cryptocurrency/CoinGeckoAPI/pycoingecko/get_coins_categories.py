from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
cats = cg.get_coins_categories()
print("Here are some cryptocurrency categories:\n")
num = 0
for i in cats:
    num = num+1
    print(f"{num}.")
    print(i, "\n")
