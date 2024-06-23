import os

name_list = []
bid_list = []

while True:
    name = input("What's your name? ")
    bid = int(input("What's your bid amount? "))
    name_list.append(name)
    bid_list.append(bid)
    askAgain = input("Are there any other bidders?(Y/N) ")
    if askAgain.upper() == "N":
        break
    elif askAgain.upper() == "Y":
        os.system('cls')

def createDict(name_list, bid_list):
    dictionary = {}
    for name, bid in zip(name_list, bid_list):
        dictionary[name] = bid
    return dictionary


user_dictionary = createDict(name_list, bid_list)

def highestBid(dictionary):
    maximum = max(dictionary.values())
    max_bidder = [key for key, value in dictionary.items() if value == maximum][0]
    print(f"The highest bid is from {max_bidder} and the amount is {maximum}")

highestBid(user_dictionary)
