#Import random module to generate computer choice. Yes, the computer will play with you!
#Time for some delays
import random, time

#Welcome and initial message displayed in the terminal when user execute this file
print("Welcome to the Mini Game Challenge Project!")
print("Let's play rock, paper, scissors.")
print("Make your choice, typing:\n" \
      " 🪨 'rock' for rock\n" \
      " 📄 'paper' for paper\n" \
      " ✂️ 'scissors' for scissors")
print("Don't worry with caps lock, you can type in any case! But make sure to type correctly by suggestions.")
print("I'll play with you selecting randomly my choice.")

#Asking if user want to play in loop mode
loop_mode = input("Do you want to play in loop mode? (yes/no): ").lower()
loop_mode_condition = loop_mode == 'yes'
if loop_mode_condition:
    print("Loop mode activated! You can play multiple rounds until you decide to quit. Type 0 to quit")
else:
    print("Single round mode activated! You will play only one round.")

def clear_screen():
    """Function to clear the terminal screen for better user experience."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

#initialize the game in loop mode or single round mode
user_score = computer_score = 0

while True:

    #Display the score if in loop mode, and in strong text, clear blue color
    if loop_mode_condition:
        print(f"\033[1;34mScore - You: {user_score} | Computer: {computer_score}\033[0m")

    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    
    #Check if user want to quit the game
    if loop_mode_condition and user_choice == '0':
        print("Thanks for playing! Goodbye!")
        break

    #Validate user input
    if user_choice not in ['rock', 'paper', 'scissors', 'exit']:
        print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
        continue

    #Using random to generate computer choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer_choice}")

    #Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    #Determine the winner in all conditions
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    #Explain the result, justifying the winner
    if result == "It's a tie!":
        print("It's a tie! Both chose the same.")
    elif result == "You win!":
        if user_choice == 'rock':
            print("You win! Rock crushes Scissors.")
        elif user_choice == 'paper':
            print("You win! Paper covers Rock.")
        else:
            print("You win! Scissors cut Paper.")
    else:
        if computer_choice == 'rock':
            print("Computer wins! Rock crushes Scissors.")
        elif computer_choice == 'paper':
            print("Computer wins! Paper covers Rock.")
        else:
            print("Computer wins! Scissors cut Paper.")

    #A little delay for better user experience
    time.sleep(1.5)

    if user_choice == 'exit':
        not loop_mode_condition

    if not loop_mode_condition:
        if user_choice == 'exit':
            print("Thanks for playing! Goodbye!")
            break

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'no':
            break
        #If the choose is yes, another round will start

    #Clear screen for next round
    clear_screen()
    print("Next round! Make your choice again.")
    time.sleep(1)
    clear_screen()