# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class: 11/28/22
# Date of Submission:
# Description:
# Input:
# Output:
# Additional Comments:

header = 'The number of players'
def scorereader():
    with open('golf.txt', 'r') as f:
       lines = f.readlines()
       print(lines)
       for line in lines:
           if line.find(header) != -1:
               print(f'{line}', end='')
           elif not any([char.isdigit() for char in line]):
               print(f'Name: {line}', end='')
           elif any([char.isdigit() for char in line]):
               print(f'Score: {line}', end='')




scorereader()
