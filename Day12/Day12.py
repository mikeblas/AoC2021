import pprint
import time


class Graph:

    def __init__(self):
        self.points = dict()
        self.paths = []

    def add_point(self, start, end):
        if start not in self.points:
            self.points[start] = []
        if end not in self.points:
            self.points[end] = []
        self.points[end].append(start)
        self.points[start].append(end)

    @staticmethod
    def reentrant(next_place):
        if next_place == next_place.upper():
            return True
        return False

    def more_traversals(self, place, place_paths, visited):

        for next_place in place_paths:
            if next_place == "end":
                self.paths.append(visited + [place] + ["end"])
            elif Graph.reentrant(next_place) or next_place not in visited:
                self.more_traversals(next_place, self.points[next_place], visited + [place])

    def all_traversals(self):

        self.paths.clear()
        visited = []

        self.more_traversals("start", self.points["start"], [])

        return self.paths

    @staticmethod
    def get_histogram(visited):
        histogram = {}
        for place in visited:
            if Graph.reentrant(place):
                continue
            if place not in histogram:
                histogram[place] = 1
            else:
                histogram[place] += 1
        return histogram

    @staticmethod
    def can_enter(visited, target, mode):

        # can't enter start
        if target == 'start':
            return 2

        # if reentrant, we can always visit
        if Graph.reentrant(target):
            return mode

        # if never entered, we can visit
        if target not in visited:
            return mode

        if mode == 1:
            return 2

        # target was visited before, but we must be sure no other was visited before
        histogram = Graph.get_histogram(visited)
        if not any(v >= 2 for v in iter(histogram.values())):
            # print(f"{visited} towards {target} == TRUE")
            return 1

        # otherwise, no
        return 2

    def more_traversals2(self, place, place_paths, visited, mode):

        if place == "end":
            self.paths.append(visited + ["end"])
            # print(f"added {visited + ['end']}")
        else:
            for next_place in place_paths:
                result = Graph.can_enter(visited + [place], next_place, mode)
                if result in [0, 1]:
                    self.more_traversals2(next_place, self.points[next_place], visited + [place], result)


    def all_traversals2(self):

        self.paths.clear()
        visited = []

        self.more_traversals2("start", self.points["start"], [], 0)

        return self.paths



with open('input.txt') as my_file:
    input_lines = my_file.readlines()
input_lines = [s.strip() for s in input_lines]
line_count = len(input_lines)

print(f"{line_count} lines read")
# pprint.pprint(input_lines)

the_graph = Graph()

for line in input_lines:
    fields = line.split("-")
    # print(f"{fields[0]} to {fields[1]}")
    the_graph.add_point(fields[0], fields[1])

the_graph.all_traversals()

# print(f"{the_graph.paths}")
print(f"{len(the_graph.paths)}")

start = time.time_ns()
the_graph.all_traversals2()
end = time.time_ns()
# pprint.pprint(the_graph.paths)
print(f"{len(the_graph.paths)}")
print(f"{(end - start) / (10**9)} s elapsed")
