# Import CSV
import csv

# Import the datetime class from the datetime
# module so that it can be used in this program
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    #Create a dictionary to save the information
    dict = {}

    with open(filename, "rt") as csv_file:
        
        # Read the file using CSV reader
        reader = csv.reader(csv_file)
        
        # Skip the header
        next(reader)
        
        # Iterate through the items
        for item in reader:
            key = item[key_column_index]
            dict[key] = item

        return dict

def main():
    # Get customer name
    customer_name = input("What is your full name: ").capitalize()
    customer_TIN = input("What is your Tax ID Number? ")

    PROD_ID = 0
    PROD_NAME = 1
    PROD_PRICE = 2
    PROD_QUANTITY = 1

    # Error Handling
    try:
        # Shop's CSV file
        shop_file = read_dict("products.csv", PROD_ID)
        
        # User's CSV file
        client_file = read_dict("request.csv", PROD_ID)
        
        # Set variables
        subtotal = 0
        quantity = 0

        # Print the shop name
        print()
        print("Hawk Emporium")
        print(f"Customer Name: {customer_name}")
        print(f"Customer TIN Number: {customer_TIN}")
        print()

        for item in shop_file and client_file:

            # SHOP FILE variables
            shop_file_id =  shop_file[item][PROD_ID] # not used
            shop_file_name =  shop_file[item][PROD_NAME]
            shop_file_price =  float(shop_file[item][PROD_PRICE])

            # CLIENT FILE variables (stored for future use)
            client_file_id = client_file[item][PROD_ID] # not used
            client_file_quantity = int(client_file[item][PROD_QUANTITY])

            # Calculate total per product
            product_total = client_file_quantity * shop_file_price
            
            # Print the items
            print(f"{shop_file_name}: {client_file_quantity} @ {shop_file_price}")
            
            # Calculate subtotal and quantity
            subtotal +=  product_total
            quantity += client_file_quantity
        
        # Calculate sales tax and total
        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax

        # Print the quantity, subtotal, sales tax, and total
        print()
        print(f"Number of items: {quantity}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales tax: ${sales_tax:.2f}")
        print(f"Total: ${total:.2f} ")
        print()
        print("Thank you for shopping at the Hawk Emporium.")

        # Use an f-string to print the current
        # day of the week and the current time
        # following this format: Wed Nov  4 05:10:30 2020
        print(f"{current_date_and_time: %c}")
    
    except (FileNotFoundError, PermissionError) as file_error:
        print(file_error)
    
    except KeyError as key_err:
        for item in client_file:
            if item in shop_file:
                shop_file[item]
            else:
                print()
                print(f"This product does not exist in the request.csv file: '{key_err}'")

# Call the main funtion
if __name__ == "__main__":
    main()