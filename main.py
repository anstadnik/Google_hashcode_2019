import sys
from parser import *


if __name__ == '__main__':
	metro = parser(sys.argv[1])
	for i in metro.rides:
		print(time_needed(Car(0, 0, 0), i), i)
	very_good_algo(metro)
