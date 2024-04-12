from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
# Get the list of currencies you can compare others against
supp = cg.get_supported_vs_currencies()
# Print the list
print(supp)
