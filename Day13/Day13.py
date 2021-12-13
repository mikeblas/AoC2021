
with open('input.txt') as my_file:
    input_lines = my_file.readlines()
input_lines = [s.strip() for s in input_lines]
line_count = len(input_lines)

print(f"read {line_count} lines total")

dot_map = {}

after_line = None
for line_number, line in enumerate(input_lines):
    if len(line) == 0:
        after_line = line_number
        break

    coords = line.split(",")
    dot_map[(int(coords[0]), int(coords[1]))] = 1

print(dot_map)
print(f"map has {len(dot_map)}")

instructions = input_lines[after_line+1:]

for step in instructions:
    axis = step[11]
    value = int(step[13:])

    new_map = {}

    for k in dot_map.keys():
        if axis == 'y':
            if k[1] > value:
                new_map[(k[0], 2*value - k[1])] = 1
            else:
                new_map[k] = 1
        elif axis == 'x':
            if k[0] > value:
                new_map[(2*value - k[0], k[1])] = 1
            else:
                new_map[k] = 1
        else:
            assert False

    print(f"map has {len(new_map)}")
    dot_map.clear()
    dot_map = new_map.copy()
    print(f"map has {len(dot_map)}")
    print(dot_map)


min_x, min_y = None, None
max_x, max_y = None, None

for k in dot_map.keys():
    if min_x is None or min_x > k[0]:
        min_x = k[0]
    if max_x is None or max_x < k[0]:
        max_x = k[0]

    if min_y is None or min_y > k[1]:
        min_y = k[1]
    if max_y is None or max_y < k[1]:
        max_y = k[1]

print(f"{min_x},{min_y} to {max_x},{max_y}")

render = [[0 for y in range(max_y+1)] for x in range(max_x+1)]

# print(render)

for k in dot_map.keys():
    render[k[0]][k[1]] = 1

for y in range(max_y+1):
    for x in range(max_x+1):
        if render[x][y] == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

