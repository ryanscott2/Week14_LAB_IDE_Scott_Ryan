# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class: 11/28/22
# Date of Submission:
# Description: This program opens "golf.txt" reads its contents into a list, and comprehends the contents of each
# list element to determine the appropriate output
# Input: This program does not require any input
# Output: This program outputs the data stored in "golf.txt"
# Additional Comments: If 'The number of players' is entered as a player name or score it will not print with the
# appropriate format. If a number is entered in a name it will also cause a formatting issue.


header = 'The number of players'
def scorereader():
    with open('golf.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.find(header) != -1:
                print(f'{line}', end='')
            elif not any([char.isdigit() for char in line]):
                print(f'Name: {line}', end='')
            elif any([char.isdigit() for char in line]):
                print(f'Score: {line}')




scorereader()
