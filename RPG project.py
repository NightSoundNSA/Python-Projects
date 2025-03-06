import random

#print('The great adventure!')

# Player Name
hero = input("Enter your name: ")

# Hero Stats
hero_hp = 100
hero_dmg = 35
hero_armor = 5
#hero_revives = 0
#critical_chance = 0
#miss_chance = 0
#inventory = ['chestplate', 'sword', 'amulet']   ( Tuples and list maybe ?)
# Should add a regenerative factor or potions.   ( Tuples and list maybe ?)

# Enemies and Stats
goblin_hp = 100
goblin_dmg = 2
goblin_armor = 1

orc_hp = 120
orc_dmg = 4
orc_armor = 2

elite_hp = 160
elite_dmg = 8
elite_armor = 3

boss_hp = 300
boss_dmg = 10
boss_armor = 4

# Random day/night generation
time = random.randint(0,1)
day_night_cycle = 'day' if time == 0 else 'night'

# Based on day and night some monsters will be affected
goblin_hp -= 20 if time == 0 else 0
goblin_dmg += 1 if time == 1 else 0
boss_armor -= 1 if time == 0 else 0
elite_dmg += 1 if time == 0 else 0

if orc_hp < orc_hp / 2:
    orc_dmg += 2
    print("The orc is getting enraged his damage increased")

# Function to handle combat
def combat(enemy_name, enemy_hp, enemy_dmg, enemy_armor):
    global hero_hp
    print(f"A wild {enemy_name} has appeared!")
    while enemy_hp > 0 and hero_hp > 0:
        print("1) Attack")
        print("2) Flee")
        try:
            action = int(input("Choose an action: "))
            if action == 1:
                damage_dealt = max(hero_dmg - enemy_armor, 0)
                enemy_hp -= damage_dealt
                print(f"You dealt {damage_dealt} damage to the {enemy_name}!")
                if enemy_hp <= 0:
                    print(f"You defeated the {enemy_name}!")
                    return
                
                damage_taken = max(enemy_dmg - hero_armor, 0)
                hero_hp -= damage_taken
                print(f"The {enemy_name} dealt {damage_taken} damage to you!")
                if hero_hp <= 0:
                    print(f"You have been defeated by the {enemy_name}!")
                    return
            elif action == 2:
                print("You fled from battle!")
                return
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Starting Adventure
print("You are in a forest, it is", day_night_cycle, "time and the place is crawling with monsters.")  
print("Choose a direction: North, South, West or East!")

while True:
    choice1 = input('Choose direction: ').capitalize()
    
    if choice1 == 'North':
        print("You have decided to go north. In the distance, you see smoke coming through the woods.")
        print("1) Go towards it")
        print("2) Ignore it")
        try:
            choice2 = int(input("Decide what will you do next: "))
            if choice2 == 1:
                print("You have found an abandoned camping spot with food. You eat and fall asleep.")
                print("While sleeping, you were killed by passing bandits.")
                break
            elif choice2 == 2:
                print("You ignore the smoke and continue north.")
                combat("Boss", boss_hp, boss_dmg, boss_armor)
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    elif choice1 == 'South':
        print("You have decided to go south, but the path is blocked. Choose another direction.")
    
    elif choice1 == 'West':
        print("You meet a traveling merchant who offers to take you to the city. Do you accept?")
        print("1) Yes")
        print("2) No")
        try:
            choice2 = int(input("Decide: "))
            if choice2 == 1:
                print("You accept the merchant's offer but are ambushed and killed by bandits.")
                break
            elif choice2 == 2:
                print("You decline. Soon after, you hear a scream for help. Do you go towards it?")
                print("1) Yes")
                print("2) No")
                try:
                    choice3 = int(input("Decide: "))
                    if choice3 == 1:
                        print("You try to help but are discovered and shot by an archer. You die.")
                        break
                    elif choice3 == 2:
                        print("You ignore the scream and continue your journey safely. THE END.")
                        break
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    elif choice1 == 'East':
        print("You trip over a rock, hit your head, and die. A goblin dances on your corpse.")
        break
    
    else:
        print("Invalid input. Please choose North, South, West, or East.")
