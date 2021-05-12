#Create Variable for Total Collection
total = 0

#Create Loop
for day in range (1,8):
    #Ask user for bugs collected each day
    print( 'How many bugs were collected on day' , day)
    bugs = int(input())

    #Add daily collection to total
    total += bugs

#Display Total Bugs Collected
print('You collected a total of: ', total, ' bugs.')
