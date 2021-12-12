import pprint

class Graph:

    def __init__(self):
        self.points = dict()

    def add_point(self, start, end):
        if start not in self.points:
            self.points[start] = []
        if end not in self.points:
            self.points[end] = []
        self.points[end].append(start)
        self.points[start].append(end)
        self.paths = []

    def reentrant(self, next_place):
        if next_place == next_place.upper():
            return True
        return False

    def more_traversals(self, place, place_paths, visited):

        for next_place in place_paths:
            if next_place == "end":
                self.paths.append(visited + [place] + ["end"])
            elif self.reentrant(next_place) or next_place not in visited:
                self.more_traversals(next_place, self.points[next_place], visited + [place])

    def all_traversals(self):

        self.paths.clear()
        visited = []

        self.more_traversals("start", self.points["start"], [])

        return self.paths


    def get_histogram(self, visited):
        histogram = {}
        for place in visited:
            if self.reentrant(place):
                continue
            if place not in histogram:
                histogram[place] = 1
            else:
                histogram[place] += 1
        return histogram


    def can_enter(self, visited, target):

        # can't enter start
        if target == 'start':
            return False

        # if reentrant, we can always visit
        if self.reentrant(target):
            return True

        # if never entered, we can visit
        if target not in visited:
            return True

        # target was visited before, but we must be sure no other was visited before
        histogram = self.get_histogram(visited)
        if not any(v >= 2 for v in iter(histogram.values())):
            # print(f"{visited} towards {target} == TRUE")
            return True

        # otherwise, no
        return False

    def more_traversals2(self, place, place_paths, visited):

        if place == "end":
            self.paths.append(visited + ["end"])
            # print(f"added {visited + ['end']}")
        else:
            for next_place in place_paths:
                if self.can_enter(visited + [place], next_place):
                    self.more_traversals2(next_place, self.points[next_place], visited + [place])


    def all_traversals2(self):

        self.paths.clear()
        visited = []

        self.more_traversals2("start", self.points["start"], [])

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


# 195155 is too high
the_graph.all_traversals2()
# pprint.pprint(the_graph.paths)
print(f"{len(the_graph.paths)}")
