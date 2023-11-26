from Take5Player import Player
from Take5State import State, PlayerState
import random

class MyAI(Player):
    def __init__(self):
        Player.__init__(self)
        self.setName('MyAI')

    def playCard(self, hand, rows, state):
        #Sorting the hand first from low to high cards
        sorted_hand = sorted(hand, key=lambda card: card.number)

        #Initialize variables so we can choose the best card from our hand
        best_card = None 
        min_gap = 1000000.0 
        min_penalty = 1000000.0


        for card in sorted_hand:
            #Find what card goes to what row in our hand, from low to high
            row_index = card.goesToRow(rows)
            if row_index is not None:
                #Calcuate the gap between the card we are iterating and the last card in the row it goes to
                gap = card.number - rows[row_index].cards[-1].number
                #Calculate the penalty if we put the card we are iterating in the row it goes to 
                penalty = self.calculateRowPenalty(rows[row_index], card)

                #after iterating through each card, choose the best card
                #according to the gap
                if rows[row_index].size() < 4 and gap < min_gap:
                    best_card = card
                    min_gap = gap
                #according to the penalty
                elif rows[row_index].size() == 4 and penalty < min_penalty:
                    best_card = card
                    min_penalty = penalty

        #return the best card
        #If there is no best card found, lets return the last card
        return best_card if best_card else sorted_hand[-1]

    def chooseRow(self, rows, state):

        #Initialize variables so we can choose the row with the least penalty
        min_penalty = 1000000.0
        best_row_index = 0

        #Lets calculate the penalty of each row to find the roew with the least penalty 
        for i, row in enumerate(rows):
            penalty = self.calculateRowPenalty(row)
            if penalty < min_penalty:
                min_penalty = penalty
                best_row_index = i

        #Return the index of the eow with the best (so lowest) penalty. 
        return best_row_index

    #This is an easy definition to calculate the penalty of a whole row if taken
    def calculateRowPenalty(self, row, new_card=None):
        #calculates the total penalty of a row
        penalty = sum(card.penalty for card in row.cards)
        #If we are playing the 5th card of the row, we need to calcualte the penalty with the card in our hand 
        if new_card and row.size() == 4:
            penalty += new_card.penalty
        return penalty

