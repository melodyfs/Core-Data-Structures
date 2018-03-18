import time

class Routing:

    def __init__(self, file_name):
        self.pricing = self.read_costs_file(file_name)
        self.matches = {}

    def read_costs_file(self, file_name):
        opened_file = open('datafiles/{}'.format(file_name))
        file_lines = opened_file.read().splitlines()
        pricing = {}

        for line in file_lines:
            split = line.split(',')
            pricing[split[0]] = split[1]
        self.pricing = pricing
        return self.pricing

    def find_matches(self, number):
        matches = {}

        for prefix in self.pricing:
            if number.startswith(prefix):
                matches[prefix] = self.pricing[prefix]
        self.matches = matches
        print(self.matches)
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
            self.record_result(number, match)
        else:
            self.record_result(number, self.matches[number])
        return match

    def record_result(self, number, price):
        result_file = open("result.txt", "a")
        result_file.write("{}, {}\n".format(number, price))

def main():
    routing = Routing('route-costs-106000.txt')
    start_time = time.time()
    routing.find_best_match('+449932173')
    end_time = time.time()
    print("Run time:", end_time - start_time)


if __name__ == "__main__":
    main()
