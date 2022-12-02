# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class: 11/28
# Date of Submission:
# Description:
# Input:
# Output:
# Additional Comments:

lines = []

def scorereader():
    with open('golf.txt', 'r') as f:
       lines = f.readlines()
       i = 0
       print(lines)
       for line in lines:
           if i == 0:
               print(f'{line}', end='')
               i += 1
           elif any(chr.isdigit(#for chr in line or something)) == False:
               print(f'Name: {line}', end='')
           elif line.isdigit() == True:
               print(f'Score: {line}', end='')




scorereader()
