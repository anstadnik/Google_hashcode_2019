class Ride:
	def __init__(self, ridenumber, start_row, start_col, final_row, final_col, start_time, final_time):
		self.ride_number = ridenumber
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
	def __init__(self, car_number, row, col, time_elapsed):
		super(Car, self).__init__()
		self.car_number = car_number
		self.row = row
		self.col = col
		self.time_elapsed = time_elapsed
		self.rides = []

	def __str__(self):
		return "Car [{}, {}] elapsed time {}\nRides:\n{}".format(self.row, self.col, self.time_elapsed,
		[str(ride) for ride in self.rides])

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
	car = Car(0, 0, 0, 0)
	try_this = sorted(rides, key=lambda ride: time_needed(car, ride))
	return try_this[:ncars]

def each_car(car, rides: list)->Ride:
	return sorted(rides, key=lambda ride: time_needed(car, ride))[0]


def very_good_algo(metro):
	while metro.rides:
		for i in range(metro.nvehicles):
			if not metro.rides:
				break
			best_ride = each_car(metro.cars[i], metro.rides)
			metro.cars[i].row = best_ride.final_row
			metro.cars[i].col = best_ride.final_col
			metro.cars[i].time_elapsed += best_ride.time_needed
			metro.cars[i].rides.append(best_ride)
			metro.rides.remove(best_ride)
		print("rides left:")
		[print(ride) for ride in metro.rides]


class Metropolis:
	def __init__(self, nrows, ncols, nvehicles, nrides, bonus, time, rides: list):
		self.nrows = nrows
		self.ncols = ncols
		self.nvehicles = nvehicles
		self.nrides = nrides
		self.bonus = bonus
		self.time = time
		self.rides = rides
		self.cars = [Car(i + 1, 0, 0, 0) for i in range(nvehicles)]

	def __str__(self):
		return "Grid [{}, {}] | Nvehicles: {} | Nrides: {} | Bonus: {} | Time: {}".format(
		self.nrows, self.ncols, self.nvehicles, self.nrides, self.bonus, self.time)


def parser(filename):
	with open(filename) as f:
		nrows, ncols, nvehicles, nrides, bonus, nsteps = map(int, f.readline().split())
		rides = [f.readline().split() for n in range(nrides)]
		print(rides)
		metro = Metropolis(nrows, ncols, nvehicles, nrides, bonus, nsteps,
			[Ride(i, *map(int,ride)) for i, ride in zip(range(nrides), rides)])
		# print(metro)
		# [print(ride) for ride in metro.rides]
		# [print(car) for car in metro.cars]
		return metro
