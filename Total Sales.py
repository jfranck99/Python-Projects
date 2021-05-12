days = 7
totalSales = 0
sales = []

for count in range(days):
    sales.append(input('What were the store\'s sales for the day: $'))


for index in range(days):
    totalSales += int(sales[index])
    
print('Your total sales for the week is $', totalSales)






