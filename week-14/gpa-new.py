import tkinter as tk
root = tk.Tk()

grad = tk.StringVar()
clas = tk.StringVar()

classes = []
grades = []

def main():
    tk.Entry(root,textvariable=clas).grid(row=0,column=0)
    tk.Entry(root,textvariable=grad).grid(row=0,column=1)
    tk.Button(root,text="add class",command=add_class).grid(row=0,column=2)

    root.mainloop()

def add_class():
    grade = grad.get()
    classs = clas.get()
    grades.append(grade)
    classes.append(classs)
    grad.set("")
    clas.set("")
    for x in range(len(classes)):
        textt = f"class: {classes[x]} score: {grades[x]}"
        tk.Label(root,text=textt, anchor="w").grid(row=1+x)
    tk.Button(root,text="Calculate GPA",command=calc).grid(row=x+2)    

def calc():
    sum = 0
    for x in converted_grades:
        sum += int(x)
    gpa = sum / len(grades)
    gpa = f"{gpa:.2f}"
    tk.Label(root,text="GPA: "+ str(gpa)).grid(row=2,column=1)


if __name__ == "__main__":
    main()