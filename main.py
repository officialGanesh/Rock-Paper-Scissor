# import the requied stuff
from random import choice

def rock_paper_scissor():
    '''Main game function to play rock-paper-scissor'''
    score = 0

    while True:
        stop = input('press q to stop or leave to play!!: ')

        if stop == 'q':
            break
        computer_move = choice(['r', 'p', 's'])
        
        player_move = input(
            'Enter your move ( r --> rock, s --> scissors and p --> paper ): ').lower()

        if computer_move == player_move:
            print("It's a tie!!")

        else:
            # player win check
            if (player_move == 'r' and computer_move == 's') or (player_move == 'p' and computer_move == 'r') or (player_move == 's' and computer_move == 'p'):
                score += 1
                print("You Won")

            else:
                print("Computer Won")

    print(f"Your total score --> {score}")      

if __name__ == "__main__":

    rock_paper_scissor()

    print("Code Completed 🔥")
