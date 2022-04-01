import os
import pdb

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines += f.read().split("\n")
    lines.pop()


class Card:
    def __init__(self, value):
        self.value = value

class Deck:
    def __init__(self, cards):
        self.cards = cards

    def display(self):
        #return [f"{index}: {card.value}" for index, card in enumerate(self.cards)]
        return [card.value for card in self.cards]
    
    def draw(self):
        return self.cards.pop(0)
    
    def add_to_bottom(self, card):
        self.cards.append(card)

deck_one_cards = list()
deck_two_cards = list()
one_filled = False
for line in lines:
    if line == "" or line == "Player 1:":
        continue
    if line == "Player 2:":
        one_filled = True
        continue
    if one_filled:
        deck_two_cards.append(Card(value=int(line)))
    else:
        deck_one_cards.append(Card(value=int(line)))

deck_one = Deck(cards=deck_one_cards)
deck_two = Deck(cards=deck_two_cards)
print("Deck one:")
print(deck_one.display())
print("Deck two:")
print(deck_two.display())

turn = 1
#while turn < 7:
winner = None
while len(deck_one.cards)>0 and len(deck_two.cards)>0:
    print(f"\n-- Turn {turn} --")
    print(f"Player 1's deck: {deck_one.display()}")
    print(f"Player 2's deck: {deck_two.display()}")
    player_one_plays = deck_one.draw()
    print(f"Player 1 plays: {player_one_plays.value}")
    player_two_plays = deck_two.draw()
    print(f"Player 2 plays: {player_two_plays.value}")
    if player_one_plays.value > player_two_plays.value:
        winner = 1
        print(f"Player 1 wins the round!")
        deck_one.add_to_bottom(player_one_plays)
        deck_one.add_to_bottom(player_two_plays)
    elif player_one_plays.value < player_two_plays.value:
        winner = 2
        print(f"Player 2 wins the round!")    
        deck_two.add_to_bottom(player_two_plays)
        deck_two.add_to_bottom(player_one_plays)
    turn += 1
# [3, 2, 10, 6, 8, 5, 9, 4, 7, 1]
print(f"\n== Post-game results ==")
print(f"Player {winner} wins!")
print(f"Player 1's deck: {deck_one.display()}")
print(f"Player 2's deck: {deck_two.display()}")
winner_deck = deck_one if winner==1 else deck_two
#cards_index = [index+1 for index, card in enumerate(winner_deck.cards)]
#print(cards_index)
score = 0
winner_deck_cards = winner_deck.cards
winner_deck_cards.reverse()
for index, card in enumerate(winner_deck_cards):
    score += card.value*(index+1)
print(f"Score: {score}")
#score_cards = 