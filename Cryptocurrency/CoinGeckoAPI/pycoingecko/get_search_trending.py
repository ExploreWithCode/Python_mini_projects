from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
trend = cg.get_search_trending()
print("Trending:")
for i in trend:
    print(f"{str(i).upper()}:\n")
    num = 0
    for c in trend[i]:
        num = num + 1
        print(f"{num}.")
        print(c, "\n")
