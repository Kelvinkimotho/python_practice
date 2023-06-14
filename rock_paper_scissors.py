#importing the  module
import random
#creating a funcvtion named game
def game():
     options=["rock","paper","scissors"]
     comp_choice=random.choice(options)
     user_choice=input("Enter your choice (rock\paper\scissors):").lower()
     print("your choice is:"+user_choice)
     print("computer choice is:"+comp_choice)
     if user_choice==comp_choice:
         print("It's a tie")
     elif user_choice=="paper" and comp_choice=="scissors":
         print("You win")
     elif user_choice=="paper" and comp_choice=="rock":
         print("You win")
     elif user_choice=="scissors" and comp_choice=="paper":
         print("You win")
     else: print("computer win!!")
#function call
game()