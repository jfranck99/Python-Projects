#Create main function

def main():

    #Get user input
    user_data = input('Enter a series of characters you would like to test: ')

    #Display result
    print('There are', number_v(user_data), 'vowels and', \
          number_c(user_data), 'consonants in this entry.')

#Function to count vowels
def number_v(s):

    #Make a list of vowels to test
    vowels = ['a','e','i','o','u']

    #Start a counter
    count_v = 0

    #Create loop to test characters in the string
    for ch in s:
        if ch.lower() in vowels:
            count_v += 1

    return count_v

#Function to count consonants
def number_c(s):

    #Make a list of vowels to test from
    vowels = ['a','e','i','o','u']

    #Start a counter
    count_c = 0

    #Create loop to test characters in the string
    for ch in s:
        if ch.isalpha() and ch.lower() not in vowels:
            count_c += 1

    return count_c

main()

    
