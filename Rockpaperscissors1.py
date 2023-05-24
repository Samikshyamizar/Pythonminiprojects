import random

# Function to generate a random number for computer's selection
def ComputerRandomNumberGen():
    return random.randint(1, 3)

# Function to display computer's choice
def displayComputerChoice(choice):
    if choice == 1:
        print("Computer chose Rock.")
    elif choice == 2:
        print("Computer chose Paper.")
    else:
        print("Computer chose Scissors.")

# Function to display user's choice
def displayUserChoice():
    choice = int(input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors: "))
    if choice == 1:
        print("You chose Rock.")
    elif choice == 2:
        print("You chose Paper.")
    else:
        print("You chose Scissors.")
    return choice

# Function to determine the winner of RPS game
def DetermineWinnerOfRPS(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif user_choice==1 and computer_choice==2:
        return"the rock wins"
    elif user_choice==2 and computer_choice==1:
        return"the rock no win sed"
   
    else:
        return "computer"

# Function to display user's name, address, and phone number if user wins
def display_static_Info(name, address, phone, winner):
    if winner == "user":
        with open("inputData.txt", "a") as f:
            f.write(f"{name}, {address}, {phone} has won the game.\n")

# Main function to run the game
def play_RPS_game():
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")
    print("Let's play Rock-Paper-Scissors!")
    while True:
        user_choice = displayUserChoice()
        computer_choice = ComputerRandomNumberGen()
        displayComputerChoice(computer_choice)
        winner = DetermineWinnerOfRPS(user_choice, computer_choice)
        if winner == "tie":
            print("It's a tie. Play again!")
        else:
            print(f"{winner.capitalize()} wins!")
            display_static_Info(name, address, phone, winner)
            break

play_RPS_game()
