#Variable for converting from kilometers to miles
conversion = 0.6214

def main():

    #Prompt User
    km = float( input('How many kilometers do you need converted to miles? '))

    #Calls conversion function
    kilometer_converter(km)


def kilometer_converter(km):

    #Calculate Mi --> Km
    miles = km * conversion

    #Display result
    print('That equals', format(miles, '.2'), 'miles.')

#Calls the main function
main()
