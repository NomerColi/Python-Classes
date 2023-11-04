import math

c = 299792458
v = float(input("Enter space ship velocity as a fraction of the speed of light: "))
d = math.sqrt(1 - ((v * c) ** 2 / c ** 2))

travelDistance = 7.4740 * (10 ** 16)

print(travelDistance)

timeOnEarth = travelDistance / (v * c)
timeOnShip = timeOnEarth * d

dayOnEarth = timeOnEarth / 86400
dayOnShip = (timeOnShip / 3600) / 24

yearOnEarth = int(dayOnEarth // 365)
yearOnShip = int(dayOnShip // 365)

dayOnEarth = int(dayOnEarth % 365)
dayOnShip = int(dayOnShip % 365)

print("Traveling to Proxima Alpha...")

print(f"An observer on Earth ages {yearOnEarth} years, {dayOnEarth} days during the trip.")
print(f"A passenger on the ship ages {yearOnShip} years, {dayOnShip} days during the trip.")