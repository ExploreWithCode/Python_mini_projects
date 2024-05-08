from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
nft = cg.get_nfts_list()
print("Here is a list of NFTs:\n")
num = 0
for i in nft:
    num = num+1
    print(f"{num}.\n {i}")
