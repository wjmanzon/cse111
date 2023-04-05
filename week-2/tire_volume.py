# TASK: compute the volume of air inside a tire

# get the datetime module from python library
from datetime import datetime
today = datetime.now()

# import math so we can use the math.pi later
import math

w = float(input("Please enter the tire width in mm: ")) #width of tire in mm
a = float(input("Please enter the tire aspect ratio: ")) #aspect ratio of tire
d = float(input("Please enter the wheel diameter in inches: ")) #diameter of wheel in inches

# formula for computing the tire volume
v = math.pi * ((w ** 2) * a * ((w * a) + (2540 * d))) / 10000000000
print(f"The approximate volume is {v: .2f} liters.")

# Add a set of if … elif … else statements
if v > 20 and v < 25:
    will_buy = input ("The price of this tire is $55. Do you want to buy it? If yes, type YES. Otherwise, type NO. ")
    will_buy = will_buy.lower()
    if will_buy == "yes":
        phone_number = input("Perfect! What is your phone number? ")
        print(f"Your order has been placed. We will contact you at {phone_number} soon. Thank you!")
        with open("volumes.txt", "a+") as volumes_file:
            print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}, {phone_number}", file=volumes_file)
    else:
        print("Thank you.")
        with open("volumes.txt", "a+") as volumes_file:
            print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}", file=volumes_file)
elif v > 26 and v < 30:
    will_buy = input ("The price of this tire is $65. Do you want to buy it? If yes, type YES. Otherwise, type NO. ")
    will_buy = will_buy.lower()
    if will_buy == "yes":
        phone_number = input("Perfect! What is your phone number? ")
        print(f"Your order has been placed. We will contact you at {phone_number} soon. Thank you!")

        with open("volumes.txt", "a+") as volumes_file:
            print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}, {phone_number}", file=volumes_file)
    else:
        print("Thank you.")
        with open("volumes.txt", "a+") as volumes_file:
            print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}", file=volumes_file)

elif v > 31 and v < 35:
    will_buy = input ("The price of this tire is $75. Do you want to buy it? If yes, type YES. Otherwise, type NO. ")
    will_buy = will_buy.lower()
    if will_buy == "yes":
        phone_number = input("Perfect! What is your phone number? ")
        print(f"Your order has been placed. We will contact you at {phone_number} soon. Thank you!")

        with open("volumes.txt", "a+") as volumes_file:
            print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}, {phone_number}", file=volumes_file)
    else:
        print("Thank you.")
        with open("volumes.txt", "a+") as volumes_file:
            print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}", file=volumes_file)
elif v > 36 and v < 40:
    will_buy = input ("The price of this tire is $85. Do you want to buy it? If yes, type YES. Otherwise, type NO. ")
    will_buy = will_buy.lower()
    if will_buy == "yes":
        phone_number = input("Perfect! What is your phone number? ")
        print(f"Your order has been placed. We will contact you at {phone_number} soon. Thank you!")

        with open("volumes.txt", "a+") as volumes_file:
            print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}, {phone_number}", file=volumes_file)
    else:
        print("Thank you.")
        with open("volumes.txt", "a+") as volumes_file:
            print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}", file=volumes_file)

elif v > 41 and v < 45:
    will_buy = input ("The price of this tire is $95. Do you want to buy it? If yes, type YES. Otherwise, type NO. ")
    will_buy = will_buy.lower()
    if will_buy == "yes":
        phone_number = input("Perfect! What is your phone number? ")
        print(f"Your order has been placed. We will contact you at {phone_number} soon. Thank you!")

        with open("volumes.txt", "a+") as volumes_file:
            print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}, {phone_number}", file=volumes_file)
    else:
        print("Thank you.")
        with open("volumes.txt", "a+") as volumes_file:
            print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}", file=volumes_file)

elif v > 46 and v < 50:
    will_buy = input ("The price of this tire is $105. Do you want to buy it? If yes, type YES. Otherwise, type NO. ")
    will_buy = will_buy.lower()
    if will_buy == "yes":
        phone_number = input("Perfect! What is your phone number? ")
        print(f"Your order has been placed. We will contact you at {phone_number} soon. Thank you!")

        with open("volumes.txt", "a+") as volumes_file:
            print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}, {phone_number}", file=volumes_file)
    else:
        print("Thank you.")
        with open("volumes.txt", "a+") as volumes_file:
            print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}", file=volumes_file)

elif v > 51 and v < 55:
    will_buy = input ("The price of this tire is $115. Do you want to buy it? If yes, type YES. Otherwise, type NO. ")
    will_buy = will_buy.lower()
    if will_buy == "yes":
        phone_number = input("Perfect! What is your phone number? ")
        print(f"Your order has been placed. We will contact you at {phone_number} soon. Thank you!")

        with open("volumes.txt", "a+") as volumes_file:
            print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}, {phone_number}", file=volumes_file)
    else:
        print("Thank you.")
        with open("volumes.txt", "a+") as volumes_file:
            print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}", file=volumes_file)

elif v > 56 and v < 60:
    will_buy = input ("The price of this tire is $125. Do you want to buy it? If yes, type YES. Otherwise, type NO. ")
    will_buy = will_buy.lower()
    if will_buy == "yes":
        phone_number = input("Perfect! What is your phone number? ")
        print(f"Your order has been placed. We will contact you at {phone_number} soon. Thank you!")

        with open("volumes.txt", "a+") as volumes_file:
            print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}, {phone_number}", file=volumes_file)
    else:
        print("Thank you.")
        with open("volumes.txt", "a+") as volumes_file:
            print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}", file=volumes_file)

elif v > 61 and v < 65:
    will_buy = input ("The price of this tire is $135. Do you want to buy it? If yes, type YES. Otherwise, type NO. ")
    will_buy = will_buy.lower()
    if will_buy == "yes":
        phone_number = input("Perfect! What is your phone number? ")
        print(f"Your order has been placed. We will contact you at {phone_number} soon. Thank you!")

        with open("volumes.txt", "a+") as volumes_file:
            print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}, {phone_number}", file=volumes_file)
    else:
        print("Thank you.")
        with open("volumes.txt", "a+") as volumes_file:
            print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}", file=volumes_file)

elif v > 66:
    will_buy = input ("The price of this tire is $145. Do you want to buy it? If yes, type YES. Otherwise, type NO. ")
    will_buy = will_buy.lower()
    if will_buy == "yes":
        phone_number = input("Perfect! What is your phone number? ")
        print(f"Your order has been placed. We will contact you at {phone_number} soon. Thank you!")

        with open("volumes.txt", "a+") as volumes_file:
            print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}, {phone_number}", file=volumes_file)
    else:
        print("Thank you.")
        with open("volumes.txt", "a+") as volumes_file:
            print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}", file=volumes_file)
else:
    print("Sorry! No tire matches these specifications.")

# with open("volumes.txt", "a+") as volumes_file:
#     print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}, {phone_number}", file=volumes_file)

# with open("volumes.txt", "a+") as volumes_file:
#     print (f"{today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}", file=volumes_file)


