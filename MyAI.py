from Take5Player import Player
from Take5State import State, PlayerState
import random


class MyAI(Player):
    def __init__(self):
        Player.__init__(self)
        self.setName('MyAI')

    def playCard(self, hand, rows, state):
        # Sort hand based on card number
        sorted_hand = sorted(hand, key=lambda card: card.number)

        # If early in the game, try to play middle cards to keep flexibility
        if len(hand) > 7:
            return sorted_hand[len(sorted_hand) // 2]

        # Analyze the vulnerability of each row
        vulnerable_rows = [row for row in rows if row.size() == 4]
        if vulnerable_rows:
            # Find the card that fits in the most vulnerable row (highest penalty)
            for card in reversed(sorted_hand):
                if card.goesToRow(vulnerable_rows) is not None:
                    sorted_vulnerable_rows = sorted(vulnerable_rows, key=lambda x: x.penalty(), reverse=True)
                    if card.goesToRow([sorted_vulnerable_rows[0]]) is not None:
                        return card

        # Try to play a card that goes into a row without giving a penalty
        for card in sorted_hand:
            row_index = card.goesToRow(rows)
            if row_index is not None and rows[row_index].size() < 4:
                return card

        # If all cards seem to give a penalty or go into a vulnerable row, play a random one
        return random.choice(hand)

    def chooseRow(self, rows, state):
        # Choose the row with the least penalty points
        min_penalty = float('inf')
        best_row = 0
        for i, row in enumerate(rows):
            penalty = row.penalty()
            if penalty < min_penalty:
                min_penalty = penalty
                best_row = i
        return best_row
