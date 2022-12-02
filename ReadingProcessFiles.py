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
    print()


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
    print(f'The product is: {scalar_product}\n')


def clearfile():
    with open('numbers1.txt', 'r+') as f1:
        f1.truncate(0)
    with open('numbers2.txt', 'r+') as f2:
        f2.truncate(0)
    print('Numbers cleared\n')

def menu():
    control = '0'
    while control != '4':
        print('1. Enter numbers.')
        print('2. Calculate the product.')
        print('3. Clear numbers')
        print('4. Exit the program.\n')
        control = input('Enter your choice: ')
        print()
        if control == '1':
            numinput()
        elif control == '2':
            numcalc()
        elif control == '3':
            clearfile()
        elif control == '4':
            print('Exiting the program')
        else:
            print('Error: please enter 1-4')

menu()


