class Ride:
	def __init__(self, start_row, start_col, final_row, final_col, start_time, final_time):
		self.start_row = start_row
		self.start_col = start_col
		self.final_row = final_row
		self.final_col = final_col
		self.start_time = start_time
		self.final_time = final_time

	def __str__(self):
		return "[{}, {}] -> [{}, {}] in time [{}, {}]".format(self.start_row, self.start_col, self.final_row,
		self.final_col, self.start_time, self.final_time)

class Car(object):
	"""docstring for Car"""
	def __init__(self, row, col, time_elapsed):
		super(Car, self).__init__()
		self.row = row
		self.col = col
		self.time_elapsed = time_elapsed
		self.rides = []

	def __str__(self):
		return "[{}, {}] | current time {}".format(self.row, self.col, self.time_elapsed)


class Metropolis:
	def __init__(self, nrows, ncols, nvehicles, nrides, bonus, time, rides: list):
		self.nrows = nrows
		self.ncols = ncols
		self.nvehicles = nvehicles
		self.nrides = nrides
		self.bonus = bonus
		self.time = time
		self.rides = rides
		self.cars = [Car(0, 0, 0) for car in range(nvehicles)]

	def __str__(self):
		return "Grid [{}, {}] | Nvehicles: {} | Nrides: {} | Bonus: {} | Time: {}".format(
		self.nrows, self.ncols, self.nvehicles, self.nrides, self.bonus, self.time)


def parser(filename):
	with open(filename) as f:
		nrows, ncols, nvehicles, nrides, bonus, nsteps = map(int, f.readline().split())
		rides = [f.readline().split() for n in range(nrides)]
		metro = Metropolis(nrows, ncols, nvehicles, nrides, bonus, nsteps, [Ride(*ride) for ride in rides])
		print(metro)
		[print(ride) for ride in metro.rides]
		[print(car) for car in metro.cars]
