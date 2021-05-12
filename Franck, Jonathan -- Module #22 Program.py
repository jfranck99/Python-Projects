thing == 'vehicle'
vehicle == 'car'
car == 'corvette'
if thing == 'vehicle':
    if vehicle == 'car':
        if car == 'corvette':
            print 'This car is a corvette'
        else:
            print 'I am not sure what this car is'
    else:
        print 'I do not know what type of vehicle this is'
else:
    print 'I do not know what this thing is'
