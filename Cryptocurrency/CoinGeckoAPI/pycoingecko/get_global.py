from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
glo = cg.get_global()
for i in glo:
    print(f"{i}: {glo[i]}\n")
