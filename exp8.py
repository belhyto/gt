import random
from abc import ABC, abstractmethod

class Auction(ABC):
    def __init__(self, bidders):
        self.bidders = bidders
        self.winner = None
        self.final_price = None

    @abstractmethod
    def conduct_auction(self):
        pass

class FirstPriceSealedBidAuction(Auction):
    def conduct_auction(self):
        highest_bidder = max(self.bidders, key=lambda b: b['bid'])
        self.winner = highest_bidder
        self.final_price = highest_bidder['bid']
        return self.winner, self.final_price

class SecondPriceSealedBidAuction(Auction):
    def conduct_auction(self):
        sorted_bidders = sorted(self.bidders, key=lambda b: b['bid'], reverse=True)
        self.winner = sorted_bidders[0]
        self.final_price = sorted_bidders[1]['bid'] if len(sorted_bidders) > 1 else sorted_bidders[0]['bid']
        return self.winner, self.final_price

# Example Usage
bidders = [
{'name': 'Alice', 'bid': 80},
{'name': 'Bob', 'bid': 110},
{'name': 'Charlie', 'bid': 85}
]
first_price_auction = FirstPriceSealedBidAuction(bidders)
winner, price = first_price_auction.conduct_auction()
print(f"First-Price Auction Winner: {winner['name']} at price {price}")
second_price_auction = SecondPriceSealedBidAuction(bidders)
winner, price = second_price_auction.conduct_auction()
print(f"Second-Price Auction Winner: {winner['name']} at price {price}")
