print("WELCOME TO THE DRAGON GAME!!!!")
print("Defeat the dragon!")
print( "You have 3 chances to deafeat it, Choose one of the following attacks:!!!")
print("\nKick = 25\nPunch = 15\nMagic = 50")

dragon_health = 100
chances = 3
total_damage = 0

for i in range(chances):
    attack = input(f"\nChance {i+1} - Your Move: ").lower()

    if attack == "kick":
        total_damage += 25
        print("You kicked the dragon! -25HP")
    elif attack == "punch":
        total_damage += 15
        print("You punched the dragon! -15HP")
    elif attack == "magic":
        total_damage += 50
        print("You used magic!!!!! -50HP")
    else: 
        print("Invalid Move! ")

if total_damage >= dragon_health:
    print("You dealt with", total_damage, "damage of dragon!")
    print("Congratulations.")
else:
    print("You dealt with", total_damage, "damage of dragon!")
    print("You lost!. The dragon flew away.")
