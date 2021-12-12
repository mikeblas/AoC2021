
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




with open('input.txt') as my_file:
    input_lines = my_file.readlines()
input_lines = [s.strip() for s in input_lines]
line_count = len(input_lines)

print(f"{line_count} lines read")
# pprint.pprint(input_lines)

the_graph = Graph()

for line in input_lines:
    fields = line.split("-")
    print(f"{fields[0]} to {fields[1]}")
    the_graph.add_point(fields[0], fields[1])

the_graph.all_traversals()

print(f"{the_graph.paths}")
print(f"{len(the_graph.paths)}")
