import math
import pprint
import sys

all3_factors = [
    [-1, -1, -1],
    [-1, -1,  1],
    [-1,  1, -1],
    [-1,  1,  1],
    [ 1, -1, -1],
    [ 1, -1,  1],
    [ 1,  1, -1],
    [ 1,  1,  1]
]

all2_factors = [
    [-1, -1],
    [-1,  1],
    [ 1, -1],
    [ 1,  1],
]

three_rotations = [
    [0, 1, 2],
    [0, 2, 1],
    [1, 0, 2],
    [1, 2, 0],
    [2, 1, 0],
    [2, 0, 1]
]

identity_factors = [[1, 1]]

rotations =[
 [0, 2, 1, 1, 1, -1],
 [2, 0, 1, -1, 1, -1],
 [0, 2, 1, 1, -1, -1],
 [2, 0, 1, 1, 1, -1],
 [2, 1, 0, 1, -1, 1],
 [1, 2, 0, 1, 1, 1],
 [2, 1, 0, -1, 1, 1],
 [1, 2, 0, -1, -1, 1],
 [1, 0, 2, -1, 1, 1],
 [0, 1, 2, 1, -1, 1],
 [1, 0, 2, 1, 1, 1],
 [0, 1, 2, 1, 1, 1],
 [2, 0, 1, -1, 1, 1],
 [0, 2, 1, 1, -1, 1],
 [2, 0, 1, 1, 1, 1],
 [0, 2, 1, 1, 1, 1],
 [0, 1, 2, 1, 1, -1],
 [1, 0, 2, -1, 1, -1],
 [0, 1, 2, 1, -1, -1],
 [1, 0, 2, 1, 1, -1],
 [1, 2, 0, 1, -1, 1],
 [2, 1, 0, 1, 1, 1],
 [1, 2, 0, -1, 1, 1],
 [2, 1, 0, -1, -1, 1]
]

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



def distance3(first, second):
    dx = first[0] - second[0]
    dy = first[1] - second[1]
    dz = first[2] - second[2]
    return math.sqrt(dx*dx* + dy*dy + dz*dz)


# returns diffs of sorted coordinates as list[axis][station_id]
def find_diffs(scanner_points):

    all_diffs = []

    for axis in range(0,3):
        diffs = []
        for index in range(0, len(scanner_points)):
            temp_n_x = [point[axis] for point in scanner_points[index]]
            temp_n_x.sort()
            this_row = []
            for point_index in range(1, len(temp_n_x)):
                dx = temp_n_x[point_index-1] - temp_n_x[point_index]
                this_row.append(dx)
            diffs.append(this_row)

        all_diffs.append(diffs)

    return all_diffs



def find_diffs3(scanner_points):

    all_diffs = []

    for index in range(0, len(scanner_points)):
        this_row = []
        for p1_index in range(0, len(scanner_points[index])-1):
            for p2_index in range(p1_index+1, len(scanner_points[index])):
                dist = distance3(scanner_points[index][p1_index], scanner_points[index][p2_index])
                this_row.append(dist)
        all_diffs.append(this_row)

    return all_diffs


def compare_out(all_diffs, axis1, axis2, factors):
    # compare all diff lists on this axis to see who has many in common
    for outer_index in range(0, len(all_diffs[axis1])-1):
        outer_set = set([n * factors[0] for n in all_diffs[axis1][outer_index]])
        for inner_index in range(outer_index+1, len(all_diffs[axis2])):
            r = outer_set.intersection([n * factors[1] for n in all_diffs[axis2][inner_index]])
            if len(r) >= 12:
                print(f"{axis1}, {outer_index}, {factors[0]} -> {axis2}, {inner_index}, {factors[1]}: {len(r):4} {r}")

    # all_diffs[axis1][2].sort()
    # all_diffs[axis2][20].sort()
    # print(f"station  2, axis {axis1}: {all_diffs[axis1][2]}")
    # print(f"station 20, axis {axis2}: {all_diffs[axis2][20]}")


def compare_out3(all_diffs3):
    for outer_index in range(0, len(all_diffs3)-1):
        outer_set = set([n for n in all_diffs3[outer_index]])
        for inner_index in range(outer_index+1, len(all_diffs3)):
            r = outer_set.intersection([n for n in all_diffs3[inner_index]])
            if len(r) >= 12:
                print(f"{outer_index} -3> {inner_index}: {len(r):4} {r}")


def method_2d(scanner_points):
    all_diffs = find_diffs(scanner_points)
    for axis in range(0, 3):
        print(f"{len(all_diffs[axis])} diffs computed on axis {axis}")

    pprint.pprint(all_diffs, compact=True, width=160)

    for axis1 in range(0, 3):
        for axis2 in range(0, 3):
            for factor in identity_factors:
                compare_out(all_diffs, axis1, axis2, factor)
    # print(x_diffs)



def method_3d(scanner_points):
    all_diffs3 = find_diffs3(scanner_points)
    pprint.pprint(all_diffs3, compact=True, width=160)
    compare_out3(all_diffs3)


def rotate_point(point, rotation):
    ret = [
        point[rotation[0]] * rotation[3],
        point[rotation[1]] * rotation[4],
        point[rotation[2]] * rotation[5]
    ]
    return ret


def get_delta(point1, point2):
    x = [
        point1[0] - point2[0],
        point1[1] - point2[1],
        point1[2] - point2[2]
    ]
    return x


def add_delta(point1, point2):
    x = [
        point1[0] + point2[0],
        point1[1] + point2[1],
        point1[2] + point2[2]
    ]
    return x


def place_station(scanner_points, known_stations, station):

    # print(f"rotations = {len(rotations)}, scanner points = {len(scanner_points[station])}, match = {len(scanner_points[0])}")
    # for each rotation ...
    for rotation_idx in range(len(rotations)):

        for known_station, known_station_info in known_stations.items():
            if rotation_idx == 0:
                print(f"working {known_station} on {station}")

            for known_rotate_point_idx in range(len(scanner_points[known_station])):

                # print(f"{station} against {known_station_info}")
                known_station_origin = known_station_info[0]
                known_station_rotation = known_station_info[1]

                # build an offset from station[0] point[0] to each point
                # in the target station, and see if anything else lines up ...
                for candidate_idx, candidate_point in enumerate(scanner_points[station]):
                    rotated_target = rotate_point(candidate_point, rotations[rotation_idx])
                    candidate_delta = get_delta(scanner_points[known_station][known_rotate_point_idx], rotated_target)

                    matches = 0
                    for test_idx, test_point in enumerate(scanner_points[station]):
                        rotated_test = rotate_point(test_point, rotations[rotation_idx])
                        result = add_delta(rotated_test, candidate_delta)

                        for rematch_idx, rematch_point in enumerate(scanner_points[known_station]):
                            temp = rotate_point(rematch_point, rotations[known_station_rotation])
                            # temp = add_delta(temp, known_station_origin)
                            if temp == result:
                                matches += 1
                    if matches >= 12:
                        print(f"station = {station}, rotation_idx = {rotation_idx}, candidate_idx = {candidate_idx}, matches = {matches}")
                        return station, rotation_idx, candidate_delta

    return None

def main():

    with open('input.txt') as my_file:
        input_lines = my_file.readlines()
    input_lines = [s.strip() for s in input_lines]
    line_count = len(input_lines)
    print(f"{line_count} lines read")

    # read scanner all points
    scanner_points = get_scanner_points(input_lines)
    print(f"{len(scanner_points)} scanners read")
    print(f"{[len(row) for row in scanner_points]}")

    # method_2d(scanner_points)
    # method_3d(scanner_points)

    # origins of known scanners; we normalize to station #0
    origins = { 0: ([0, 0, 0], 11) }

    # which stations are not known just yet?
    unknown_set = set([n for n in range(1, len(scanner_points))])

    while len(unknown_set) > 0:
        matched_one = False
        for station in unknown_set:
            match_info = place_station(scanner_points, origins, station)
            if match_info is not None:
                (match_station, match_rotation, match_delta) = match_info
                print(match_info)
                # unknown_set.remove(match_station)
                origins[match_station] = (match_delta, match_rotation)
                del origins[0]
                unknown_set.add(0)

                for point in scanner_points[match_station]:
                    rotated_test = rotate_point(point, rotations[match_rotation])
                    result = add_delta(rotated_test, match_delta)
                    print(result)

                matched_one = True
                break

        if not matched_one:
            print("Failed to match")
            break



if __name__ == '__main__':
    main()

