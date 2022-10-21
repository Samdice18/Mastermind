import numbers
import random as r


def secret_number(length):
    numbers = "0123456789"

    secret_number = r.sample(numbers, length)

    return secret_number

def run_game():
    
    print("""
     __       __   _________   _________   _______________   ___________   _________
    |  \\     /  | |   ___   | |   ______| |               | |           | |   ____  |
    |   \\   /   | |  |   |  | |  |        |_____     _____| |   ________| |  |   |  |      ___________
    |    \\_/    | |  |___|  | |  |______        |   |       |  |__        |  |___|  |     |           |
    |  |\\   /|  | |   ___   | |_______  |       |   |       |   __|       |   ___   |     |___________|
    |  | \\_/ |  | |  |   |  |        |  |       |   |       |  |________  |  |   \\  \\
    |  |     |  | |  |   |  |  ______|  |       |   |       |           | |  |    \\  \\
    |__|     |__| |__|   |__| |_________|       |___|       |___________| |__|     \\__\\
                                                 __       __   __   ___      __   ____
                                                |  \\     /  | |__| |   \\    |  | |  _ \\
                                                |   \\   /   |  __  |    \\   |  | | | \\ \\
                                                |    \\_/    | |  | |  |\\ \\  |  | | |  \\ \\
                                                |  |\\   /|  | |  | |  | \\ \\ |  | | |   \\ \\
                                                |  | \\_/ |  | |  | |  |  \\ \\|  | | |    \\ \\
                                                |  |     |  | |  | |  |   \\    | | |____| |
                                                |__|     |__| |__| |__|    \\___| |________|
    
    Welcome to the Mastermind game...
    To get started first set up the length of the secret number 
    The length should be greater than 3 and less than 10 
    """)

    not_found = True 
    turns = 12

    while True:
        user_length = input("Enter the required length of the secret number : ")

        if not user_length.isdigit() or len(user_length) > 1 or 3 <= int(user_length) > 9:
            print("Enter a valid length and use numbers...")
            continue
        elif user_length.isdigit or len(user_length) == 1 and 4 >= int(user_length) <= 9:
            secret = secret_number(int(user_length))
            break

    print("""
The secret number has been set and you have 12 turns to get the secret number
* type 'exit' or 'quit' to end the game 

Goodluck....
    """)

    while not_found and turns != 0:
        correct_digits = 0
        incorrect_digits = 0

        user_guess = input("Guess the secret number: ")

        if user_guess.lower() == "exit" or user_guess.lower() == "quit":
            print("Sad to see you go...")
            break

        if len(user_guess) != len(secret):
            print("Enter the required length.")
            continue

        if not user_guess.isdigit():
            print("Enter digits only")
            continue

        if len(user_guess) == len(secret) and user_guess.isdigit():
            for i in range(len(secret)):
                if user_guess[i] in secret:
                    if user_guess[i] == secret[i]:
                        correct_digits += 1
                    else:
                        incorrect_digits += 1

            if user_guess != ''.join(secret):
                turns -= 1
                print(f"you have {turns} turns left")
                
            print(f"""
correct digits in correct places = {correct_digits}
correct digits not in correct places = {incorrect_digits}
            """)

            if user_guess == ''.join(secret):
                print("congratulations, you are a code breaker")
                print(f"the code was : {''.join(secret)}")
                not_found = False

    if turns == 0:
        print("better luck next time.")
        print(f"the code was {''.join(secret)}")



if __name__ == '__main__':
    run_game()