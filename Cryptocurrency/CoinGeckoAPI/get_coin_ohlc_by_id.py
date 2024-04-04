from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
inp = input("Give me the name of a cryptocurrency and get its price back:\n")
# The 'ohlc' stands for 'open, high, low, close' and they correspond to coin[-1][1], coin[-1][2], coin[-1][3] and coin[-1][4] accordingly.
coin = cg.get_coin_ohlc_by_id(id=inp, vs_currency="USD", days="1")
print(f"Current price of {inp.capitalize()}: {coin[-1][4]} USD")
print(f"Open: {coin[-1][1]} USD")
print(f"High: {coin[-1][2]} USD")
print(f"Low: {coin[-1][3]} USD")
print(f"Close: {coin[-1][4]} USD")
