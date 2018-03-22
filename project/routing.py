import time
from binarytree import BinarySearchTree

class Routing:

    def __init__(self, cost_file, number_file=None):
        self.pricing = self.read_cost_file(cost_file)
        self.phone_nums = {}
        if number_file is not None:
            self.phone_nums = self.read_number_file(number_file)

    def read_cost_file(self, file_name):
        opened_file = open('data/{}'.format(file_name))
        file_lines = opened_file.read().splitlines()
        pricing = {}

        for line in file_lines:
            split = line.split(',')
            pricing[split[0]] = split[1]
        return pricing

    def read_number_file(self, file_name):
        opened_file = open('data/{}'.format(file_name))
        file_lines = opened_file.read().splitlines()
        return file_lines

    def find_all_matches(self, number):
        matches = {}

        # n - # of prefixes
        # m - # of numbers to look up
        for prefix in self.pricing:  # n iterations
            if number.startswith(prefix):  # O(n*m) running time
                matches[prefix] = self.pricing[prefix]
        return matches

    def find_best_match(self, number):
        matches = self.find_all_matches(number)
        longest_key = max(matches, key=len)
        match = matches[longest_key]
        return match

    def record_result(self, number, match, N):
        result_file = open("route-costs-{}.txt".format(N), "a")
        result_file.write("{}, {}\n".format(number, match))

    # Scenario 2: check route costs for multiple phone numbers
    def find_multi_numbers(self, N):
        if self.phone_nums is not None:
            for num in self.phone_nums:
                match = self.find_best_match(num)
                self.record_result(num, match, N)

class PricingNode:

    def __init__(self, prefix, cost):
        self.prefix = prefix
        self.cost = cost

    def __gt__(self, other):

    def __lt__(self, other):

    def __eq__(self, other):



class MultiRouting:

    def __init__(self, cost_file, number_file=None):
        self.pricing = self.read_cost_file(cost_file)
        self.phone_nums = {}
        if number_file is not None:
            self.phone_nums = self.read_number_file(number_file)

    def read_cost_file(self, file_name):
        opened_file = open('data/{}'.format(file_name))
        file_lines = opened_file.read().splitlines()
        binary_search_tree = BinarySearchTree()

        for line in file_lines:
            prefix, cost = line.split(',')
            item = (prefix, cost)
            binary_search_tree.insert(item)
        print(binary_search_tree)
        return binary_search_tree

    def read_number_file(self, file_name):
        opened_file = open('data/{}'.format(file_name))
        file_lines = opened_file.read().splitlines()
        return file_lines

    def find_all_matches(self, number):
        node = self.pricing.search(number)
        print(node)

def main():
    # number = '+19446855669'
    number = ('+34924199', 0.39)
    # routing = Routing('route-costs-10000000.txt', 'phone-numbers-10000.txt')
    # routing = Routing('route-costs-106000.txt')


    start_time = time.time()
    multi_routing = MutiRouting('route-costs-10.txt')
    multi_routing.find_all_matches(number)
    # print(muti_routing.root)
    # routing.find_multi_numbers(3)s
    # match = routing.find_best_match(number)
    # print('match: ' + str(match))
    end_time = time.time()
    print("Running time:", end_time - start_time)

# Scenario 1 running time: 0.017
# Scenario 2 running time: 17.69
# Scenario 3 running time:

if __name__ == "__main__":
    main()
