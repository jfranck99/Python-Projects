# This PB&J Text Adventure was made by Jonathan Franck
a = raw_input ("Hello, welcome to the PB&J Text Adventure! It is nearly lucnh time, aren't you hungry?(yes or no) ")
if a == "yes":
    print "Ok, let's make a pb&j!"
    b = raw_input ("What is the first ingredient? ")
    if b == "bread":
        print "Right"
        c = raw_input ("What do you want to put on the bread first the peanut butter or the jelly? ")
        if c == "peanut butter":
            print "Ok"
            d = raw_input ("Would you like creamy or crunchy peanut butter? ")
            print "Now you spread your %s peanut butter on the piece of bread."%(d)
            e = raw_input ("What type of jelly do you want strawberry or grape? ")
            print "Then you spread the %s jelly on the other slice of bread. Next, you put the two slices of bread together. Finally, eat up!"%(e)
            raw_input ("Press <enter> to chew.")
            raw_input ("Press <enter> to exit.")
        elif c == "jelly":
            print "Ok"
            f = raw_input ("Do you want grape or strawberry jelly? ")
            print "Now you spread the %s jelly on the slice of bread."%(f)
            g = raw_input ("What type of Peanut butter do you want creamy or crunchy? ")
            print "Then, you spread your %s peanut butter on your bread. Next, you put the two slices of bread together. Finally, eat up!"%(g)
           
            raw_input ("Press <enter> to chew.")
            raw_input ("Press <enter> to exit.")
        else:
            print "I do not understand."
            raw_input ("Press <enter> to exit.")
    else:
        print "No, you dummy. The first ingredient is bread."
        c = raw_input ("What do you want to put on the bread first the peanut butter or the jelly? ")
        if c == "peanut butter":
            print "Ok"
            d = raw_input ("Would you like creamy or crunchy peanut butter? ")
            print "Now you spread your %s peanut butter on the piece of bread."%(d)
            e = raw_input ("What type of jelly do you want strawberry or grape? ")
            print "Then you spread the %s jelly on the other slice of bread. Next, you put the two slices of bread together. Finally, eat up!"%(e)
            raw_input ("Press <enter> to chew.")
            raw_input ("Press <enter> to exit.")
        elif c == "jelly":
            print "Ok"
            f = raw_input ("Do you want grape or strawberry jelly? ")
            print "Now you spread the %s jelly on the slice of bread."%(f)
            g = raw_input ("What type of Peanut butter do you want creamy or crunchy? ")
            print "Then, you spread your %s peanut butter on your bread. Next, you put the two slices of bread together. Finally, eat up!"%(g)
            raw_input ("Press <enter> to chew.")
            raw_input ("Press <enter> to exit.")
        else:
            print "I do not understand."
            raw_input ("Press <enter> to exit.")
elif a == "no":
    print "Oh, well. Goodbye."
    raw_input ("Press <enter> to exit.")
