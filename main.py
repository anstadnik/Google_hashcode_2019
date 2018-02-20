import sys
import math

class Pizza:

    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.ingredients = 0
        self.total_area = 0
        self.data = [[]]



def count(pizza, i, j):# Oh shi...
	amount = 0# Total amount of valid slices
	for q in range(pizza.total_area):# This is offset (from 0 to max)
		for k in range(pizza.total_area):# Just as this one
			if q * k >= pizza.ingredients * 2 and q * k <= pizza.total_area and q + i < pizza.rows and k + j < pizza.cols:# If we're not out of the pizza and slise has ok size
				pepperonis = 0
				mushrooms = 0
				for foo in range(q):# Go through all pieces
					for bar in range(k):# in the slice
						if pizza.data[i + foo][j + bar] == 'T':
							pepperonis += 1
						else:
							mushrooms += 1
				if pepperonis >= pizza.ingredients and mushrooms >= pizza.ingredients:
					amount = amount + 1
	return amount


def solver(pizza):
	sum = 0
	for i in range(pizza.rows):# Iterate through
		for j in range(pizza.cols):# Each square
			sum += count(pizza, i, j)# Assume it's the top corner of the slice
		print('.', end = '', flush=True)
	return sum

if __name__ == '__main__':
	pizza = Pizza()
	if len(sys.argv) > 1:
		with open(sys.argv[1]) as f:
			meta = f.readline().split()
			pizza.rows = int(meta[0])
			pizza.cols = int(meta[1])
			pizza.ingredients = int(meta[2])
			pizza.total_area = int(meta[3])
			pizza.data = [list(line[:-1]) for line in f]
	print(solver(pizza))

