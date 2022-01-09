# Shuffle Deck of Cards

# importing modules
import itertools, random

# OR
# import itertools
# import random

# --> make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
    
random.shuffle(deck) # --> shuffle the cards

# draw five cards
print("You got:")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])
    
