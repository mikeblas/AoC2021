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


# returns sorted coordinate diffs as list[coord][station_id]
def find_diffs(scanner_points):

    all_diffs = []

    for axis in range(0,3):
        x_diffs = []
        for index in range(0, len(scanner_points)):
            temp_n_x = [point[axis] for point in scanner_points[index]]
            temp_n_x.sort()
            this_row = []
            for point_index in range(1, len(temp_n_x)):
                dx = abs(temp_n_x[point_index-1] - temp_n_x[point_index])
                this_row.append(dx)
            x_diffs.append(this_row)

        all_diffs.append(x_diffs)

    return all_diffs


def compare_out(all_diffs, axis1, axis2):
    # compare all diff lists on this axis to see who has many in common
    for outer_index in range(0, len(all_diffs[axis1])-1):
        outer_set = set(all_diffs[axis1][outer_index])
        for inner_index in range(outer_index+1, len(all_diffs[axis2])):
            r = outer_set.intersection(all_diffs[axis2][inner_index])
            if len(r) >= 12:
                print(f"{axis1}, {outer_index} -> {axis2}, {inner_index}: {len(r):4} {r}")

    # all_diffs[axis1][2].sort()
    # all_diffs[axis2][20].sort()
    # print(f"station  2, axis {axis1}: {all_diffs[axis1][2]}")
    # print(f"station 20, axis {axis2}: {all_diffs[axis2][20]}")


def main():
    with open('input.txt') as my_file:
        input_lines = my_file.readlines()
    input_lines = [s.strip() for s in input_lines]
    line_count = len(input_lines)
    print(f"{line_count} lines read")

    # read scanner all points
    scanner_points = get_scanner_points(input_lines)
    print(f"{len(scanner_points)} scanners read")
    # pprint.pprint(scanner_points[0])

    all_diffs = find_diffs(scanner_points)
    for axis in range(0, 3):
        print(f"{len(all_diffs[axis])} diffs computed on axis {axis}")

    pprint.pprint(all_diffs, compact=True, width=132)

    for axis1 in range(0, 3):
        for axis2 in range(0, 3):
            compare_out(all_diffs, axis1, axis2)
    # print(x_diffs)


if __name__ == '__main__':
    main()

