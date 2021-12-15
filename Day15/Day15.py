import sys
import pprint

with open('input.txt') as my_file:
    input_lines = my_file.readlines()
input_lines = [s.strip() for s in input_lines]
line_count = len(input_lines)
print(f"{line_count} lines read")

cells = [[int(x) for x in line] for line in input_lines]
print(f"width is {len(cells[0])}")
print(f"height  is {len(cells)}")

calls = 0

def min_cost(x, y):

    global calls
    calls += 1
    if x < 0 or y < 0:
        ret = sys.maxsize
    elif x == 0 and y == 0:
        ret = 0
    else:
        ret = cells[y][x] + min(min_cost(x-1, y),  min_cost(x, y-1))

    return ret


def min_cost2(x, y):

    tc = [[None for x2 in range(x+1)] for y2 in range(y+1)]
    # tc[0][0] = cells[0][0]
    tc[0][0] = 0

    for i in range(1, y + 1):
        tc[i][0] = tc[i - 1][0] + cells[i][0]

    for j in range(1, x + 1):
        tc[0][j] = tc[0][j - 1] + cells[0][j]

    for i in range(y + 1):
        for j in range(x + 1):
            if tc[i][j] is None:
                s = "    "
            else:
                s = f"{tc[i][j]:3} "
            print(f"{s}", end='')
        print()


    print("-------")

    for j in range(1, x + 1):
        for i in range(1, y + 1):
            left = tc[i][j]
            tc[i][j] = min(tc[i - 1][j], tc[i][j - 1]) + cells[i][j]

    for i in range(y + 1):
        for j in range(x + 1):
            print(f"{tc[i][j]:3} ", end='')
        print()

    # pprint.pprint(tc)
    return tc[y][x]


# print(min_cost(len(cells[0])-1, len(cells)-1))
print(calls)

print(min_cost2(len(cells[0])-1, len(cells)-1))
