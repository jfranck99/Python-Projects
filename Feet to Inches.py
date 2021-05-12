#Define conversion function
def feet_to_inches(feet):
    return feet*12

#Prompt user
feet = float(input('How many feet would you like to convert to inches? '))

#Display the result
print(feet, ' feet is equal to', feet_to_inches(feet), 'inches.')
