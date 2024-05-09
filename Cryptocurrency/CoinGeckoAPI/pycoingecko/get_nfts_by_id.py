from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
print("Get current data (name, price_floor, volume_24h ...) for an NFT collection.\n"
      "As an example, we will use the id 'alter-ego-punks' to get info on that collection.\n")
nft_id = cg.get_nfts_by_id('alter-ego-punks')
for i in nft_id:
    print(f"{i}: {nft_id[i]}")
