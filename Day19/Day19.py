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


def get_opposite(point1):
    x = [
        -point1[0],
        -point1[1],
        -point1[2]
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
                    scanner_point = rotate_point(scanner_points[known_station][known_rotate_point_idx], rotations[known_station_rotation])
                    scanner_point = add_delta(scanner_point, known_station_origin)
                    candidate_delta = get_delta(scanner_point, rotated_target)

                    matches = 0
                    check_list = []
                    for test_idx, test_point in enumerate(scanner_points[station]):
                        rotated_test = rotate_point(test_point, rotations[rotation_idx])
                        result = add_delta(rotated_test, candidate_delta)

                        for rematch_idx, rematch_point in enumerate(scanner_points[known_station]):
                            temp = rotate_point(rematch_point, rotations[known_station_rotation])
                            temp = add_delta(temp, known_station_origin)
                            if temp == result:
                                matches += 1
                                check_list.append((rematch_point, test_point))
                    if matches >= 12:
                        print(f"station = {station}, rotation_idx = {rotation_idx}, candidate_idx = {candidate_idx}, matches = {matches}")
                        # pprint.pprint(check_list)
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
    print(f"points per scanner: {[len(row) for row in scanner_points]}")

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
                unknown_set.remove(match_station)
                origins[match_station] = (match_delta, match_rotation)
                print(f"match_station {match_station} = ({match_delta}, {match_rotation}")
                # del origins[0]
                # unknown_set.add(0)

                for point in scanner_points[match_station]:
                    rotated_test = rotate_point(point, rotations[match_rotation])
                    result = add_delta(rotated_test, match_delta)
                    print(result)

                matched_one = True
                break

        if not matched_one:
            print("Failed to match")
            break
        break



if __name__ == '__main__':
    main()

