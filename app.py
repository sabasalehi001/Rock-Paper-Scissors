import random

def play_game():
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    user_choice = user_choice.lower()

    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    print("Your choice:", user_choice)
    print("Computer's choice:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            print("You win!")
        else:
            print("Computer wins!")
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print("You win!")
        else:
            print("Computer wins!")
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            print("You win!")
        else:
            print("Computer wins!")
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")

play_game()
