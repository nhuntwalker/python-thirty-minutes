"""Model of a multi-deck blackjack game with a single player and a dealer."""
import random
import sys


def build_deck(n_decks: int) -> dict:
    """Construct a collection of cards given a number of decks."""
    return {
        "1": {"val": 1, "count": 4 * n_decks},
        "2": {"val": 2, "count": 4 * n_decks},
        "3": {"val": 3, "count": 4 * n_decks},
        "4": {"val": 4, "count": 4 * n_decks},
        "5": {"val": 5, "count": 4 * n_decks},
        "6": {"val": 6, "count": 4 * n_decks},
        "7": {"val": 7, "count": 4 * n_decks},
        "8": {"val": 8, "count": 4 * n_decks},
        "9": {"val": 9, "count": 4 * n_decks},
        "10": {"val": 10, "count": 4 * n_decks},
        "J": {"val": 10, "count": 4 * n_decks},
        "Q": {"val": 10, "count": 4 * n_decks},
        "K": {"val": 10, "count": 4 * n_decks},
        "A": {"val": 11, "count": 4 * n_decks}
    }


def count_deck(deck: dict) -> int:
    """Count the number of remaining cards in the deck."""
    total = 0
    for card, card_item in deck.items():
        total += card_item['count']
    return total


def deal_card(player: dict, deck: dict, initial: bool=True) -> None:
    """Deal one card at random into the player's hand."""
    if count_deck(deck) <= 0:
        print("We're out of cards. Come again later!")
        sys.exit()

    card = random.choice(list(deck.keys()))
    while deck[card]['count'] == 0:
        card = random.choice(list(deck.keys()))

    deck[card]["count"] -= 1
    player["hand"].append(card)
    if not initial:
        print(f"\nYou drew {card} into your hand.")
    player["value"] += cards[card]["val"]


def take_bet(player: dict) -> float:
    """Prompt the player for how much money to bet."""
    while True:
        print(f"\nYou currently have ${player['money']:.2f}")
        bet = input('How much money would you like to bet on this hand? (min: $20)\n> $')
        if not bet.isdigit() or float(bet) < 20:
            print('You must bet at least $20\n')
            continue
        if float(bet) > player['money']:
            print(f"You only have {player['money']}. You can't bet more than you've got\n")
            continue
        rounded_bet = round(float(bet), 2)
        player['money'] -= rounded_bet
        return rounded_bet


def format_hand(player: dict) -> str:
    """Print the formatted player's hand."""
    player_hand = ' '.join(player["hand"])
    msg = f"You have {player['value']} in your hand."
    msg += f"\nYour cards are: {player_hand}"
    return msg


def hit_or_stay(player: dict) -> str:
    """Prompt the player for whether they want to hit or stay."""
    print(format_hand(player))
    while True:
        action = input('Would you like to hit or stay?\n> ')
        if action.lower() not in ['hit', 'stay']:
            print('You must type either "hit" or "stay"\n')
            continue
        return action.lower()
        

def win_lose_draw(player: dict, dealer: dict, bet: float) -> None:
    """Determine whether this hand is a win, a loss, or a draw for the player."""
    player_hand = ' '.join(player['hand'])

    if dealer["value"] > 21:
        msg = f"The dealer drew {dealer['value']} into their hand and busted!"
        msg += " You won!"
        player['money'] += 2 * bet

    elif player["value"] > dealer["value"]:
        msg = f"You've drawn {player_hand}"
        msg += f" You have {player['value']} in your hand, and you won! Congratulations!"
        player['money'] += 2 * bet

    elif player["value"] == dealer["value"]:
        msg = f"You've drawn {player_hand}"
        msg += f" You have {player['value']} in your hand and tied with the dealer. No win, no loss."
        player['money'] += bet

    elif player["value"] < dealer["value"]:
        msg = f"You've drawn {player_hand}"
        msg += f" You have {player['value']} in your hand, but the dealer had {dealer['value']}. You lose!"

    print(msg)
    reset_hand(player)
    reset_hand(dealer)


def reset_hand(player: dict) -> None:
    """Clear out the player's hand after a round."""
    player['hand'] = []
    player['value'] = 0


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("When you run this script you need to include a number that denotes how many decks you'll be playing with.")
        sys.exit()

    n_decks = sys.argv[1]
    if n_decks not in ['1','2','3','4','5','6','7','8','9','10']:
        print('The number of decks must be in the range from 1 to 10')
        sys.exit()
    n_decks = int(n_decks)

    cards = build_deck(n_decks)

    dealer = {
        "value": 0,
        "hand": []
    }
    player = {
        "value": 0,
        "hand": [],
        "money": 0
    }

    # prompt the user for their money pot
    while True:
        money_pot = input('How much money do you want to play with?\n> $')
        if not money_pot.isdigit() or float(money_pot) < 20:
            print('You must input a number greater ≥ 20\n')
            continue
        player['money'] = float(money_pot)
        break
    
    while player['money'] >= 20:
        bet = take_bet(player)
        for i in range(2):
            deal_card(dealer, cards)
        for i in range(2):
            deal_card(player, cards)
        
        action = hit_or_stay(player)
        while action == 'hit':
            deal_card(player, cards, initial=False)
            if player['value'] > 21:
                break
            action = hit_or_stay(player)

        if player['value'] > 21:
            print(f"You have {player['value']} in your hand. Bust! Try again!\n----")
            reset_hand(player)
            reset_hand(dealer)
            continue
        
        while dealer["value"] <= 17:
            deal_card(dealer, cards)
        
        win_lose_draw(player, dealer, bet)
