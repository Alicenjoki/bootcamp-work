import random

while True:
    random_number = random.randint(1, 20)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and 20! :"))
        if guess > random_number:
            print("Your guess is too high")
        elif guess < random_number:
            print("your guess id too low")
        elif guess == random_number:
            print("Yaay, You won")



        
        play_again = input("play again? (y/n):")
        if play_again != "y":
            break

        print("Bye,thank you for playing")
    