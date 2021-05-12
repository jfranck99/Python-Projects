#Open the file
myfile = open('numbers.txt', 'r')

#Read and display file
for line in myfile:
    number = int(line)
    print(number)

#Close the file
myfile.close()
