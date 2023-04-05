def main():
    points_positive = 0
    points_negative = 0

    # Introductory statement:
    print ("This program is an implementation of the Rosenberg")
    print("Self-Esteem Scale. This program will show you ten")
    print("statements that you could possibly apply to yourself")
    print("Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters")
    print()
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")
    print()

    # Assessment:
    answer_1 = input("1. I feel that I am a person of worth, at least on an equal plane with others.")
    answer_2 = input("2. I feel that I have a number of good qualities. ")
    answer_3 = input("3. All in all, I am inclined to feel that I am a failure. ")
    answer_4 = input("4. I am able to do things as well as most other people. ")
    answer_5 = input("5. I feel I do not have much to be proud of. ")
    answer_6 = input("6. I take a positive attitude toward myself. ")
    answer_7 = input("7. On the whole, I am satisfied with myself. ")
    answer_8 = input("8. I wish I could have more respect for myself. ")
    answer_9 = input("9. I certainly feel useless at times. ")
    answer_10 = input("10. At times I think I am no good at all. ")

    # Positive
    positive_answers = [answer_1, answer_2, answer_4, answer_6, answer_7]
    for answer_n in positive_answers:
        positive = convert_positive_answer(answer_n)    
        points_positive += positive

    # Negative
    negative_answers = [answer_3, answer_5, answer_8, answer_9, answer_10]
    for answer_n in negative_answers:
        negative = convert_negative_answer(answer_n)
        points_negative += negative

    points = points_positive + points_negative

    print(points)

def convert_positive_answer(answer):
    """
    POSITIVE - numbers 1,2,4,6,7
    ---
    Choice	            Points     Answer 
    Strongly Disagree	0           D
    Disagree	        1           d
    Agree	            2           a
    Strongly Agree	    3           A
    """
    if answer == "D":
        points = 0
    elif answer == "d":
        points = 1
    elif answer == "a":
        points = 2
    else:
        points = 3
    return points

def convert_negative_answer(answer):
    """
    NEGATIVE - numbers 3,5,8,9,10
    ---
    Choice	            Points      Answer
    Strongly Disagree	3           D
    Disagree	        2           d
    Agree	            1           a
    Strongly Agree	    0           A
    """
    if answer == "D":
        points = 3
    elif answer == "d":
        points = 2
    elif answer == "a":
        points = 1
    else:
        points = 0
    return points


main()