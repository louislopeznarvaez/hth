# Guessing Game - louis, seline xue, maite r.,jayla
import random

def guessing_game():
    while True:
        try:
            user_input =int(input("guess a number between 1 and 100"))
            if 1<= (user_input) <= 100:
                return user_input
            else:
                print("enter a correct number between 1 and 100")
        
        except ValueError:
            print("please enter a valid number")

#step 4

def generate_random_number():
    return random.randint(1, 100)

def play_game():
    print("guess a number between 1 and 100 and see if you answer correct")
    secret_number = generate_random_number()

    while True:
        guess = guessing_game()

        if guess < secret_number:
            print("your guess is too low, try again")

        elif guess > secret_number:
            print("your guess is too high, try again")

        else:
            print("congrats, you got it right!")
            break

#step 5

def game_loop():
    while True:
        play_game()

        user_input= input("do you want to play again").lower()
        if user_input == "yes":
            play_game()
        else:
            print("thanks for playing")
            break

if __name__ == "__main__":
    game_loop()