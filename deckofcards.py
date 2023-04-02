import random
import numpy as np
import itertools

class Card:
    def __init__(self, type):
      self.type = type
      
def generate_deck(numberOption, numberStarter):
  cards = [] #Your deck
  
  for x in range(numberOption):
    cards.append(Card("option"))
  
  for x in range(numberStarter):
    cards.append(Card("starter"))
    
  while len(cards) < 50:
    cards.append(Card("Generic"))
    
  return cards


# def brick_checker(numberStarter, firstOrSecond): Inneficient memory usage to create a deck multiple times. Instead made a function that asks for a deck as a parameter.
#   deck = generate_deck(0, numberStarter)
#   random.shuffle(deck)
  
#   if firstOrSecond == "first":
#     startingHand = deck[0:5]
#   else:
#     startingHand = deck[0:6]
  
#   for i in range(len(startingHand)):
#     if startingHand[i].type == "starter":
#       return False
    
#   return True



def brick_checker_with_mulligan(deck, firstOrSecond):
  newDeck = deck
  np.random.shuffle(newDeck)
  
  if firstOrSecond == "first":
    startingHand = newDeck[0:5]
  else:
    startingHand = newDeck[0:6]
    
  for i in range(len(startingHand)):
    if startingHand[i].type == "starter":
      return True
  
  np.random.shuffle(newDeck)
  
  if firstOrSecond == "first":
    startingHand = newDeck[0:5]
  else:
    startingHand = newDeck[0:6]
  
  for i in range(len(startingHand)):
    if startingHand[i].type == "starter":
      return True
  
  return False

deck = generate_deck(12,14)



  
brickResult = {
  "brick": 0,
  "notBrick" : 0,
}

for i in range(10000):
  flag = brick_checker_with_mulligan(deck, "first")
  if flag == True:
    brickResult["notBrick"] += 1
  else:
    brickResult["brick"] += 1

print("Had a starter in hand:", brickResult["notBrick"]/ (brickResult["brick"] + brickResult["notBrick"])*100, "% of the time")