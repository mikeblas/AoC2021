
import pprint

with open('sample.txt') as my_file:
    input_lines = my_file.readlines()
input_lines = [s.strip() for s in input_lines]
line_count = len(input_lines)

the_map = []
for line in input_lines:
    the_map.append([int(ch) for ch in line])
map_width = len(the_map[0])
map_height = len(the_map)
print(f"{map_width} by {map_height}")
# pprint.pprint(the_map)


# ---- part 1
low_points = 0
low_costs = 0
low_point_list = []
for y in range(0, map_height):
    for x in range(0, map_width):

        this_one = the_map[y][x]

        if y-1 >= 0 and the_map[y-1][x] <= this_one:
            continue
        if y+1 < map_height and the_map[y+1][x] <= this_one:
            continue
        if x-1 >= 0 and the_map[y][x-1] <= this_one:
            continue
        if x+1 < map_width and the_map[y][x+1] <= this_one:
            continue

        low_points += 1
        low_costs += 1 + this_one
        print(f"at {x},{y} found {this_one}")
        low_point_list.append((x,y))

# 1718 incorrect
print(f"{low_points} low points")
print(f"{low_costs} low costs")

pprint.pprint(low_point_list)

# ---- part 2