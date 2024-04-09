from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
# Get a list of cryptocurrencies in alphabetical order
coins = cg.get_coins_list()
# Organize the output
for i in coins:
    print(i)
