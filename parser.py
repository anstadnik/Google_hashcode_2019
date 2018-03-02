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
                                                                 "\n".join([str(ride) for ride in self.rides]))


class Metropolis:
    def __init__(self, nrows, ncols, nvehicles, nrides, bonus, time, rides: list):
        self.nrows = nrows
        self.ncols = ncols
        self.nvehicles = nvehicles
        self.nrides = nrides
        self.bonus = bonus
        self.time = time
        self.rides = rides
        self.cars = [Car(i, 0, 0, 0) for i in range(1, nvehicles + 1)]

    def __str__(self):
        return "Grid [{}, {}] | Nvehicles: {} | Nrides: {} | Bonus: {} | Time: {}".format(
            self.nrows, self.ncols, self.nvehicles, self.nrides, self.bonus, self.time)


def manhetten_distance(x1, y1, x2, y2):
    """
    Calculate manhatten distance
    :param x1: row
    :param y1: col
    :param x2: row
    :param y2: col
    :return:
    """
    return abs(x2 - x1) + abs(y2 - y1)


def time_needed(car: Car, ride: Ride):
    """row это х, col это y"""
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


def custom_sort(time, car: Car, ride: Ride):
    if ride.start_col == car.col and ride.start_row == car.row:
        return int(time_needed(car, ride) * 0.9)
    elif manhetten_distance(car.row, car.col, ride.start_row, ride.start_col) < 5 and \
            ride.start_time <= car.time_elapsed + manhetten_distance(car.row, car.col, ride.start_row, ride.start_col):
        return int(time_needed(car, ride) * 0.6)
    elif car.time_elapsed + ride.time_needed > time:
        return int(time_needed(car, ride) * 100)
    else:
        return time_needed(car, ride)


def each_car(time, car, rides: list)->Ride:
    return min(rides, key=lambda ride: custom_sort(time, car, ride))


def very_good_algo(metro: Metropolis):
    while metro.rides:
        car = min(metro.cars, key=lambda car: len(car.rides))
        best_ride = each_car(metro.time, car, metro.rides)
        car.row = best_ride.final_row
        car.col = best_ride.final_col
        if car.time_elapsed < best_ride.start_time:
            car.time_elapsed = best_ride.start_time + best_ride.time_needed
        else:
            car.time_elapsed += best_ride.time_needed
        car.rides.append(best_ride)
        metro.rides.remove(best_ride)
        # print("rides left:")
        # [print(ride) for ride in metro.rides]


def parser(filename):
    with open(filename) as f:
        nrows, ncols, nvehicles, nrides, bonus, nsteps = map(int, f.readline().split())
        rides = [f.readline().split() for n in range(nrides)]
        metro = Metropolis(nrows, ncols, nvehicles, nrides, bonus, nsteps,
                           [Ride(i, *map(int,ride)) for i, ride in zip(range(nrides), rides)])
        # print(metro)
        # [print(ride) for ride in metro.rides]
        # [print(car) for car in metro.cars]
        return metro
