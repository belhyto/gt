class VCGAuction:
    def __init__(self, bidders):
        """
        bidders: dict of {agent_name: value}
        """
        self.bidders = bidders
        self.winner = None
        self.payments = {}

    def run_auction(self):
        # Sort bidders by their value
        sorted_bidders = sorted(self.bidders.items(), key=lambda x: x[1],
                               reverse=True)
        self.winner = sorted_bidders[0][0]
        second_price = sorted_bidders[1][1] if len(sorted_bidders) > 1 else 0

        # VCG payment rule: winner pays the externality imposed (second highest value)
        for bidder in self.bidders:
            if bidder == self.winner:
                self.payments[bidder] = second_price
            else:
                self.payments[bidder] = 0

    def get_result(self):
        return {
            'winner': self.winner,
            'payments': self.payments
        }

# Example usage
if __name__ == "__main__":
    bidders = {
        'Alice': 100,
        'Bob': 80,
        'Charlie': 60
    }

    auction = VCGAuction(bidders)
    auction.run_auction()
    result = auction.get_result()

    print("Winner:", result['winner'])
    print("Payments:")
    for bidder, payment in result['payments'].items():
        print(f"  {bidder}: ${payment}")
