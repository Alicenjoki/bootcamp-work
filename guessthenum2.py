import random

while True:

    number = random.randint(1, 20)
    
    guess1 = int(input("Give your first guess between 1 and 20 :"))

    if guess1 > number :
        print("Your guess is too high!")
    elif guess1 < number:
        print("Your guess is too l0w")
    else :
            print("Yaay, you won")   

    guess2 = int(input("Give your second guess between 1 and 20 :"))

    if guess2 > number :
        print("Your guess is too high!")
    elif guess2 < number:
        print("Your guess is too l0w")
    else:
            print("Yaay, you won")

    guess3 = int(input("Give your third guess between 1 and 20 :"))

    if guess3 > number :
        print("Your guess is too high!")
    elif guess3 < number:
        print("Your guess is too l0w")
    else:
        print("Yaay, you won")


    
    play_again = input("play again? (y/n):")
    if play_again != "y":
        break

print("Bye,thank you for playing")
        
