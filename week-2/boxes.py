number_of_items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

# print(f"The number of items is {number_of_items} and number of items per box is {items_per_box}.")

import math

number_of_boxes = number_of_items / items_per_box

print(f"For {number_of_items} items, packing {items_per_box} in each box, you will need {math.ceil(number_of_boxes)} boxes.")
