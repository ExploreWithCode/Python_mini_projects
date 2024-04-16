from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
# Get the list of currencies you can compare others against
supp_vs_curr = cg.get_supported_vs_currencies()
# Organize and print the list in sections
supp1 = (supp_vs_curr[0:11])
supp2 = supp_vs_curr[11:-4]
supp3 = (supp_vs_curr[-2], supp_vs_curr[-1])
supp4 = supp_vs_curr[-4:-2]

print(f"\nCryptocurrencies:")
supp1CAP = []
for i in supp1:
    i = str(i).upper()
    supp1CAP.append(i)
print(supp1CAP)
print(f"\nFiat Currencies:")
supp2CAP = []
for i in supp2:
    i = str(i).upper()
    supp2CAP.append(i)
print(supp2CAP)
print(f"\nBitcoin Units:")
supp3CAP = []
for i in supp3:
    i = str(i).upper()
    supp3CAP.append(i)
print(supp3CAP)
print(f"\nCommodities:")
supp4CAP = []
for i in supp4:
    i = str(i).upper()
    supp4CAP.append(i)
print(supp4CAP)
