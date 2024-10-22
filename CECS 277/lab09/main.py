

from check_input import get_int_range
from random import randint
from hero import Hero
from dragon import Dragon
from fire_dragon import FireDragon
from flying_dragon import FlyingDragon
from flying_fire_dragon import FlyingFireDragon


def main():
    hero_name = input("What is your name, challenger?\n")

    print("\nWelcome to dragon training, " + hero_name)
    print("You must defeat 3 dragons.\n")

    hero = Hero(hero_name, 50) # constructs hero object and sets max hp to 50
    dragons = [FireDragon(), FlyingDragon(), FlyingFireDragon()] # a list that contains all dragons

    
    end = False
    while end is not True: # initiates our loop
        print(hero)
        # Displays a description of the dragons with their hp and special moves remaining
        for i in range(len(dragons)):
            print(f"{i + 1}. {dragons[i]}")
        dragon_to_attack = dragons[get_int_range("Choose a dragon to attack: ", 1, 3) - 1] # User chooses which dragon to attack

        print()

        weapon_select_prompt = "Attack with:\n1. Sword (2 D6)\n2. Arrow (1 D12)\nEnter weapon: "
        weapon = get_int_range(weapon_select_prompt, 1, 2) # User chooses which weapon to attack the dragon with

        print()

        combat_str = ""
        if weapon == 1:
            combat_str += hero.basic_attack(dragon_to_attack) # attacks dragon with Sword
        else:
            combat_str += hero.special_attack(dragon_to_attack) # attacks dragon with Arrow
        print(combat_str)
        
        if dragon_to_attack.hp == 0:
            dragons.remove(dragon_to_attack)
            if len(dragons) == 0:
                print("Congratulations! You have defeated all three dragons, you have passed the trials.")
                end = True
        
        attacking_dragon = dragons[randint(0, len(dragons) - 1)] # randomly selects a random (surviving) dragon to attack the hero
        dragon_move = randint(0, 1) # randomly chooses what attack the dragon attacks the hero with

        combat_str = ""
        if dragon_move == 1: # dragon does basic attack
            combat_str += attacking_dragon.basic_attack(hero)
        else: # dragon does special attack
            combat_str += attacking_dragon.special_attack(hero)
        print(combat_str)

        print()

        if hero.hp == 0:
            print("Game Over")
            end = True

main()