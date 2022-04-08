import time
from pop import Pilot

Car = Pilot.AutoCar()

Car.camPan(-90)
for angle in range(-90, 90, 5):
    Car.camPan(angle)

time.sleep(1)
Car.camPan(0)

time.sleep(3)

Car.camTilt(0)
for angle in range(0, 180, 5):
    Car.camTilt(angle)

time.sleep(1)
Car.camTilt(0)
