from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
# SOL
SOL = cg.get_price(ids="solana", vs_currencies="USD")
am_SOL = 9.54714737
val_SOL = round(float(SOL['solana']['usd']) * am_SOL, 2)
print(f"SOL: {val_SOL} USD ({am_SOL} SOL)")
