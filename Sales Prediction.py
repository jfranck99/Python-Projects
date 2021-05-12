# Ask for projected sales.
sales = float (input ("What are your projected total sales: $"))

# Calculate profit (23% of sales)
profit = float (sales * 0.23)

# Display profit
print ("Your profit will be $" , format(profit, ',.2f'))
