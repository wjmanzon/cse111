#input from user
subtotal = float(input("Please enter the subtotal: "))

#compute discount and tax
discount = subtotal * .10
tax = subtotal * 0.06

#this computes how much the user needs to reach $50
remaining = 50 - subtotal

#compute for new subtotal when there is discount
discounted_subtotal = subtotal - discount
discounted_tax = discounted_subtotal * 0.06

# this gets the datetime module from python library
from datetime import datetime
date_time_now = datetime.now()
day_of_week = date_time_now.weekday()

# this code is temporary
# day_of_week = 6

#here goes the if elif else statements
if subtotal >= 50: 
    if day_of_week == 2:
        total = discounted_subtotal + discounted_tax
        print(f"Discount: {discount: .2f}")
        print(f"Sales tax amount: {discounted_tax: .2f}")
        print(f"Total: {total: .2f}")
    elif day_of_week == 3:
        total = discounted_subtotal + discounted_tax
        print(f"Discount: {discount: .2f}")
        print(f"Sales tax amount: {discounted_tax: .2f}")
        print(f"Total: {total: .2f}")
    else:
        total = subtotal + tax
        print(f"Sales tax amount: {tax: .2f}")
        print(f"Total: {total: .2f}")
else:
    if day_of_week == 2:
        total = subtotal + tax
        print(f"Sales tax amount: {tax: .2f}")
        print(f"Total: {total: .2f}")
        print("You can get a 10% discount today when you purchase worth $50 or more!")
        print(f"You are about to purchase ${subtotal} worth of items.")
        print(f"Add items worth ${remaining} or more to get 10% discount.")
    elif day_of_week == 3:
        total = subtotal + tax
        print(f"Sales tax amount: {tax: .2f}")
        print(f"Total: {total: .2f}")
        print("You can get a 10% discount today when you purchase worth $50 or more!")
        print(f"You are about to purchase ${subtotal} worth of items.")
        print(f"Add items worth ${remaining} or more to get 10% discount.")
    else:
        total = subtotal + tax
        print(f"Sales tax amount: {tax: .2f}")
        print(f"Total: {total: .2f}")