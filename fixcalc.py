number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))
case = int(input("Enter 1.Addition \n2.Subtraction \n3.Multiplication \n4.Division: "))

if case == 1:
    print("Addition:", number_one + number_two)
elif case == 2:
    print("Subtraction:", number_one - number_two)
elif case == 3:
    print("Multiplication:", number_one * number_two)
elif case == 4:
    print("Division:", number_one / number_two)
else:
    print("Invalid choice")
