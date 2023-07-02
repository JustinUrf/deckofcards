from deckofcards import *

def generateDeck(level3, level4, kiriha):
  cards = []
  
  for x in range(level3):
    cards.append(Card("lv3"))
    
  for x in range(level4):
    cards.append(Card("lv3"))
    
  for x in range(kiriha):
    cards.append(Card("kirihia"))
  
  while len(cards) < 50:
    cards.append(Card("Generic"))
      
  return cards
