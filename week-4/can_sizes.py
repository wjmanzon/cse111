"""
Your program must compute the volume of all 12 can sizes.
Your program must compute the surface area of all 12 can sizes.
Your program must compute and print the storage efficiency of all 12 can sizes.
"""

import math

def main():

    # list of 12 cans:
    cans = ["#1 Picnic", 6.83, 10.16, 0.28],["#1 Tall", 7.78, 11.91, 0.43],["#2", 8.73, 11.59, 0.45],["#2.5", 10.32, 11.91, 0.61],["#3 Cylinder", 10.79, 17.78, 0.86],["#5", 13.02, 14.29, 0.83],["#6Z", 5.40, 8.89, 0.22],["#8Z short", 6.83, 7.62, 0.26],["#10", 15.72, 17.78, 1.53],["#211", 6.83, 12.38, 0.34],["#300", 7.62, 11.27, 0.38],["#303", 8.10, 11.11, 0.42]

    i = 0

    for i in range(len(cans)):
    # Declare the variables to be used in 3 functions below:
        radius = cans[i][1]
        height = cans[i][2]

    # Call compute_volume function (list one)
        volume = compute_volume(radius, height)

    # Call compute_surface_area function
        surface_area = compute_surface_area(radius, height)

    # Call the compute_storage_efficiency function
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        print(f"{cans[i][0]} {storage_efficiency:.2f}")

        i += 1

# Define the functions here:
def compute_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency

main()

