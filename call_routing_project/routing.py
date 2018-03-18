import time

class Routing:

    def __init__(self, cost_file, number_file=None):
        self.pricing = self.read_cost_file(cost_file)
        self.matches = {}
        self.phone_nums = self.read_number_file(number_file)

    def read_cost_file(self, file_name):
        opened_file = open('datafiles/{}'.format(file_name))
        file_lines = opened_file.read().splitlines()
        pricing = {}

        for line in file_lines:
            split = line.split(',')
            pricing[split[0]] = split[1]
        return pricing

    def read_number_file(self, file_name):
        opened_file = open('datafiles/{}'.format(file_name))
        file_lines = opened_file.read().splitlines()
        return file_lines


    def find_matches(self, number):
        matches = {}

        for prefix in self.pricing:
            if number.startswith(prefix):
                matches[prefix] = self.pricing[prefix]
        self.matches = matches
        return self.matches

    def find_best_match(self, number):
        self.find_matches(number)
        match = 0

        if len(self.matches) > 1:
            str_len = 0
            for m in self.matches:
                if len(m) > str_len:
                    str_len = len(m)
                    match = self.matches[m]
        elif len(self.matches) == 1:
            match = list(self.matches.values())[0]
        return match

    def record_result(self, number, match, N):
        result_file = open("route-costs-{}.txt".format(N), "a")
        result_file.write("{}, {}\n".format(number, match))

    def find_multi_numbers(self):
        if self.phone_nums is not None:
            for num in self.phone_nums:
                match = self.find_best_match(num)
                self.record_result(num, match, 2)



def main():
    number = '+19446855669'
    routing = Routing('route-costs-106000.txt', 'phone-numbers-1000.txt')
    start_time = time.time()
    routing.find_multi_numbers()
    # match = routing.find_best_match(number)
    # print('match: ' + str(match))
    end_time = time.time()
    print("Running time:", end_time - start_time)

# Scenario 2 running time: 17.69

if __name__ == "__main__":
    main()
