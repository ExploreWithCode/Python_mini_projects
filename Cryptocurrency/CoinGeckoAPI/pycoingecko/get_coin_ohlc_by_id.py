from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
inp_coin = input("Give me the name of a cryptocurrency:\n")
inp_cur = input("Give me the ticker symbol of a currency to value it in:\n")
# The 'ohlc' stands for 'open, high, low, close' and they correspond to coin[-1][1], coin[-1][2], coin[-1][3] and coin[-1][4] accordingly.
coin = cg.get_coin_ohlc_by_id(id=inp_coin.lower(), vs_currency=inp_cur, days="1")
print(f"Current price of {inp_coin.capitalize()}: {coin[-1][-1]} {inp_cur.upper()}")
print(f"Open: {coin[-1][1]} {inp_cur.upper()}")
print(f"High: {coin[-1][2]} {inp_cur.upper()}")
print(f"Low: {coin[-1][3]} {inp_cur.upper()}")
print(f"Close: {coin[-1][4]} {inp_cur.upper()}")
