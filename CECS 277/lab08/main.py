""" Racing Game

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
from truck import Truck
import random
import check_input


# Function to create the track
def create_track():
    """Creates tracks with obstacles.
    Args:
        none
    Returns:
        a 2D string list of tracks
    """
    # Create a 2D list for the track with 3 lanes (for 3 vehicles)
    tracks = [['-' for _ in range(100)] for _ in range(3)]
    
    # Randomly place two obstacles in each lane, not at the start (0) or finish (99)
    for lane in range(3):
        obstacle_positions = random.sample(range(1, 99), 2)  # Pick 2 unique positions
        for pos in obstacle_positions:
            tracks[lane][pos] = '0'  # '0' represents an obstacle
    
    return tracks

# Function to display the track
def display_track(tracks, vehicles, player_lane: int):
    """Displays the tracks with vehicles.
    Args:
        tracks (2D str[]): tracks to display
        vehicles (Vehicle[]): three vehicles to display
        player_lane (int): the lane of the player
    Returns:
        none
    """
    for i in range(len(tracks)):
        temp = tracks[i]
        initial = ''
        if i == player_lane:
            initial = 'P'
        else:
            initial = vehicles[i].initial

        temp[min(vehicles[i].position, 99)] = initial
        print("".join(temp))


def move_vehicle(vehicle: Vehicle, track, action: int) -> str:
    """Moves a vehicle acacording to an action
    Args:
        vehicle (Vehicle): a vehicle to move
        track (str[]): a track where the vehicle is
        action (int): an action among fast, slow, and special move
    Returns:
        a string of the movement result
    """
    dist = -1
    try:
        # finds an obstacle starting from the right of the vehicle
        dist = track[vehicle.position + 1:].index('0') + 1
    # if there is no more obstacle to pass
    except ValueError:
        dist = 99
    
    if action == 1:
        return vehicle.fast(dist)
    elif action == 2:
        return vehicle.slow(dist)
    else:
        return vehicle.special_move(dist)

def get_random_action(energy) -> int:
    """Gets a random action for a vehicle being controlled by the computer
    Args:
        energy (int): the remaining energy of this vehicle
    Returns:
        an integer for the action
    """
    action = 0
    # if the vehicle has less then 5 energy, just go with 'slow'
    if energy < 5:
        action = 2 # slow
    else:
        rand = random.randint(0, 9)

        # if the vehicle has less then 15 energy, select between 'fast' and 'slow'
        if energy < 15:
            if rand <= 4:
                action = 1 # fast
            else:
                action = 2 # slow
        # if the vehicle has more than or equal to 15 energy, any action is selectable
        else:
            if rand <= 2:
                action = 1 # fast
            elif rand <= 6:
                action = 2 # slow
            else:
                action = 3 # special
    return action


def main():
    tracks = create_track()

    # instantiates vehicles
    vehicles = []
    vehicles.append(Car())
    vehicles.append(Motorcycle())
    vehicles.append(Truck())

    winners = []

    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (player = 'P'). Slow down for obstacles ('0') or else you'll crash!")
    for i in range(3):
        print(str(i + 1) + " " + vehicles[i].description_string())
    vehicle_select = check_input.get_int_range("Choose your vehicle (1-3): ", 1, 3) - 1

    print()

    end = False
    while end is False:

        for vehicle in vehicles:
            print(vehicle)
        display_track(tracks, vehicles, vehicle_select)

        # if the player's vehicle has not reached the destination yet
        if vehicles[vehicle_select].position < 99:
            player_action = check_input.get_int_range("Choose action (1. Fast, 2. Slow, 3. Special Move): ", 1, 3)
        print("")

        for i in range(3):
            # if this vehicle has reached the destination, do nothing
            if vehicles[i].position >= 99:
                continue

            action = player_action
            # if this vehicle is not player's
            if i != vehicle_select:
                action = get_random_action(vehicles[i].energy)

            # marks the previous position
            tracks[i][vehicles[i].position] = '*'
            
            print(move_vehicle(vehicles[i], tracks[i], action))

            if vehicles[i].position >= 99:
                winners.append(i)
                if len(winners) == 3:
                    end = True

        print()

    # final result
    display_track(tracks, vehicles, vehicle_select)
    print("1st place:", vehicles[winners[0]])
    print("2nd place:", vehicles[winners[1]])
    print("3rd place:", vehicles[winners[2]])

    
main()
