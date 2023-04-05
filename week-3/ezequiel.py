# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime
import os
UNDERLINE = '\033[4m'
END = '\033[0m'
YELLOW = '\033[33m'
def main():
    os.system('cls')
    # Get the user's gender, birthdate, height, and weight.
    print('')
    gender = input("Please enter your gender ("+YELLOW+"M"+END+" or "+YELLOW+"F"+END+"): "+YELLOW)
    birthdate = input(END+"Enter your birthdate ("+YELLOW+"YYYY-MM-DD"+END+"): "+YELLOW)
    pounds = float(input(END+"Enter your weight in U.S. "+YELLOW+"pounds"+END+": "+YELLOW))
    inches = float(input(END+"Enter your height in U.S. "+YELLOW+"inches"+END+": "+YELLOW))
    print(END)
    # compute the user's age in years.
    age = compute_age(birthdate)
    #convert pounds from weight to kilograms
    kg = kg_from_lb(pounds)
    #convert inches from weight to cm, then to mts
    cm = cm_from_in(inches)
    mts = mts_from_cm(cm)
    #Call body_mass_index function.
    bmi = body_mass_index(kg, cm)
    #Call basal_metabolic_rate function.
    bmr = basal_metabolic_rate(gender, kg, cm, age)
    # Print the results for the user to see.
    os.system('cls')
    print('')
    print(UNDERLINE+'Results:'+END)
    print('')
    print(f'Age (years): {YELLOW}{age}{END}')
    print(f'Weight (kg): {YELLOW}{kg:.2f}{END}')
    print(f'Height (mts): {YELLOW}{mts:.1f}{END}')
    print('')
    print(f'Body mass index: {YELLOW}{bmi:.1f}{END}')
    print(f'Basal metabolic rate (kcal/day): {YELLOW}{bmr:.0f}{END}')
    print('')
    pass
def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()
    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year
    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1
    return years
def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    kg_from_lb = pounds * 0.45359237
    return kg_from_lb
def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    cm_from_in = inches * 2.54
    return cm_from_in
def mts_from_cm(cm):
    mts_from_cm = cm / 100
    return mts_from_cm
def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = weight  / (height ** 2) * 10000
    return bmi
def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender.upper() == "M":
        """ (men)  bmr = 88.362 + 13.397 weight + 4.799 height − 5.677 age """
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender.upper() == "F":
        """ (women)  bmr = 447.593 + 9.247 weight + 3.098 height − 4.330 age """
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr
# Call the main function so that
# this program will start executing.
main()