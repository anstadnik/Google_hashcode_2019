import sys
from parser import parser, very_good_algo, Metropolis


if __name__ == '__main__':
	metro = parser(sys.argv[1])
	very_good_algo(metro)
