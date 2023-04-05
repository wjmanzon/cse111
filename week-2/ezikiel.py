#Import the library
from datetime import datetime
import os

#Call the method to show the current day
current_date_and_time = datetime.now()

#Call the method to show the day
day_of_week = current_date_and_time.weekday()

#0 → Monday
#1 → Tuesday
#2 → Wednesday
#3 → Thursday
#4 → Friday
#5 → Saturday
#6 → Sunday

#Example to enter to the loop
subtotal = -1 
os.system('cls')
print('')
#User inputs → values
while subtotal != 0:
    os.system('cls')
    subtotal = float(input("Please enter the subtotal: "))

    #Conditionals
    if day_of_week == 1 or day_of_week == 2:
        total_discount =  subtotal - 50
        print(f"Discount amount: {total_discount:.2f}")
        sales_tax = float(input("Sales tax amount: "))
        total = total_discount + sales_tax
        print(f"Total: {total:.2f}")
        print('')


    else:
        sales_tax = float(input("Sales tax amount: "))
        total = subtotal + sales_tax
        print(f"Total: {total:.2f}")
        print('')
