import random
import numpy as np
import itertools

class Card:
    def __init__(self, type):
      self.type = type
      
def generate_deck(numberOption, numberStarter, numberKiriha):
  cards = [] #Your deck
  
  for x in range(numberOption):
    cards.append(Card("option"))
  
  for x in range(numberStarter):
    cards.append(Card("starter"))
    
  for x in range(numberKiriha):
    cards.append(Card("kiriha"))
    
  while len(cards) < 50:
    cards.append(Card("Generic"))
    
  return cards


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

deck = generate_deck(12,9,8)

def kiriha(deck, firstOrSecond):
  newDeck = deck
  np.random.shuffle(newDeck)
  
  if firstOrSecond == "first":
    kirihaSearch = newDeck[6:12]
  else:
    kirihaSearch = newDeck[7:13]
    
  for i in range(len(kirihaSearch)):
    if kirihaSearch[i].type == "kiriha":
      return True
    
  return False
    

kirihaResult = {
  "yeah": 0,
  "no": 0,
}

for i in range(10000):
  flag = kiriha(deck, "first")
  if flag == True:
    kirihaResult["yeah"] += 1
  else:
    kirihaResult["no"] += 1  

print(kirihaResult)
  
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

print("Had a Rookie in hand:", brickResult["notBrick"]/ (brickResult["brick"] + brickResult["notBrick"])*100, "% of the time")