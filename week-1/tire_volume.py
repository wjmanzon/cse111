#compute the volume of a tire

#this imports math so we can use the math.pi later
import math

w = float(input("Please enter the tire width in mm: ")) #width of tire in mm
a = float(input("Please enter the tire aspect ratio: ")) #aspect ratio of tire
d = float(input("Please enter the wheel diameter in inches: ")) #diameter of wheel in inches

#formula for computing the tire volume
v = math.pi * ((w ** 2) * a * ((w * a) + (2540 * d))) / 10000000000

print(f"The approximate volume is {v: .2f} liters.")
