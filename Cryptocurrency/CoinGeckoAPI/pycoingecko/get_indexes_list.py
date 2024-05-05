from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
ind = cg.get_indexes_list()
print("Here is a simple list of market indexes:\n")
num = 0
for i in ind:
    num = num+1
    print(f"{num}. {i}")
