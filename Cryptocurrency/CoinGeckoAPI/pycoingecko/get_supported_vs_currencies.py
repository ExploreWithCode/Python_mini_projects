from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
# Get the list of currencies you can compare others against
supp_vs_curr = cg.get_supported_vs_currencies()
# Print the list
print(supp_vs_curr)
