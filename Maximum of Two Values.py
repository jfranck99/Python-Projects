#Define function
def max_of_two(one,two):
    #Test 1
    if one > two:
        return one
    
    #Test 2
    elif two > one:
        return two

    #Default
    else:
        equal = 'neither; they are equal'
        return equal

#Ask for the first number
one = int(input('What is the first number you would like to compare? '))

#Ask for the second number
two = int(input('What is the second number you would like to compare? '))

#Display result
print('The maximum value is', max_of_two(one,two))
