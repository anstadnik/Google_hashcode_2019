import sys
from parser import *


def output(metro, filename):
    with open(filename, "w+") as f:
        for car in metro.cars:
            print(str(len(car.rides)) + " " + " ".join([str(ride.ride_number) for ride in car.rides]), file=f)


if __name__ == '__main__':
    metro = parser(sys.argv[1])
    very_good_algo(metro)
    for car in metro.cars:
        print(car)
    output(metro, sys.argv[2])
