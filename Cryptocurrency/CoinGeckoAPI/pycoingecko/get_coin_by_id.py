from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
inp = input("Give me the name of a cryptocurrency and get info on it:\n").lower()
print("Note that not all coins and tokens are supported!\n")
# This is the data set and it is a dictionary
coin = cg.get_coin_by_id(id=inp)
# Turn the dictionary into a list
cl = list(coin)
# Select a couple useful parts of the list
final_list = (cl[1], cl[2])
# Create a for loop to get the data and give titles
for i in final_list:
    print(f"{i}: {str(coin[i]).upper()}")
# Get the description for the coin or token
print(coin['description']['en'])
