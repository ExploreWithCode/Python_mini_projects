from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
cat_l = cg.get_coins_categories_list()
print("Here is a list of cryptocurrency categories:\n")
num = 0
for i in cat_l:
    num = num+1
    print(f"{num}. {i['name']}")
