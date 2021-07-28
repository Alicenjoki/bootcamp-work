import random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
          player = input("Choose rock,paper or scissors: ").lower()
    if player == computer:
            print("computer: ", computer)
            print("player: ", player)
            print("You both tie")

    elif player == "scissors":
      if computer == "rock":
        print("computer: ", computer)
        print("player:", player)
        print("You lose")
      if computer == "paper":
        print("computer: ", computer)
        print("player:", player)
        print("You win")
          

        
    elif player == "rock":
      if computer == "paper":
        print("computer: ", computer)
        print("player:", player)
        print("You lose")
      if computer == "scissors":
        print("computer: ",computer)
        print("player: ",player)
        print("You win")

        
    elif player == "paper":
      if computer == "rock":
        print("computer: ", computer)
        print("player:", player)
        print("You win")
      if computer == "scissors":
        print("computer: ",computer)
        print("player: ",player)
        print("You lose")

    play_again = input("Do you want to play again? (y/n):").lower()
    if play_again != "y":
        break
print("Thanks for playing see you again next time")