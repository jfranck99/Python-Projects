#Ask for length of the first rectangle.
lengthOne = int( input('What is the length of the first rectangle? '))

#Ask for width of the first rectangle.
widthOne = int( input('What is the width of the first rectangle? '))
print (' ')

#Ask for length of the second rectangle.
lengthTwo = int( input('What is the length of the second rectangle? '))

#Ask for width of the second rectangle.
widthTwo = int( input('What is the width of the second rectangle? '))
print (' ')

#Calculate the area for both rectangles.

rectOne = lengthOne * widthOne
rectTwo = lengthTwo * widthTwo

#Determine which is larger.

if ( rectOne > rectTwo) :
    print ('The area of the first rectangle is larger than the second.')

elif (rectOne < rectTwo ) :
    print ('The area of the second rectangle is larger than the first.')

else:
    print ('The areas of the two rectangles are equal.')
