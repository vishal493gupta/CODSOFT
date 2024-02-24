# Rock Paper Scissors Game.

''' Three Rules that should be follow..
1. Rock wins against Scissors.
2. Scissors win against paper.
3. Papers wins against rock.'''

import random

Rock="✊"
Paper="✋"
Scissors="✌️"

map=['Rock', 'Paper',' Scissors']

comp_choose=random.choice(map).lower()

you_choose=input("What would you like to choose ? Type Rock, Paper or Scissors : ").lower()

if comp_choose==you_choose:
	print(f"you choose {you_choose} and computer choose {comp_choose} , both are same thats why it is tie(draw).")
	
elif (you_choose==Rock )and (comp_choose==Scissors):
	print(f"you choose {you_choose} and computer choose {comp_choose}, Congrats 😇, you have won..")
	
elif (you_choose==Paper )and (comp_choose==Rock):
	print(f"you choose {you_choose} and computer choose {comp_choose}, Congrats 😇, you have won..")
	
elif (you_choose==Scissors )and (comp_choose==Paper):
	print(f"you choose {you_choose} and computer choose {comp_choose}, Congrats 😇, you have won..")
	
else:
	print(f"you choose {you_choose} and computer choose {comp_choose}, Oops 😢, you lost the game.")