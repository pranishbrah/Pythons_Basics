print("Welcome to the favorite things survey")

games = []
fruits = []
dishes = []

while True:
    game = input("Enter your favorite game: ")
    fruit = input("Enter your favorite fruit: ")
    dish = input("Enter your favorite dish: ")

    games.append(game)
    fruits.append(fruit)
    dishes.append(dish)

    more = input("Do you want to add another response? (yes/no): ").lower()
    if more == "no":
        break

print("Survey Completed! Here are the results:")

# print("Games: ", game)
# print("Fruits: ", fruit)
# print("Dishes: ", dish)

# for loop for showing resultssss
for i in range(len(games)):
    print(f"\n--- User {i+1} ---")
    print("Favorite Game:", games[i])
    print("Favorite Fruit:", fruits[i])
    print("Favorite Dish:", dishes[i])

# for i in range (1000):
#     print("Hello", i) 

# count = 0

# while count < 5:
#     print("Hello", count)

#     count += 1

# print("Welcome to the favorite things survey")

# games = []
# fruits = []
# dishes = []

# while True:
#     game = input("Enter your favorite game: ")
#     fruit = input("Enter your favorite fruit: ")
#     dish = input("Enter your favorite dish: ")

#     games.append(game)
#     fruits.append(fruit)
#     dishes.append(dish)

#     # Ask if user wants to continue
#     more = input("Do you want to add another response? (yes/no): ").lower()
#     if more != "yes":
#         break

# print("\nSurvey Completed! Here are the results:")
# print("Games:", games)
# print("Fruits:", fruits)
# print("Dishes:", dishes)



# command = 'y'

# while command == 'y':
#     name = input("Enter your name: ")
#     weight = float(input("Enter the number of squats you can perform: "))

#     if weight <= 150:
#         print("Good Job")
#         print("Keep Pushing")
    
#     elif 150 <= weight <= 200:
#         print("You're getting stronger!!!,")

#     else:
#         print("You're elite level! Contact national coaches or consider international competitions!")

#     command = input("Press [y/N]: ")



# basket = ['Apple', 'Banana', 'Cheery', 'Dragon Fruits', 'Egg Plant', 'Fruit Salad', 'Guava']

# for fruits in basket:
#     print("Basket: ", basket)
#     print("Basket [0]: ", basket[0])
#     print("Basket.last()", basket[-1])


# basket = ['Apple', 'Banana', 'Cherry', 'Dragon Fruits', 'Egg Plant', 'Fruit Salad', 'Guava']
# print("Basket: ", basket)
# print("Basket[0]: ", basket[0])
# print("Basket.last(): ", basket[-1])          
# print("Basket.third_last(): ", basket[-5])    
# print("my favorite fruit is: ", basket[-4])


# iterable data
# list, tuple, sets, dictionaries
# command = 'y'
# while command == 'y':
#     user_fruit = input("Enter the name of your favorite fruit: ")
#     basket.append(user_fruit)
#     print("Favorite Fruit added. ", basket)
#     command = input("Continue? [Y/N]: ")

# print("Thank you!")
