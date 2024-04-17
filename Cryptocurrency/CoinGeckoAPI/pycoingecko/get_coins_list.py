from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
# Get a list of cryptocurrencies in alphabetical order
coins = cg.get_coins_list()
# Organize the output
print("Here is a list of coins and tokens in alphabetical order:\n")
for i in coins:
    ic1 = str(i["symbol"]).upper()
    '''ic0k = str(list(i)[0]).upper()'''
    ic1k = str(list(i)[1]).upper()
    ic2k = str(list(i)[2]).upper()
    print(f"{ic1k}: {ic1} | {ic2k}: {i["name"]}")
'''print(list(coins[0])[0])'''
