
import pprint

with open('input.txt') as my_file:
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
        low_point_list.append((x, y))

# 1718 incorrect
print(f"{low_points} low points")
print(f"{low_costs} low costs")

pprint.pprint(low_point_list)

# ---- part

pond_sizes = []
while len(low_point_list) > 0:

    (start_x, start_y) = low_point_list.pop()
    visit_queue = []
    visit_queue.append((start_x, start_y))
    print(f"starting {start_x},{start_y}")
    visited = [[False for j in range(map_width)] for i in range(map_height)]
    # pprint.pprint(visited)
    pond_size = 0

    while len(visit_queue) > 0:
        (current_x, current_y) = visit_queue.pop()

        # print(f"working {current_x}, {current_y}, len = {len(visit_queue)}")
        if visited[current_y][current_x]:
            continue
        if the_map[current_y][current_x] == 9:
            continue

        visited[current_y][current_x] = True
        pond_size += 1
        if current_y-1 >= 0:
            visit_queue.append((current_x, current_y-1))
        if current_y+1 < map_height:
            visit_queue.append((current_x, current_y+1))
        if current_x-1 >= 0:
            visit_queue.append((current_x-1, current_y))
        if current_x+1 < map_width:
            visit_queue.append((current_x+1, current_y))

    print(f"pond size is {pond_size}")
    pond_sizes.append(pond_size)

pond_sizes.sort(reverse=True)
total_product = 1
for top in range(0, 3):
    print(f"size {top} is {pond_sizes[top]}")
    total_product *= pond_sizes[top]

print(f"total product is {total_product}")

