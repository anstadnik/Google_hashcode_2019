import sys

class Pizza:

    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.ingredients = 0
        self.total_area = 0





def solver(pizza):
    """
    @brief      { Counts a number of all the squares }

    @return     { Returns list of all the squares (or a number?)}
    """
	for i in range(pizza.cols)


def parse_file(filename):

    with open(filename, 'r') as f:
        try:
            pizza = Pizza()

			for i in range(pizza.)
        except IOError:
            print ("Failed to read the file {}", filename)
            sys.exit(1)


if __name__ == '__main__':

    if (len(sys.argv) > 1):
        parse_file(sys.argv[1])
