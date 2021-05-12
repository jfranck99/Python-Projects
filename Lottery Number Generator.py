#Import module for random functions
import random

#Create constant variables

Beginning = 0
End = 9
Digits = 7

#Create a list to store numbers

numbers = []

#Make a loop to generate numbers
for count in range(Digits):
    numbers.append(random.randint(Beginning, End))

#Display lottery numbers
print('Your lottery numbers are: ', end='')
for index in range(Digits):
    print(numbers[index], end='')
