#Create sum variable
total = 0

#Create test variable
test = 0

#Create while loop
while test <= 0:

    #Ask user for number
    number = int( input('Enter a positive number to be summed, or a negative number to end the sum: '))

    #Check if number is postive or negative
    if (number >= 0):

        #Add positive number to total
        total += number

    else:

        #Break loop
        test = 1

        #Tell user
        print('You ended the sum by entering a negative number.')

#Display sum
print('Your total is:', total)
                

