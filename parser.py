class Ride:
	def __init__(self, start_row, start_col, final_row, final_col, start_time, final_time):
		self.start_row = start_row
		self.start_col = start_col
		self.final_row = final_row
		self.final_col = final_col
		self.start_time = start_time
		self.final_time = final_time
		self.time_needed = manhetten_distance(start_row, start_col, final_row, final_col)

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

def manhetten_distance(x1, y1, x2, y2):
	return abs(x2 - x1) + abs(y2 - y1)

def time_needed(car: Car, ride: Ride):
	#row это х, col это y
	ret = manhetten_distance(car.row, car.col, ride.start_row, ride.start_col)
	if ret + car.time_elapsed < ride.start_time:
		ret = ride.start_time
	ret += ride.time_needed
	return ret

def first_n(ncars, rides: list):
	# пожалуйста
	eta_huina = [Ride(0, 0, 42, 42, 0, 100000) for i in range(ncars)]
	car = Car(0, 0, 0)
	for ride in rides:
		if time_needed(car, ride) < eta_huina[ncars - 1].time_needed:
			eta_huina.pop(0)
			eta_huina.append(ride)
	return eta_huina


def very_good_algo(metro):
	i = 0

	for n in first_n(metro.nvehicles, metro.rides):
		if (n.time_needed < 99999):
			metro.cars[i].row = n.final_row
			metro.cars[i].col = n.final_col
			metro.cars[i].time_elapsed += n.time_needed
			print(metro.cars[i])
			i += 1




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

	def very_good_algo(self):
		# Init n vehicles (find first rides)
		# Find new ride for car with the smallest value of time_elapsed
		# Do while time_counter < time OR cnt_rides < nrides
		i = 0
		for n in first_n(self.nvehicles, self.rides):
			if (n < 99999):
				self.cars[i]


def parser(filename):
	with open(filename) as f:
		nrows, ncols, nvehicles, nrides, bonus, nsteps = map(int, f.readline().split())
		rides = [f.readline().split() for n in range(nrides)]
		metro = Metropolis(nrows, ncols, nvehicles, nrides, bonus, nsteps, [Ride(*map(int,ride)) for ride in rides])
		print(metro)
		[print(ride) for ride in metro.rides]
		[print(car) for car in metro.cars]
		return metro
