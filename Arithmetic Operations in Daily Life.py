#Arithmetic Operations in Daily Life

#Objective: The aim of this assignment is to get familiarized with basic arithmetic operations 
#and understand how they can be applied in everyday situations.

#Task 1: Grocery Store Math Calculate the total cost of three items you'd commonly find in a grocery store, 
#given their individual prices. For example, what would be the cost of bread, peanut butter, 
#and jelly be? Prices don't need to be realistic!

#get the price of each item
price_item1 = float(input("Enter the price of the first item:"))
price_item2 = float(input("Enter the price of the second item:"))
price_item3 = float(input("Enter the price of the third item:"))

#Calculate the total cost
total_cost = price_item1 + price_item2 + price_item3

#Print the total cost
print("The total cost of all 3 items is:", total_cost)


#Task 2: Bank Interest If you have a savings account with a particular initial 
#amount and a fixed yearly interest rate, calculate the total amount in your account after a year.

#So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. 
#For the example the expected outcome would be $10,700.

#Define the principle amount(inital investment).
amt = 10000

#Define the annual rate as a percentage.
int = 7

#Define the number of years.
years = 1

#Calculate the future value of the investment using the compoud interest formula.
future_value = amt * ((1 + (0.01 * int)) ** years)

#Round the future value to two decimal places and print it.
print(round(future_value, 2))