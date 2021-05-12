#Create main function
def main():

    #Get user input
    user_name = input('What is your full name? ')

    #Display result
    print('Your initials are:', uppercase(user_name))

#Function to test for uppercase letters
def uppercase(s):

    #Variable to store initals
    initials = ''
    
    #Create loop to test characters in the string
    for ch in s:
        if ch.isalpha() and ch.isupper():
            initials += ch + '. '
            

    return initials

main()
