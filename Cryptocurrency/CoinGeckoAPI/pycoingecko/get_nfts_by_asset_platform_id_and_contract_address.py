from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
print("Get current data (name, price_floor, volume_24h ...) for an NFT collection.\n"
      "We will use 'Ethlings' as an example and we need the 'asset_platform_id' and 'contract_address.'\n")
nft_ = cg.get_nfts_by_asset_platform_id_and_contract_address('polygon-pos', '0x8a1abd2e227db543f4228045dd0acf658601fede')
for i in nft_:
    print(f"{i}: {nft_[i]}")
