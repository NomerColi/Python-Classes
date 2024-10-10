"""
A treasure hunter game where the player has to find treasures while avoiding traps.

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""
def read_map():
    """Reads the contents of the file ('map.txt') and stores
    contents in a 2D list.
    Args:
        none
    Returns:
        filled 2D list
    """
    file = open("map.txt")
    list2d = []
    for row in file:
        list = []
        for item in row:
            if item != ' ' and item != '\n':
                list.append(item)
        list2d.append(list)
    return list2d


def display_map(map, player):
    """Passes in the map and the user's location.
    Args:
        map: 2d array of the map for the player
        player: an integer array that has x and y component for the player's position.
    Returns:
        none
    """
    for i in range(len(map)):
        for j in range(len(map[i])):
            s = map[i][j]
            if i == player[0] and j == player[1]:
                s = 'P'
            print(s, end=' ')
        print()


def move_player(player, dir, upper_bound):
    """Moves the player to the selected direction
    Args:
        player: an integer array that has x and y component for the player's position.
        dir: string to determine where to go
        upper_bound: integer of the maximuim position index
    Returns:
        none
    """
    dis = 0 #initializes distance to move.
    moved_pos = 0 #initializes new position.
    # if 'dir' is W or S
    direction_code = 0 if ord(dir) >= ord('S') else 1
    if direction_code == 0:
        dis = -1 if dir == 'W' else 1
    else:
        dis = -1 if dir == 'A' else 1
    
    moved_pos = player[direction_code] + dis #calculate the new position.

    if moved_pos < 0 or moved_pos > upper_bound:
        print("You cannot move that direction.")
    else:
        player[direction_code] = moved_pos
        

def count_treasures_traps(map, player, upper_bound):
    """Iterates through the surrounding spaces of the user’s current location.
    Args:
        map: 2d array of the map
        player: array of the player's position
        upper_bound: max boundary of the map
    Returns:
        a count of the number of treasures and traps nearby
    """

    counts = [0, 0] #Initialize counters for treasures and traps

    #defines the bounds for checking surrounding tiles
    check_start_point = [max(0, player[0] - 1), max(0, player[1] - 1)]
    check_end_point = [min(upper_bound, player[0] + 1), min(upper_bound, player[1] + 1)]
    
    for i in range(check_start_point[0], check_end_point[0] + 1):
        for j in range(check_start_point[1], check_end_point[1] + 1):
            s = map[i][j]
            #print(f"i: {i} j: {j} s: {s}")
            if s == 'T':
                counts[0] += 1
            elif s == 'X':
                counts[1] += 1
    
    return counts 
    

def main():
    solution_map = read_map()
    user_map2d = [['.' for j in range(7)] for i in range(7)]
   
    player = [0, 0] # 1D list that initializes user's location at the top left corner (0, 0).
    upper_bound = 6 # Sets the maximum boundary for the map.

    # initialize trap and treasure counters
    treasure_count = 0
    trap_count = 0

    print("Treasure Hunt!")
    print("Find the 7 treasures without getting\ncaught in a trap. Look around to spot\nnearby traps and treasures.")
    # loop used here
    # result: 0:ongoing, 1:player won, -1:player lost
    result = 0
    while result == 0:
        display_map(user_map2d, player)
        user_input = input("Enter Direction: (WASD or L to look around\nor Q to quit): ").upper()
        if len(user_input) != 1 or user_input not in "WASDLQ": # checks for invalid inputs
            print("Invalid input.")
        elif user_input in "WASD":
            move_player(player, user_input, upper_bound)
            # checks what the player is standing on
            s = solution_map[player[0]][player[1]]
            user_map2d[player[0]][player[1]] = s
            if s == 'T': 
                print("You found treasure!")
                treasure_count += 1
                # when the player collects less than 7 treasures
                if treasure_count < 7:
                    print("There are " + str(7 - treasure_count) + " treasures remaining.")
                else:
                    result = 1
            elif s == 'X':
                print("You were caught in a trap!")
                result = -1
        elif user_input == "L":
            # calls for hint
            treasure_count, trap_count = count_treasures_traps(solution_map, player, upper_bound)
            print("You detect " + str(treasure_count) + " treasures nearby.")
            print("You detect " + str(trap_count) + " traps nearby.")
            # 
            user_map2d[player[0]][player[1]] = str(trap_count)
        elif user_input == 'Q':
            exit()
    
    #displays final result
    print("You found " + str(treasure_count) + " treasures.")
    display_map(user_map2d, player)
    if result == 1:
        print("You won!")
    elif result == -1:
        print("Game Over!")


main()
