from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
var = cg.get_exchanges_id_name_list()
print("Here is a list of exchanges:\n")
for i in var:
    print(i)
