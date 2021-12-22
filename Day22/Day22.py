import pprint


def coord_included(x, y, z, coord):
    if x > coord[0][1] or x < coord[0][0]:
        return False
    if y > coord[1][1] or y < coord[1][0]:
        return False
    if z > coord[2][1] or z < coord[2][0]:
        return False
    return True


def get_volume(coord):
    x_len = coord[0][1] - coord[0][0] + 1
    y_len = coord[1][1] - coord[1][0] + 1
    z_len = coord[2][1] - coord[2][0] + 1
    return x_len * y_len * z_len


def get_range(string):
    pairs = string[2:].split("..")
    return int(pairs[0]), int(pairs[1])


def get_overlap(coords1, coords2):
    x_min = max(coords1[0][0], coords2[0][0])
    x_max = min(coords1[0][1], coords2[0][1])
    if x_max < x_min:
        return None
    y_min = max(coords1[1][0], coords2[1][0])
    y_max = min(coords1[1][1], coords2[1][1])
    if y_max < y_min:
        return None
    z_min = max(coords1[2][0], coords2[2][0])
    z_max = min(coords1[2][1], coords2[2][1])
    if z_max < z_min:
        return None
    return (x_min, x_max), (y_min, y_max), (z_min, z_max)


def do_part_1(instructions):
    block = [[[0 for x in range(-50,51)] for y in range(-50,51)] for z in range(-50,51)]

    for z in range(-50,51):
        print(z)
        for y in range(-50,51):
            for x in range(-50,51):
                for step in instructions:
                    if coord_included(x, y, z, step[1]):
                        block[z][y][x] = step[0]

    total_on = 0
    for z in range(-50,51):
        # print(z)
        for y in range(-50,51):
            for x in range(-50,51):
                if block[z][y][x] == 1:
                    total_on += 1
                    # print(f"{x}, {y}, {z}")

    print(f"{total_on} cubes on")


def main():
    with open('input.txt') as my_file:
        input_lines = my_file.readlines()
    input_lines = [s.strip() for s in input_lines]
    line_count = len(input_lines)

    instructions = []

    for line in input_lines:
        if line.startswith("on "):
            setting = 1
            remaining = line[3:]
        else:
            setting = 0
            remaining = line[4:]

        splits = remaining.split(",")
        x_range = get_range(splits[0])
        y_range = get_range(splits[1])
        z_range = get_range(splits[2])

        instructions.append([setting, (x_range, y_range, z_range)])


    print(f"read {len(instructions)} instructions")
    # pprint.pprint(instructions)

    # do_part_1(instructions)

    # part 2

    cubes = []

    for step_idx, step in enumerate(instructions):
        if step[0] == 1:
            overlaps = [[-1 * c[0], get_overlap(c[1], step[1])] for c in cubes if get_overlap(c[1], step[1]) is not None]
            # print(overlaps)
            cubes.append([1, step[1]])
            cubes.extend(overlaps)
        else:
            overlaps = [[-1 * c[0], get_overlap(c[1], step[1])] for c in cubes if get_overlap(c[1], step[1]) is not None]
            # print(overlaps)
            cubes.extend(overlaps)
        print(f"step {step_idx+1} has {len(cubes)} cubes from {len(overlaps)}")
        # if step_idx+1 in [9, 10]:
        if step_idx + 1 <= 10:
            pprint.pprint(overlaps)

    total_volume = 0
    for c in cubes:
        total_volume += c[0] * get_volume(c[1])
    print(f"total volume is {total_volume}")




if __name__ == '__main__':
    main()


# 533801419067254
# 2758514936282235