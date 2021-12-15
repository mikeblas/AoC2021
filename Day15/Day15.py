import heapq
import sys
import pprint

class CellChoice:
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance

    def __repr__(self):
        return f"{self.x}, {self.y}: {self.distance}"

    def __lt__(self, other):
        if self.distance == other.distance:
            if self.x != other.x:
                return self.x < other.x
            else:
                return self.y < other.y
        else:
            return self.distance < other.distance


def get_cell_part1(cells, x, y):
    return cells[y][x]

def get_cell_part2(cells, x, y):

    width = len(cells[0])
    height = len(cells)

    x_block = int(x / width)
    y_block = int(y / height)

    val = cells[y % height][x % width]
    val += x_block + y_block

    val = ((val - 1) % 9) + 1

    return val





def min_cost3(cells, dimensions, get_cell):

    cols = dimensions[0]
    rows = dimensions[1]
    tc = [[sys.maxsize for x in range(cols)] for y in range(rows)]
    tc[0][0] = 0

    mql = 0
    iterations = 0

    deltas = [ (-1, 0), (0, 1), (1, 0), (0, -1) ]

    # start at 0,0
    pq = [CellChoice(0, 0, 0)]
    heapq.heapify(pq)

    while len(pq) > 0:

        if len(pq) > mql:
            mql = len(pq)
            # print(f"mql = {mql} at iteration {iterations}")
        iterations += 1

        # this_cell = pq.pop(0)
        this_cell = heapq.heappop(pq)

        for (dx, dy) in deltas:
            x = dx + this_cell.x
            y = dy + this_cell.y

            if x < 0 or y < 0:
                continue
            if x >= cols or y >= rows:
                continue

            if tc[y][x] > tc[this_cell.y][this_cell.x] + get_cell(cells, x, y):

                if tc[y][x] != sys.maxsize:
                    for n in range(len(pq)):
                        if pq[n].x == x and pq[n].y == y:
                            del [n]
                            heapq.heapify(pq)
                            break

                tc[y][x] = tc[this_cell.y][this_cell.x] + get_cell(cells, x, y)
                heapq.heappush(pq, CellChoice(x, y, tc[y][x]))

    ret = tc[rows-1][cols-1]
    print(f"answer = {ret}, after {iterations} iterations and a max queue length of {mql}")

    return ret


def test_part2(cells):
    for x in range(len(cells[0])*5):
        print(f"{get_cell_part2(cells, x, 0)} ", end='')
    print()

    test_cells = [[8]]
    for y in range(5):
        for x in range(5):
            print(f"{get_cell_part2(test_cells, x, y)} ", end='')
        print()


def main():
    with open('input.txt') as my_file:
        input_lines = my_file.readlines()
    input_lines = [s.strip() for s in input_lines]
    line_count = len(input_lines)
    print(f"{line_count} lines read")

    cells = [[int(x) for x in line] for line in input_lines]
    print(f"width is {len(cells[0])}")
    print(f"height  is {len(cells)}")

    dim = (len(cells[0]), len(cells))
    print(min_cost3(cells, dim, get_cell_part1))

    # test_part2(cells)

    print(min_cost3(cells, tuple([5*x for x in dim]), get_cell_part2))


if __name__ == '__main__':
    main()

