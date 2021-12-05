import pprint

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if other.x == self.x and other.y == self.y:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.x) * 31 + hash(self.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"

def coord_from_string(str):
    parsed = str.split(",")
    x = int(parsed[0])
    y = int(parsed[1])
    # print(f"got {x}, {y}")
    return Coord(x, y)

def process_points(the_map, start_coord, end_coord, only_right):

    dx, dy = (0, 0)
    if start_coord.x == end_coord.x:
        dx = 0
        if start_coord.y > end_coord.y:
            dy = -1
        else:
            dy = 1
    elif start_coord.y == end_coord.y:
        dy = 0
        if start_coord.x > end_coord.x:
            dx = -1
        else:
            dx = 1
    else:
        if only_right:
            print("   not right")
            return
        else:
            if start_coord.y > end_coord.y:
                dy = -1
            else:
                dy = 1
            if start_coord.x > end_coord.x:
                dx = -1
            else:
                dx = 1

    x = start_coord.x
    y = start_coord.y
    while y != end_coord.y + dy or x != end_coord.x + dx:

        c = Coord(x, y)
        # print(f"   set {x}, {y}")

        if c in the_map:
            the_map[c] = the_map[c] + 1
        else:
            the_map[c] = 1

        x += dx
        y += dy


with open('input.txt') as my_file:
    input_lines = my_file.readlines()
input_lines = [s.strip() for s in input_lines]
line_count = len(input_lines)

floor_map = dict()
floor_map_diag = dict()

for line in input_lines:
    two = line.index(" -> ")
    start = line[:two].strip()
    end = line[two+4:].strip()
    print(f"{start=}, {end=}")
    start_c = coord_from_string(start)
    end_c = coord_from_string(end)

    process_points(floor_map, start_c, end_c, True)
    process_points(floor_map_diag, start_c, end_c, False)

# pprint.pprint(floor_map)

multiple_count = 0
for coord, count in floor_map.items():
    if count > 1:
        multiple_count += 1

print(f"multiple_count = {multiple_count}")



multiple_count_diag = 0
for coord, count in floor_map_diag.items():
    if count > 1:
        multiple_count_diag += 1

print(f"multiple_count_diag = {multiple_count_diag}")
