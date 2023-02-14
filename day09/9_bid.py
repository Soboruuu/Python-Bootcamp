bidding ={}
bidding_finish=False

def highest_bid(bidding):
  highest_bid = 0
  winner = ""
  for bidder in bidding:
    bid_amount = bidding[bidder]
    if highest_bid < bid_amount:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
while not bidding_finish:
  name = input("What is your name? \n")
  price = int(input("What is your bid? \n$"))
  bidding[name] = price
  should_continue = input("If there are other users who want to bid?\n")
  if should_continue == "no":
    bidding_finish = True
    highest_bid(bidding)