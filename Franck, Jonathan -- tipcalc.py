x = raw_input ("What is your name?")
print "Hello " + x + "."
raw_input ("How was your meal?")
meal = input ("How much does your meal cost:")
tax = input ("How much is tax:")
tip = input ("Now, how much of a tip do you want to give:")
meal = meal + meal*tax
total = meal + meal*tip
print "Your total bill is: " + ("%.2f" % total)
raw_input ("Press <enter> to close the Tip Calculator.")
