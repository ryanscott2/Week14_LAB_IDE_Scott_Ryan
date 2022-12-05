# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class: 11/28/22
# Date of Submission: 12/4/22
# Description: This program takes a control input to determine the number of players, requests that amount of
# names and scores, and then stores them in the "golf.txt" file.
# Input: The control number "playernum", and then the requested amount of names and scores
# Output: This program outputs the names and scores to "golf.txt"
# Additional Comments: The initial input stored in "playernum" must be an integer (IE: 2) and not a string (IE: two)


def scoreinput():
    playernum = input('Enter the number of players: ')
    if playernum.isdigit():
        with open('golf.txt', 'a') as f:
            f.write(f"The number of players is: {playernum}\n")
            for i in range(0, int(playernum)):
                name = input(f'Enter the name of player number {i+1}: ')
                score = input(f'Enter the score of player number {i+1}: ')
                f.write(f'{name}\n')
                f.write(f'{score}\n')
    else:
        print('Please enter a number.')


scoreinput()