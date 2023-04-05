def main():
    # Ask for the following user input: current cumulative points, current cumulative credits
    # Note: The default value for current cum points is 12 and default for current cum credits is 3
    # since the GPA begins at 4.0
    current_cum_pts = float(input("How many current cumulative points do you have in your GPA? (ex: 270) "))
    if current_cum_pts == 0:
        current_cum_pts = 4

    current_cum_credits = float(input("How many current cumulative credits do you have in your GPA? (ex: 80) "))
    if current_cum_credits == 0:
        current_cum_credits = 1


    # Call the function that calculates the old GPA
    # Print old GPA
    print()
    print("YOUR CURRENT GPA:")
    old_GPA = calculate_old_GPA(current_cum_pts, current_cum_credits)
    print(old_GPA)

    # Ask the user for number of classes this semester
    sem_class = int(input("How many classes are you taking this semester? "))
    print()

    # Call the function that calculates the FORECASTED GPA
    forecasted_GPA = calculate_GPA(current_cum_pts, current_cum_credits, sem_class)

    # Print the forecasted GPA
    print()
    print("----------------------------------------------------------------------")
    print(f"Your expected CUMULATIVE GPA at the end of this semester is {forecasted_GPA: .3f}.")
    print("----------------------------------------------------------------------")
    print()

def calculate_old_GPA(current_cum_pts, current_cum_credits):
    """
    Computes the OLD GPA
    Shows the results to the user
    Returns old GPA
    """
    # Calculate the OLD GPA using the current points and current credits
    oldGPA = current_cum_pts / current_cum_credits

    return oldGPA

def convert_grade(grade):
    """
    Converts letter grade to float
    Purpose: Takes the letter sem_grade that the user inputs
            and converts it to a number sem_grade
    Parameters: sem_grade (letter)
    Returns a converted sem grade (float)
    """
    if grade == "A":
        grade = 4.0
    elif grade == "A-":
        grade = 3.7
    elif grade == "B+":
        grade = 3.4
    elif grade == "B":
        grade = 3.0
    elif grade == "B-":
        grade = 2.7
    elif grade == "C+":
        grade = 2.4
    elif grade == "C":
        grade = 2.0
    elif grade == "C-":
        grade = 1.7
    elif grade == "D+":
        grade = 1.4
    elif grade == "D":
        grade = 1.0
    elif grade == "D-":
        grade = 0.7
    elif grade == "F" or grade == "UW":
        grade = 0

    return grade

def get_class_grade(num):
    valid_grades = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F", "UW"]
    skip_grades = ["P", "I", "W", "T", "NR"]
    
    class_grade = input(f"What LETTER GRADE do you expect to get in class {num}? ").upper()
    
    while class_grade not in valid_grades:
        while class_grade in skip_grades:
            print("Please exclude classes with grades P, I, W, T and NR because they don't count into the GPA \n")
            class_grade = input(f"Again, what LETTER GRADE do you expect to get in class {num}? ").upper()
        while (class_grade not in valid_grades) and (class_grade not in skip_grades):
            print("Invalid grade \n")
            class_grade = input(f"Again, what LETTER GRADE do you expect to get in class {num}? ").upper()

    return class_grade

def get_quality_credits(num):

    quality_credits = int(input(f"How many CREDITS is class {num}? "))
    print()

    return quality_credits

def calculate_GPA(current_cum_pts, current_cum_credits, sem_class):
    """
    Calculates the GPA
    Parameters:
    - current cumulative credits
    - current cumulative points
    - number of classes taken this sem
    Returns the calculated GPA
    """
    sem_total_points = 0
    sem_credits = 0
    
    for x in range(sem_class):
        num = x + 1
        # Call the get_class_grade
        class_grade = get_class_grade(num)

        # Call the get_quality_credits
        quality_credits = get_quality_credits(num)

        # Call the convert_grade function to convert the user input (letter grade) to number grade
        converted_grade = convert_grade(class_grade)

        # Compute the cumulative points and credits in each iteration
        class_points = quality_credits * converted_grade
        sem_total_points += class_points
        sem_credits += quality_credits

    # Compute for the FORECASTED GPA
    # NEW STUDENT
    if current_cum_pts == 4 and current_cum_credits == 1:
        expected_pts = sem_total_points + (current_cum_pts - 4)
        expected_credits = sem_credits + (current_cum_credits - 1)
        expected_GPA = expected_pts / expected_credits

    # OLD STUDENT
    else:
        expected_pts = sem_total_points + current_cum_pts
        expected_credits = sem_credits + current_cum_credits
        expected_GPA = expected_pts / expected_credits

    return expected_GPA


# Call the main function
if __name__ == "__main__":
    main()