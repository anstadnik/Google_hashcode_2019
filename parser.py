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


class Metropolis:
	def __init__(self, nrows, ncols, nvehicles, nrides, bonus, nsteps, rides: list):
		self.nrows = nrows
		self.ncols = ncols
		self.nvehicles = nvehicles
		self.nrides = nrides
		self.bonus = bonus
		self.nsteps = nsteps
		self.rides = rides



def parser(filename):
	with open(filename) as f:
		nrows, ncols, nvehicles, nrides, bonus, nsteps = map(int, f.readline().split())
		rides = [f.readline().split() for n in range(nrides)]
		metro = Metropolis(nrows, ncols, nvehicles, nrides, bonus, nsteps, [Ride(*ride) for ride in rides])
		[print(ride) for ride in metro.rides]
