from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
plat = cg.get_asset_platforms()
print("Here is a list of asset platforms (Blockchain networks):\n")
num = 0
for i in plat:
    num = num+1
    print(f"{num}. {i['name']}")
