def move_player(player, dir, upper_bound):
    """Moves the player to the selected direction
    Args:
        player: an integer array that has x and y component for the player's position.
        dir: string to determine where to go
        upper_bound: integer of the maximuim position index
    Returns:
        none
    """
    dis = 0
    moved_pos = 0
    direction_code = 0 if ord(dir) >= ord('S') else 1
    if direction_code == 0:
        dis = -1 if dir == 'W' else 1
    else:
        dis = -1 if dir == 'A' else 1
    
    moved_pos = player[direction_code] + dis

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

    counts = [0, 0]

    check_start_point = [max(0, player[0] - 1), max(0, player[1] - 1)]
    check_end_point = [min(upper_bound, player[0] + 1), min(upper_bound, player[1] + 1)]
    
    for i in check_end_point[0] - check_start_point[0] + 1:
        for j in check_end_point[1] - check_end_point[1] + 1:
            s = map[i + check_start_point[0]][j + check_start_point[1]]
            if s == 'T':
                counts[0] += 1
            elif s == 'X':
                counts[1] += 1
    
    return counts


def main():
    player = [0, 0]
    while True:
        s = input("ASD: ").upper()
        move_player(player, s, 6)
        print(player)

main()