# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class: 11/28
# Date of Submission:
# Description:
# Input:
# Output:
# Additional Comments:

def scoreinput():
    playernum = input('Enter the number of players: ')
    with open ('golf.txt', 'a') as f:
        f.write(f"The number of players is: {playernum}\n")
        for i in range(0,int(playernum)):
            name = input(f'Enter the name of player number {i+1}: ')
            score = input(f'Enter the score of player number {i+1}: ')
            f.write(f'{name}\n')
            f.write(f'{score}\n')
            # put \n in second write command?

scoreinput()