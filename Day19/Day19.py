import math
import pprint
import sys


rotations = [
 [0, 1, 2, 1, 1, 1],
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


# read the input file and return a list of dictionary of scanner observations
#  scanner_points[0][3] --> list of observations for station #0, rotated with idx #3
#  scanner_points[0][0] --> list of observations for station #0, at identity rotation #0
#  scanner_points[0]    --> dictionary of observations for station #0, with key == rotation_idx
def get_scanner_points(input_lines):
    flat_scanner_points = []
    sensor_number = None
    for line in input_lines:
        if line.startswith("--- scanner"):
            number_end = line[12:].index(' ')
            sensor_number = int(line[12:12+number_end])
            flat_scanner_points.append([])
        elif len(line) > 1:
            trips = [int(x) for x in line.split(",")]
            flat_scanner_points[sensor_number].append(trips)

    # now that we have the complete list, fluff it up with the rotations
    scanner_points = []
    for observation in flat_scanner_points:
        this_station = dict()

        for rotation_idx in range(len(rotations)):
            this_rotation = []
            for point in observation:
                this_rotation.append(rotate_point(point, rotation_idx))

            this_station[rotation_idx] = this_rotation
        scanner_points.append(this_station)
    return scanner_points


# rotate a particular point by the translation at the given rotation_idx
def rotate_point(point, rotation_idx):
    rot = rotations[rotation_idx]
    ret = [
        point[rot[0]] * rot[3],
        point[rot[1]] * rot[4],
        point[rot[2]] * rot[5]
    ]
    return ret


# find the difference between point1 and point2
def get_delta(point1, point2):
    x = [
        point1[0] - point2[0],
        point1[1] - point2[1],
        point1[2] - point2[2]
    ]
    return x


# add point1 to point2
def add_delta(point1, point2):
    x = [
        point1[0] + point2[0],
        point1[1] + point2[1],
        point1[2] + point2[2]
    ]
    return x

# invert the given point
def get_opposite(point1):
    x = [
        -point1[0],
        -point1[1],
        -point1[2]
    ]
    return x


def place_station(scanner_points, known_stations, station):

    # print(f"rotations = {len(rotations)}, scanner points = {len(scanner_points[station][0])}, match = {len(scanner_points[0][0])}")
    # for each rotation ...
    for rotation_idx in range(len(rotations)):

        for known_station, known_station_info in known_stations.items():
            if rotation_idx == 0:
                print(f"working {known_station} on {station}")

            # print(f"{station} against {known_station_info}")
            known_station_origin = known_station_info[0]
            known_station_rotation = known_station_info[1]

            for known_rotate_point_idx in range(len(scanner_points[known_station][known_station_rotation])):

                # build an offset from station[0] point[0] to each point
                # in the target station, and see if anything else lines up ...
                for candidate_point in scanner_points[station][rotation_idx]:
                    scanner_point = scanner_points[known_station][known_station_rotation][known_rotate_point_idx]
                    scanner_point = add_delta(scanner_point, known_station_origin)
                    candidate_delta = get_delta(scanner_point, candidate_point)

                    matches = 0
                    check_list = []
                    for test_idx, test_point in enumerate(scanner_points[station][rotation_idx]):
                        result = add_delta(test_point, candidate_delta)

                        for rematch_point in scanner_points[known_station][known_station_rotation]:
                            temp = add_delta(rematch_point, known_station_origin)
                            if temp == result:
                                matches += 1
                                check_list.append((rematch_point, test_point))
                    if matches >= 12:
                        print(f"station = {station}, rotation_idx = {rotation_idx}, candidate = {candidate_point}, matches = {matches}")
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

                for point in scanner_points[match_station][match_rotation]:
                    result = add_delta(point, match_delta)
                    print(result)

                matched_one = True
                break

        if not matched_one:
            print("Failed to match")
            break
        break



if __name__ == '__main__':
    main()

