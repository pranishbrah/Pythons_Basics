"""
CONTROL STATEMENT
INDENTATION
"""

# money_in_hand = float(input("How much money do you have? "))

# if money_in_hand <= 30.99:  # Control statement
#     print("Timi ghar mai basa")
#     print("Prawess Sir ko class aau, and programmming sika")


# elif 40 < money_in_hand and  money_in_hand <= 200: # CONTROL statement
#     print("Bhai chiya khau")


# elif 200 < money_in_hand and money_in_hand < 10000:  # CONTROL statement
#     print("Sathi Lakeside, Pokhara ma vetum")

# else:
#     print("Sathi ma sanaga business Idea xa. Let's startup a business")

# print("Thank you for using this program")

print("WELCOME TO THE POWERLIFTING CLUB")

lift_weight = float(input("How much weight can you overall lift in Squat Bench Deadlift (SBD) in Kgs? "))

if lift_weight <= 150:
    print("Start lifting with proper form and techniques")
    print("Focus on nutrients and consistency")

elif 150 < lift_weight <= 215:
    print("You're getting stronger!!!,")
    print("Add some 1RPM in and on about 10 days gaps. ")

elif 215 < lift_weight <= 500:
    print("Damn Man you're really strong. ")
    print("Sign Up for powerlifting meet. ")

else:
    print("You're elite level! Contact national coaches or consider international competitions!")

print("Keep Grinding Hard Big Guy!!!")