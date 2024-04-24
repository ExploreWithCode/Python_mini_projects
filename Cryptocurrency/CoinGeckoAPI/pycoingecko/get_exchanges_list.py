from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
exc = cg.get_exchanges_list()
print("Here is some information regarding exchanges:\n")
num = 0
for i in exc:
    num = num+1
    print(f"{num}.")
    print(i, "\n")
