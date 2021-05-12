#Create counter variable for outer loop.
currentYear = 1;
totalRainfall = 0;

#Ask user for number of years.
years = int( input('How many years do you want to track the rainfall for? '))

#Create outer loop for each year
while currentYear <= years:

    
    #print(currentYear) #Tracks current year in outer loop

    #Create inner loop for each month
    for x in range (1, 13):

        #Ask user for rainfall
        print('How many inches of rain were there in month', x, 'of year', currentYear, '?')
        rainfall = int(input())

        #Add to total rainfall
        totalRainfall += rainfall

    #Increase year counter
    currentYear += 1

#Calculate number of months
months = years * 12

#Display number of months
print('We tracked the rainfall for',months ,'months.')

#Display total rainfall
print('Throughout this time, it rained', totalRainfall, 'inches.')

#Calculate average rainfall per month
average = totalRainfall/months

#Display average rainfall
print('That is an average of', format(average,'.2'), 'inches of rain per month.')
