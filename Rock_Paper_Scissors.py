# Rock Paper Scissors Game.

''' Three Rules that should be follow..
1. Rock wins against Scissors.
2. Scissors win against paper.
3. Papers wins against rock.'''

from rps_game_art import logo
import random

Rock="✊"
Paper="✋"
Scissors="✌️"

user_score = 0
computer_score = 0

map=['Rock', 'Paper','Scissors']

while True:
    print(logo)
    comp_choose=random.choice(map).lower()
    you_choose=input("What would you like to choose ? Type Rock, Paper or Scissors : ").capitalize()

    if comp_choose==you_choose.lower():
        print(f"you choose {you_choose} and computer choose {comp_choose} , both are same thats why it is tie(draw).")
        
    elif (you_choose=="Rock" )and (comp_choose=="scissors"):
        print(f"you choose {you_choose} and computer choose {comp_choose}, Congrats 😇, you have won..")
        user_score += 1
        
    elif (you_choose=="Paper" )and (comp_choose=="rock"):
        print(f"you choose {you_choose} and computer choose {comp_choose}, Congrats 😇, you have won..")
        user_score += 1
        
    elif (you_choose=="Scissors" )and (comp_choose=="paper"):
        print(f"you choose {you_choose} and computer choose {comp_choose}, Congrats 😇, you have won..")
        user_score += 1
        
    else:
        print(f"you choose {you_choose} and computer choose {comp_choose}, Oops 😢, You lose! Try again..")
        computer_score += 1
    
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
            break
