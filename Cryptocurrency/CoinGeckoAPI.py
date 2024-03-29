from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
print("PRICES\n________________________")
BTC = cg.get_coin_ohlc_by_id(id="bitcoin", vs_currency="USD", days="1")
print(f"Bitcoin: {BTC[-1][4]} USD")
ETH = cg.get_coin_ohlc_by_id(id="ethereum", vs_currency="USD", days="1")
print(f"Ethereum: {ETH[-1][4]} USD")

print("\nVALUE\n____________________________________\r")
val_btc = round(BTC[-1][4] * 1.23456789, 2)
val_eth = round(ETH[-1][4] * 2.54272793, 2)
print(f"BTC: {val_btc} USD ({1.23456789} BTC)")
print(f"ETH: {val_eth} USD ({2.54272793} ETH)")
print(f"total: {val_btc + val_eth} USD")
