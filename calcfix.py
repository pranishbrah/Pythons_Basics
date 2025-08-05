print("Hamro Calculator" )

print("1 = Add")
print("2 = subtract")
print("3 = multiplication")
print("4 = division")
print("5 = sqroot")

select=int(input("Select Option : "))

if (select in [1,2,3,4]):
    a=float(input("Enter first number : "))
    b=float(input("Enter second number : "))
    if select == 1:
        print("result =",a+b)

    elif select == 2:
        print("result = ",a-b)

    elif select == 3:
        print("result = ",a*b)

    elif select == 4:
        if b!=0:
            print("result = ",a/b)
        else:
            print("Cannot divide by 0")
        
elif select == 5:                   
    c=float(input("Input number : "))
    if c >= 0:
        print("result = ", c ** 0.5)
    else:
        print("cannot square root negative number")


else:
    print("Invalid")