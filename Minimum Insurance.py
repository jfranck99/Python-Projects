#Variable for minimum percentage
min_percent = 0.8

def main():
    #Ask user for total cost
    cost = float( input( 'What is the total cost of the building/property? '))

    #Calls function to calculate and display insurance
    find_insurance(cost)

def find_insurance(cost):
    #Calculate insurance from cost
    insurance = cost * min_percent

    #Display result
    print('You should purchase at least $', format(insurance, ',.2f'),'in insuramnce.')


#Call main function
main()
