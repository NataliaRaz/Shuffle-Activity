from random import randint

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♠", "♣"]

deck_of_cards = [f"{card}{suit}" for card in CARDS for suit in SUITS]

# Implement a solution for shuffling a deck of cards
# Use only randint() and no other imports
def shuffle_deck(deck):
    total_cards = len(deck)
    current_index = 0

    while current_index < total_cards:
        random_index = randint(0, total_cards - 1)

        chosen_card = deck.pop(random_index)

        deck.append(chosen_card)

        current_index += 1

    return deck

print("Deck before shuffling:")
print(deck_of_cards)

shuffled_deck = shuffle_deck(deck_of_cards)
print("\nDeck after shuffling:")
print(shuffled_deck)
