def main():
    add_class = "Yes"
    add_class = input("Add class? (Yes or No): ").capitalize()

    while add_class != "No":
        # course_code = input("Course code: ")
        course_grade = input("Letter grade: ").upper()
        course_credits = int(input("Credits: "))

        sort_grades(course_grade)
        sort_credits(course_grade, course_credits)
        
        add_class = input("Add more class? (Yes or No): ").capitalize()
        
        if add_class == "No":
            sort_grades(course_grade)
            sort_credits(course_grade, course_credits)

    # button
    print("Calculate")


# lists
grade_A = []
grade_A_minus = []

grade_B_plus = []
grade_B = []
grade_B_minus = []

grade_C_plus = []
grade_C = []
grade_C_minus = []

grade_D_plus = []
grade_D = []
grade_D_minus = []

grade_F = []
grade_UW = []

grade_P = []
grade_I = []
grade_W = []
grade_T = []
grade_NR = []

def sort_grades(grade):
    if grade == "A":
        grade_A.append(grade)
        return grade_A
    elif grade == "A-":
        grade_A_minus.append(grade)
        return grade_A_minus
    elif grade == "B+":
        grade_B_plus.append(grade)
        return grade_B_plus
    elif grade == "B":
        grade_B.append(grade)
        return grade_B
    elif grade == "B-":
        grade_B_minus.append(grade)
        return grade_B_minus
    elif grade == "C+":
        grade_C_plus.append(grade)
        return grade_C_plus
    elif grade == "C":
       grade_C.append(grade)
       return grade_C
    elif grade == "C-":
        grade_C_minus.append(grade)
        return grade_C_minus
    elif grade == "D+":
        grade_D_plus.append(grade)
        return grade_D_plus
    elif grade == "D":
        grade_D.append(grade)
        return grade_D
    elif grade == "D-":
        grade_D_minus.append(grade)
        return grade_D_minus
    elif grade == "F":
        grade_F.append(grade)
        return grade_F
    elif grade == "UW":
        grade_UW.append(grade)
        return grade_UW
    elif grade == "":
        grade_P.append(grade)
        return grade_P
    elif grade == "":
        grade_I.append(grade)
        return grade_I
    elif grade == "":
        grade_W.append(grade)
        return grade_W
    elif grade == "":
        grade_T.append(grade)
        return grade_T
    elif grade == "":
        grade_NR.append(grade)
        return grade_NR

    print(grade_A)
    print(grade_A_minus)
    print(grade_B_plus)
    print(grade_B)
    print(grade_B_minus)
    print(grade_C_plus)
    print(grade_C)
    print(grade_C_minus)
    print(grade_D_plus)
    print(grade_D)
    print(grade_D_minus)
    print(grade_F)
    print(grade_UW)
    print(grade_P)
    print(grade_I)
    print(grade_W)
    print(grade_T)
    print(grade_NR)

# lists
credits_A = []
credits_A_minus = []

credits_B_plus = []
credits_B = []
credits_B_minus = []

credits_C_plus = []
credits_C = []
credits_C_minus = []

credits_D_plus = []
credits_D = []
credits_D_minus = []

credits_F = []
credits_UW = []

credits_P = []
credits_I = []
credits_W = []
credits_T = []
credits_NR = []

def sort_credits(grade, credits):
    if grade == "A":
        credits_A.append(credits)
        return credits_A
    elif grade == "A-":
        credits_A_minus.append(credits)
        return credits_A_minus
    elif grade == "B+":
        credits_B_plus.append(credits)
        return credits_B_plus
    elif grade == "B":
        credits_B.append(credits)
        return credits_B
    elif grade == "B-":
        credits_B_minus.append(credits)
        return credits_B_minus
    elif grade == "C+":
        credits_C_plus.append(credits)
        return credits_C_plus
    elif grade == "C":
        credits_C.append(credits)
        return credits_C
    elif grade == "C-":
        credits_C_minus.append(credits)
        return credits_C_minus
    elif grade == "D+":
        credits_D_plus.append(credits)
        return credits_D_plus
    elif grade == "D":
        credits_D.append(credits)
        return credits_D
    elif grade == "D-":
        credits_D_minus.append(credits)
        return credits_D_minus
    elif grade == "F":
        credits_F.append(credits)
        return credits_F
    elif grade == "UW":
        credits_UW.append(credits)
        return credits_UW
    elif grade == "":
        credits_P.append(credits)
        return credits_P
    elif grade == "":
        credits_I.append(credits)
        return credits_I
    elif grade == "":
        credits_W.append(credits)
        return credits_W
    elif grade == "":
        credits_T.append(credits)
        return credits_T
    elif grade == "":
        credits_NR.append(credits)
        return credits_NR

main()