import pprint
import sys


def get_scanner_points(input_lines):
    scanner_points = []
    sensor_number = None
    for line in input_lines:
        if line.startswith("--- scanner"):
            number_end = line[12:].index(' ')
            sensor_number = int(line[12:12+number_end])
            scanner_points.append([])
        elif len(line) > 1:
            trips = [int(x) for x in line.split(",")]
            scanner_points[sensor_number].append(trips)
    return scanner_points


def find_diffs(scanner_points, coord):
    x_diffs = []
    for index in range(0, len(scanner_points)):
        temp_n_x = [point[coord] for point in scanner_points[index]]
        temp_n_x.sort()
        this_row = []
        for point_index in range(1, len(temp_n_x)):
            dx = abs(temp_n_x[point_index-1] - temp_n_x[point_index])
            this_row.append(abs(dx))
        x_diffs.append(this_row)

    # compare all diff lists on this axis to see who has many in
    for x in range(0, len(x_diffs)-1):
        x_set = set(x_diffs[x])
        for y in range(x+1, len(x_diffs)):
            r = x_set.intersection(x_diffs[y])
            if len(r) >= 12:
                print(f"{x} -> {y}: {len(r):4} {r}")

    x_diffs[2].sort()
    x_diffs[20].sort()
    print(f"reference  2, {coord}: {x_diffs[2]}")
    print(f"reference 20, {coord}: {x_diffs[20]}")


def main():
    with open('input.txt') as my_file:
        input_lines = my_file.readlines()
    input_lines = [s.strip() for s in input_lines]
    line_count = len(input_lines)
    print(f"{line_count} lines read")

    scanner_points = get_scanner_points(input_lines)
    pprint.pprint(scanner_points[0])

    print("0")
    find_diffs(scanner_points, 0)

    print("\n1")
    find_diffs(scanner_points, 1)


    print("\n2")
    find_diffs(scanner_points, 2)


    # print(x_diffs)


if __name__ == '__main__':
    main()