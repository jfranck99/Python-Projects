#Ask for the weight of the package.
weight = float( input( 'How much does your package weight? '))

#Figure out the price.
if (weight <= 2):
    price = weight * 1.50

else:
    if (weight <= 6):
        price = weight * 3

    else:
        if (weight <= 10):
            price = weight * 4

        else:
            price = weight * 4.75

#Display the price
print ('It will cost $' + format( price, ',.2f') + ' to ship the package.')
