from Take5Player import Player
from Take5State import State, PlayerState
import random


#Defines AI 
class MyAI(Player): 
     def __init__( self ):  
          Player.__init__(self) 
          self.setName('MyAI') 

#Used to play card from hand
def playCard(self, hand, rows, state):
    print(hand)



#Used to select a row  to take when  your card is lower than the top cards in any of the rows
#def chooseRow(self, rows, state):
    




