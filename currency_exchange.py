# usd_rate = 133.50

# def usd_to_npr(usd):
#     return usd * usd_rate

# def npr_to_usd(npr):
#     return npr / usd_rate

# print("Convert Currency!!")
# print("a. USD to NPR")
# print("b. NPR TO USD")

# choose = input("Choose an option(a or b)")

# if choose == "a":
#     usd = float(input("Enter amount in USD: "))
#     convert = usd_to_npr(usd)
#     print(f"{usd} USD = {convert:.2f}NPR")
# elif choose == "b":
#     npr = float(input("Enter amount in NPR: "))
#     convert = npr_to_usd(npr)
#     print(f"{npr} NPR = {convert:.2f}USD")
# else:
#     print("Invalid Choice")

rate = 133.50

print("a. USD to NPR")
print("b. NPR to USD")

choice = input("Choose a or b: ")

if choice == "a":
    usd = float(input("USD: "))
    print("NPR =", usd * rate)
elif choice == "b":
    npr = float(input("NPR: "))
    print("USD =", npr / rate)
else:
    print("Invalid choice")
