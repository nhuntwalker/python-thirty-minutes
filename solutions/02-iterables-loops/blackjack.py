"""Model of a single-deck blackjack game with a single player and a dealer."""
import random

cards = {
    "1": {"val": 1, "count": 4},
    "2": {"val": 2, "count": 4},
    "3": {"val": 3, "count": 4},
    "4": {"val": 4, "count": 4},
    "5": {"val": 5, "count": 4},
    "6": {"val": 6, "count": 4},
    "7": {"val": 7, "count": 4},
    "8": {"val": 8, "count": 4},
    "9": {"val": 9, "count": 4},
    "10": {"val": 10, "count": 4},
    "J": {"val": 10, "count": 4},
    "Q": {"val": 10, "count": 4},
    "K": {"val": 10, "count": 4},
    "A": {"val": 11, "count": 4}
}

dealer = {
    "value": 0,
    "hand": []
}
player = {
    "value": 0,
    "hand": []
}

# deal out initial cards, dealer first
for i in range(2):
    card = random.choice(list(cards.keys()))
    cards[card]["count"] -= 1

    dealer["hand"].append(card)
    dealer["value"] += cards[card]["val"]
    
    card = random.choice(list(cards.keys()))
    cards[card]["count"] -= 1

    player["hand"].append(card)
    player["value"] += cards[card]["val"]

# Player draws cards until they can't anymore
while player["value"] < 17:
    card = random.choice(list(cards.keys()))
    if cards[card]["count"] == 0:
        continue
    cards[card]["count"] -= 1

    player["hand"].append(card)
    player["value"] += cards[card]["val"]

# Dealer draws cards until they can't anymore
while dealer["value"] < 17:
    card = random.choice(list(cards.keys()))
    if cards[card]["count"] == 0:
        continue
    cards[card]["count"] -= 1

    dealer["hand"].append(card)
    dealer["value"] += cards[card]["val"]

# This will combine the player's hand into one string for later
player_hand = ' '.join(player["hand"])

# Branching logic for comparing player and dealer hands
if player["value"] > 21:
    msg = f"""You've drawn {player_hand}
    
You have {player['value']} in your hand. Bust! Try again!"""

elif dealer["value"] > 21:
    msg = f"""The dealer drew {dealer['value']} into their hand and busted!

You won!"""    

elif player["value"] > dealer["value"]:
    msg = f"""You've drawn {player_hand}

You have {player['value']} in your hand, and you won! Congratulations!"""


elif player["value"] == dealer["value"]:
    msg = f"""You've drawn {player_hand}

You have {player['value']} in your hand and tied with the dealer. No win, no loss."""

elif player["value"] < dealer["value"]:
    msg = f"""You've drawn {player_hand}

You have {player['value']} in your hand, but the dealer had {dealer['value']}. You lose!"""

print(msg)
