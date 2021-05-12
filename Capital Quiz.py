#Import the directory for the random.choice() funtion
import random

#Constant number of quiz questions asked
NUM_STATES = 5

#Define main function
def main():

    #Initialize state_caps dictionary
    state_caps = state_cap_dictionary()

    #Initialize answer counters
    correct = 0
    incorrect = 0

    #Quiz the user
    for count in range(NUM_STATES):

        #Get a random state and capital
        state, capital = random.choice(list(state_caps.items()))

        #Delete state and capital from list of quiz questions
        del state_caps[state]

        #Ask the user a question
        print('What is the capital of', state, '? ', end = '')
        answer = input()

        #Grade amswer
        if answer.lower() == capital.lower():
            correct += 1
            print('That is correct!')

        else:
            incorrect += 1
            print('Sorry, the correct answer is', capital)

    #Display the results
    print('Correct answers:', correct)
    print('Incorrect answers:', incorrect)

def state_cap_dictionary():
    sc = {  'Alabama':'Montgomery',
            'Alaska':'Juneau',
            'Arizona':'Phoenix',
            'Arkansas':'Little Rock',
            'California':'Sacramento',
            'Colorado':'Denver',
            'Connecticut':'Hartford',
            'Delaware':'Dover',
            'Florida':'Tallahassee',
            'Georgia':'Atlanta',
            'Hawaii':'Honolulu',
            'Idaho':'Boise',
            'Illinois':'Springfield',
            'Indiana':'Indianapolis',
            'Iowa':'Des Moines',
            'Kansas':'Topeka',
            'Kentucky':'Frankfort',
            'Louisiana':'Baton Rouge',
            'Maine':'Augusta',
            'Maryland':'Annapolis',
            'Massachusetts':'Boston',
            'Michigan':'Lansing',
            'Minnesota':'Saint Paul',
            'Mississippi':'Jackson',
            'Missouri':'Jefferson City',
            'Montana':'Helena',
            'Nebraska':'Lincoln',
            'Nevada':'Carson City',
            'New Hampshire':'Concord',
            'New Jersey':'Trenton',
            'New Mexico':'Santa Fe',
            'New York':'Albany',
            'North Carolina':'Raleigh',
            'North Dakota':'Bismarck',
            'Ohio':'Columbus',
            'Oklahoma':'Oklahoma City',
            'Oregon':'Salem',
            'Pennsylvania':'Harrisburg',
            'Rhode Island':'Providence',
            'South Carolina':'Columbia',
            'South Dakota':'Pierre',
            'Tennessee':'Nashville',
            'Texas':'Austin',
            'Utah':'Salt Lake City',
            'Vermont':'Montpelier',
            'Virginia':'Richmond',
            'Washington':'Olympia',
            'West Virginia':'Charleston',
            'Wisconsin':'Madison',
            'Wyoming':'Cheyenne',
            }

    return sc

#Call the main function
main()
