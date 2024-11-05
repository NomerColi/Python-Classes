""" Dungeons and Monsters Game

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import random
import check_input
from entity import Entity
from hero import Hero
from enemy import Enemy
from map import Map

def main():
    hero_name = input("What is your name, traveler? ")

    hero = Hero(hero_name)
    map = Map()

    end = False
    while end is False:
        print(hero)
        map.show_map(hero.loc)

        print()

        print("1. Go North")
        print("2. Go South")
        print("3. Go East")
        print("4. Go West")
        print("5. Quit")
        choice = check_input.get_int_range("Enter choice: ", 1, 5)

        ## Hero movement choice
        result = ''
        if choice == 1:
            result = hero.go_north()
        elif choice == 2:
            result = hero.go_south()
        elif choice == 3:
            result = hero.go_east()
        elif choice == 4:
            result = hero.go_west()        
        else:
            print("Quit")
            break
            
        ## result
        # the Hero is blocked by the bounds of the map
        if result == 'o':
            print("You cannot go that way...")
        # the Hero finds nothing
        elif result == 'n':
            map.reveal(hero.loc)
            print("There is nothing here...")
        # the Hero encounters an enemy
        elif result == 'm':
            map.reveal(hero.loc)

            enemy = Enemy()
            print("You encounter a " + enemy.__str__())
            
            combat_end = False
            while combat_end is False:
                print("1. Attack " + enemy.name)
                print("2. Run away")
                combat_choice = check_input.get_int_range("Enter choice: ", 1, 2)

                if combat_choice == 1:
                    # Hero attacks the enemy
                    print(hero.attack(enemy))
                    # if the enemy is slain, remove the enemy from the map
                    if enemy.hp == 0:
                        print("You have slain a " + enemy.name)
                        combat_end = True
                        map.remove_at_loc(hero.loc)
                        break

                    # The enemy attacsk Hero
                    print(enemy.attack(hero))
                    # if the Hero is slain, end the game
                    if hero.hp == 0:
                        print("You were slain by a " + enemy.name + ".\nGame Over")
                        combat_end = True
                        end = True
                        break

                else:
                    print("You ran away!")

                    # move the Hero by 1 in a random directio
                    rand_dir = random.randint(1, 4)
                    if rand_dir == 1:
                        hero.go_north()
                    elif rand_dir == 2:
                        hero.go_south()
                    elif rand_dir == 3:
                        hero.go_east()
                    elif rand_dir == 4:
                        hero.go_west()
                    
                    map.reveal(hero.loc)
                    combat_end = True


        # the Hero comes back to the start location
        elif result == 's':
            print("You have wound up back at the start...")
        # the Hero finds a health potion
        elif result == 'i':
            map.reveal(hero.loc)
            
            if hero.hp != 25:
                print("You found a Health Potion! You have drank it to restore your health.")
                hero.heal()
                map.remove_at_loc(hero.loc)
            else:
                print("You found a Health Potion, but you left the potion for later.")
                continue
        # the Hero reaches the destination
        else:
            print("Congratulations! You have found the exit.\nGame Over")
            end = True
        
        print()
    
main()
