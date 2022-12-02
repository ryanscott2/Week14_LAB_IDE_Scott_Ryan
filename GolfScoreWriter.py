# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class: 11/28
# Date of Submission:
# Description: This program takes a control input to determine the number of players, requests that amount of
# names and scores, and then stores them in the "golf.txt" file.
# Input: The control number "playernum", and then the requested amount of names and scores
# Output: This program outputs the names and scores to "golf.txt"
# Additional Comments:

# FIXME: add isadigit checks to prevent crashes?
def scoreinput():
    playernum = input('Enter the number of players: ')
    with open ('golf.txt', 'a') as f:
        f.write(f"The number of players is: {playernum}\n")
        for i in range(0, int(playernum)):
            name = input(f'Enter the name of player number {i+1}: ')
            score = input(f'Enter the score of player number {i+1}: ')
            f.write(f'{name}\n')
            f.write(f'{score}\n')


scoreinput()