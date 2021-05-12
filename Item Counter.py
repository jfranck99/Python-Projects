#Create a counting variable
count = 0

#Open file
myfile = open('names.txt', 'r')

#Create a loop to read the file
for line in myfile:
    count += 1

print('There are', count, 'names in this file.')
