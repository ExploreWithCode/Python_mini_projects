from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
defi = cg.get_global_decentralized_finance_defi()
# This is a simple automated way, but it can give confusing results
'''for i in defi:
    print(f"{i}: {defi[i]}\n")'''
# The manual version allows me to clarify
print(f"DeFi Market Cap: {round(float(defi['defi_market_cap']), 2)} USD")
print(f"ETH Market Cap: {round(float(defi['eth_market_cap']), 2)} USD")
print(f"DeFi to ETH ratio: {round(float(defi['defi_to_eth_ratio']), 2)} %")
print(f"24-hour trading volume: {round(float(defi['trading_volume_24h']), 2)} USD")
print(f"DeFi dominance: {round(float(defi['defi_dominance']), 2)} % (The percentage of the total market cap that DeFi has)")
print(f"Top coin name: {defi['top_coin_name']}")
print(f"Top coin DeFi dominance: {round(float(defi['top_coin_defi_dominance']), 2)} % (The percentage of the DeFi market cap that the top coin in DeFi has)")
