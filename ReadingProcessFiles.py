# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class: 11/28/22
# Date of Submission:
# Description:
# Input:
# Output:
# Additional Comments:

def numinput():
    num1 = input('Please enter the amount of numbers you will store in file 1: ')
    with open('numbers1.txt', 'a') as f1:
        for i1 in range(0,int(num1)):
            usernum1 = input(f'Enter number {i1+1} of {num1}: ')
            f1.write(usernum1)
            f1.write('\n')

    num2 = input('Please enter the amount of numbers you will store in file 2: ')
    with open('numbers2.txt', 'a') as f2:
        for i2 in range(0,int(num2)):
            usernum2 = input(f'Enter number {i2+1} of {num2}: ')
            f2.write(usernum2)
            f2.write('\n')


def numcalc():
    with open('numbers1.txt', 'r') as f1:

        lines1 = f1.read().split('\n')
    with open('numbers2.txt', 'r') as f2:

        lines2 = f2.read().split('\n')

    del lines1[-1]
    del lines2[-1]

    scalar_product = 0

    for (x, y) in zip(lines1, lines2):
        z = int(x)*int(y)
        scalar_product = int(scalar_product) + int(z)
    print(scalar_product)



def menu():
    control = '0'
    while control != '3'
        print('1. Enter numbers.')
        print('2. Calculate the product.')
        print('3. Exit program')
        control = input('Enter your choice: ')
        if control == '1':
            numinput()
        elif control == '2':
            numcalc()
        elif control == '3':
            print('Exiting program.')
        else:
            print('Error: please enter 1-3')

menu()


