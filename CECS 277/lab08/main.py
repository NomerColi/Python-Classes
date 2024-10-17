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
    # Create a 2D list for the track with 3 lanes (for 3 vehicles)
    track = [[' ' for _ in range(100)] for _ in range(3)]
    
    # Randomly place two obstacles in each lane, not at the start (0) or finish (99)
    for lane in range(3):
        obstacle_positions = random.sample(range(1, 99), 2)  # Pick 2 unique positions
        for pos in obstacle_positions:
            track[lane][pos] = 'X'  # 'X' represents an obstacle
    
    return track

# Function to display the track
def display_track(track, vehicles):
    for lane in range(len(track)):
        # Update the track with the vehicle's positions
        for vehicle in vehicles:
            if vehicle.position < 100:
                track[lane][vehicle.position] = vehicle.name[0]  # Display first letter of vehicle's name
        # Print the current lane
        print(''.join(track[lane]))


def main():
    track = create_track()
