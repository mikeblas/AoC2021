import sys


def run_test(velocity, x_range, y_range):
    pos = (0, 0)
    max_y = 0
    # print(f"at {pos}, velocity is {velocity}")
    while pos[0] < x_range[1] and pos[1] > y_range[0]:
        pos = (pos[0] + velocity[0], pos[1] + velocity[1])

        if velocity[0] > 0:
            new_vx = velocity[0] - 1
        elif velocity[0] < 0:
            new_vx = velocity[0] + 1
        else:
            new_vx = velocity[0]

        velocity = (new_vx, velocity[1] - 1)

        # print(f"at {pos}, velocity is {velocity}")
        if max_y < pos[1]:
            max_y = pos[1]

        if x_range[0] <= pos[0] <= x_range[1] and y_range[0] <= pos[1] <= y_range[1]:
            # print("Win!")
            return max_y

    # print(f"at {pos}, velocity is {velocity}")
    return -sys.maxsize


def do_tests(x_range, y_range):
    print(run_test((17, -4), x_range, y_range))
    print(run_test((9, 0), x_range, y_range))
    print(run_test((6, 3), x_range, y_range))
    print(run_test((7, 2), x_range, y_range))
    print(run_test((6, 9), x_range, y_range))
    print(run_test((5, 9), x_range, y_range))


def do_part1(x_range, y_range):

    vy = -min(y_range[1], y_range[0])
    best_of_all = -sys.maxsize

    while vy > 0:
        best = -sys.maxsize

        vx = 1
        while True:
            result = run_test((vx, vy), x_range, y_range)
            if best < result:
                best = result
                # print(f"{vx},{vy}: {best}")
            vx += 1
            if result != -sys.maxsize:
                break
            if vx > 1000:
                break

        if best_of_all < best:
            best_of_all = best

        vy -= 1

    print(f"{best_of_all} is highest y")


def do_part2(x_range, y_range):

    hits = 0

    for vy in range(min(y_range[0], y_range[1]), -min(y_range[1], y_range[0])):
        for vx in range(1, max(x_range[0], x_range[1])):
            result = run_test((vx, vy), x_range, y_range)
            if result >= 0:
                # print(f"{vx, vy}")
                hits += 1
    print(f"{hits} found")


def main():
    with open('sample.txt') as my_file:
        input_lines = my_file.readlines()
    input_lines = [s.strip() for s in input_lines]
    line_count = len(input_lines)
    print(f"{line_count} lines read")

    # substring after the colon
    t = input_lines[0][input_lines[0].index(':')+2:]

    # x and y sides, split by range
    t = [x.strip()[2:].split("..") for x in t.split(",")]
    t = [list(map(int, i)) for i in t]

    x_range = (t[0][0], t[0][1])
    y_range = (t[1][0], t[1][1])

    print(f"{x_range}, {y_range}")

    # do_tests(x_range, y_range)

    do_part1(x_range, y_range)
    do_part2(x_range, y_range)


if __name__ == '__main__':
    main()

