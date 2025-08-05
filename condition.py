# def check_age(): 
#     age = int(input("Enter your age: "))
#     if age >= 18:
#         print("You are eligible to vote")
#     else :
#         print("You are not eligible to vote")
# check_age()


# def check_grade(grades):
#     if grades >= 90:
#         print("You've got A+ Grade.")
#     elif grades >= 80:
#         print("You've got A Grade.")
#     elif grades >= 70:
#         print("You've got B+ Grade.")
#     elif grades >= 40:
#         print("You've got B Grade.")
#     else:
#         print("Sorry better luck next time.")

# # grade = float(input("Enter your marks: "))
# grades = [1, 2, 3, 4, 5, 6]
# for grade in grades:
#     check_grade(grade)


# def check_age():
#     ages = [10, 20, 19, 17, 22]

#     for age in ages:
#         print(age)
#         if age >= 18:
#             print(f"You are {age} and you are eligible to vote.")
#         else:
#             print(f"You are {age} and you are not eligible to vote.")

# a = "elephant"
# print(a[::-1])

# for i in range(5):
#    check_age()

# n = 0
# while n<=5:
#     print(n)
#     n = n+1


def check_grade(grade):
    if grade >= 90:
        return "A+ Grade"
    elif grade >= 80:
        return "A Grade"
    elif grade >= 70:
        return "B+ Grade"
    elif grade >= 40:
        return "B Grade"
    else:
        return "Sorry, better luck next time"

num = int(input("How many students' grades do you want to check? "))

for i in range(num):
    try:
        grade = float(input(f"Enter marks for student {i+1}: "))
        result = check_grade(grade)
        print(f"Student {i+1} - {grade}: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric marks.")
