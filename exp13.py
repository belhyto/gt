import random

TOTAL_AMOUNT = 100
DISCOUNT_FACTOR = 0.9  # Value of money decreases each round

def bargaining_game():
    global TOTAL_AMOUNT # Declare TOTAL_AMOUNT as global at the beginning of the function
    round_num = 1
    proposer = 'A'
    responder = 'B'

    while True:
        print(f"\nRound {round_num} - {proposer} makes an offer to {responder}")

        # Proposer makes an offer
        offer_to_A = random.randint(0, TOTAL_AMOUNT)
        offer_to_B = TOTAL_AMOUNT - offer_to_A

        print(f"Offer: A gets ${offer_to_A}, B gets ${offer_to_B}")

        # Responder decides (simulate acceptance probability)
        acceptance_threshold = 40  # Responder wants at least $40
        responder_share = offer_to_B if responder == 'B' else offer_to_A

        if responder_share >= acceptance_threshold:
            print(f"{responder} accepts the offer!")
            print(f"✅ Final Deal: A gets ${offer_to_A}, B gets ${offer_to_B}")
            break
        else:
            print(f"{responder} rejects the offer.")
            round_num += 1

            # Apply discount
            TOTAL_AMOUNT = int(TOTAL_AMOUNT * DISCOUNT_FACTOR)

            # Swap roles
            proposer, responder = responder, proposer

# Run the game
if __name__ == "__main__":
    print("   Bargaining Game: Split $100 between Player A and Player B")
    bargaining_game()
