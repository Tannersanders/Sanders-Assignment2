'''
Question 7. Miles-Per-Gallon
Input(s): 
- miles_driven, float. from the user
- gas_used_gallons, float, from the user
Process(es): 
- find mile per gallon, float, mpg = miles_driven / gas_used_gallons
Output(s): 
- Miles per gallon
'''
# Type your code here
#Inputs
#Car information
miles_driven = float(input("How many miles have you driven?"))
gas_used_gallons = float(input("How many gallons of gas have you used?"))

#Processes
mpg = float(miles_driven / gas_used_gallons)

#Outputs
print("Your car gets "  + str(mpg) + " miles per gallon!")
''' 
Question 9. Celsius to Fahrenheit Temperature Converter
Input(s): 
- Tempreture (fahrenheit), float, from the user
Process(es): 
- Convert to celsius , float, ((F - 32) * 5) / 9 = C
Output(s): 
- Tempreture (celsisus), float
'''
#Type your code here
#Inputs
temp_fahrenheit = int(input("Hi! What is the temperature in fahrenheit?"))

#Processes
temp_celsisus = float((temp_fahrenheit - 32) * 5) / 9

#Outputs
print(str(temp_fahrenheit) + " degrees in fahrenheit converts to " + str(temp_celsisus) + " degrees celsisus!")

'''
Question 11. Male and Female Percentages
Input(s): 
- males_in_class, int, from the user, 8
- females_in_class, int. from the user, 12
Process(es): 
- total_in_class, int, males + females, 20
- percent_of_males, float, males / total, .4
- percent_of_females, float, females / total .6
Output(s):
- percent_of_males
- percent_of_females
'''
# # Type your code here
# #Inputs
males_in_class = float(input("Hi! How many males are in your class?"))
females_in_class = float(input("How many females are in your class?"))

#Processes
total_in_class = float(males_in_class + females_in_class)
percent_of_males = float((males_in_class / total_in_class) * 100)
percent_of_females = float((females_in_class / total_in_class) * 100)

#Outputs
print("The percent of males in your class are " + str(percent_of_males) + "%")
print("The percent of females in your class are " + str(percent_of_females) + "%")

'''
Question 12. Stock Transaction Program
Input(s): 
  - shares_purchased, int, from the user, 2000
  - purchase_price, float, from the user, 40.00
  - COMMISSION_RATE, float, constant, 0.03
  - shares_sold, int, from the user, 2000
  - sale_price, float, from the user, 42.75
Process(es): 
  - amount_paid, float, shares_purchased * purchase_price, 80000.00
  - commission_1, float, amount_paid * commission_rate, 2400.00
  - amount_sold, float, shares_sold * sale_price, 85500.00
  - commission_2, float, amount_sold * commission_rate, 2565.00
  - earnings, float, amount_sold - amount_paid - commission_1 - commission_2, 535.00
Output(s):
  - amount_paid
  - commission_1
  - amount_sold
  - commission_2
  - earnings
# '''
# # Type your code here

#Inputs
#Buying Shares
COMMISSION_RATE = float(0.03) 
shares_purchased = int(input("How many shares did Joe purchase?"))
purchase_price = float(input("How much did Joe buy each share for?"))
#Selling Shares
shares_sold = int(input("How many shares did Joe sell?"))
sale_price  = float(input("How much did Joe sell each share?"))

#Processes 
#Buying Shares
amount_paid = float(shares_purchased * purchase_price) 
commision_1 = float(amount_paid * COMMISSION_RATE)
#Selling Shares
amount_sold = float(shares_sold * sale_price)
commision_2 = float(amount_sold * COMMISSION_RATE)
#Profit
earnings = float(amount_sold - amount_paid - commision_1 - commision_2)

#Outputs
#Buying Shares

print("Joe paid $" + str(amount_paid)  + " for his " + str(shares_purchased) + " stocks!")
print("Joe had to pay his broker $" + str(commision_1) + ".")
print("Joe sold all of his shares for $" + str(amount_sold) + "!") 
print("Joe had to pay his broker again for $" + str(commision_2) + "!")
print("Joe made $"  + str(earnings) + " overall!")