import heapq
import sys
import pprint
from queue import PriorityQueue

with open('input.txt') as my_file:
    input_lines = my_file.readlines()
input_lines = [s.strip() for s in input_lines]
line_count = len(input_lines)
print(f"{line_count} lines read")

cells = [[int(x) for x in line] for line in input_lines]
print(f"width is {len(cells[0])}")
print(f"height  is {len(cells)}")


class CellChoice:
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance

    def __repr__(self):
        return f"{self.x}, {self.y}: {self.distance}"

    def __lt__(self, other):
        if self.distance == other.distance:
            if (self.x != other.x):
                return self.x < other.x
            else:
                return self.y < other.y
        else:
            return self.distance < other.distance



def min_cost3(cols, rows):

    tc = [[sys.maxsize for x in range(cols)] for y in range(rows)]
    tc[0][0] = 0

    deltas = [ (-1, 0), (0, 1), (1, 0), (0, -1) ]

    # start at 0,0
    pq = [CellChoice(0, 0, 0)]
    heapq.heapify(pq)

    while len(pq) > 0:

        this_cell = pq.pop(0)

        for (dx, dy) in deltas:
            x = dx + this_cell.x
            y = dy + this_cell.y

            if x < 0 or y < 0:
                continue
            if x >= cols or y >= rows:
                continue

            if tc[y][x] > tc[this_cell.y][this_cell.x] + cells[y][x]:

                if tc[y][x] != sys.maxsize:
                    for n in range(len(pq)):
                        if pq[n].x == x and pq[n].y == y:
                            del [n]
                            heapq.heapify(pq)
                            break

                tc[y][x] = tc[this_cell.y][this_cell.x] + cells[y][x]
                pq.append(CellChoice(x, y, tc[y][x]))
                heapq.heapify(pq)

    return tc[rows-1][cols-1]



print(min_cost3(len(cells[0]), len(cells)))
