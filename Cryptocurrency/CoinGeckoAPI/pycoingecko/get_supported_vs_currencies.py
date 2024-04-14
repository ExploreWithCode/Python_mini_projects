from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
# Get the list of currencies you can compare others against
supp_vs_curr = cg.get_supported_vs_currencies()
# Organize and print the list in sections
supp1 = (supp_vs_curr[0:11])
supp2 = supp_vs_curr[11:-4]
supp3 = (supp_vs_curr[-2], supp_vs_curr[-1])
supp4 = supp_vs_curr[-4:-2]
print(f"Cryptocurrencies:\n{supp1}\n")
print(f"Fiat currencies:\n{supp2}\n")
print(f"Bitcoin Units:\n{supp3}\n")
print(f"Commodities:\n{supp4}")
