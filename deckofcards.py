import random
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


cards = generate_deck(12, 14)

def shuffle(self):
  if not len(self.temp):
    return []
  
brickResult = {
  "brick": 0,
  "notBrick" : 0,
}

def brick_checker(numberStarter):
  deck = generate_deck(0, numberStarter)
  random.shuffle(deck)
  
  startingHand = deck[0:6]
  
  for i in range(len(startingHand)):
    if startingHand[i].type == "starter":
      return False
    
  return True

for i in range(10000):
  flag = brick_checker(8)
  if flag == False:
    brickResult["notBrick"] += 1
  else:
    brickResult["brick"] += 1

print("Had a starter in hand:", brickResult["notBrick"]/ (brickResult["brick"] + brickResult["notBrick"])*100, "% of the time")