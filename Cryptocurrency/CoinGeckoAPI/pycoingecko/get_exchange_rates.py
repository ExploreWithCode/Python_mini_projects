from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
exc_r = cg.get_exchange_rates()
print(exc_r['rates']['btc'])
print("Here is a list of BTC-to-Currency exchange rates:\n")
num = 0
for i in exc_r['rates']:
    num = num+1
    print(f"{num}. {exc_r['rates'][i]}")
