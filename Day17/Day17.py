import sys


def run_test(velocity, x_range, y_range):
    pos = (0, 0)
    print(f"at {pos}, velocity is {velocity}")
    while pos[0] < x_range[1] and pos[1] > y_range[1]:
        print(f"at {pos}, velocity is {velocity}")

        pos = (pos[0] + velocity[0], pos[1] + velocity[1])
        velocity = (velocity[0] - 1 if velocity[0] > 0 else velocity[0] + 1, velocity[1] - 1)

        if x_range[0] <= pos[0] <= x_range[1] and y_range[0] <= pos[1] <= y_range[1]:
            print("Win!")
            return True

    print(f"at {pos}, velocity is {velocity}")
    return False


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

    velocity = (17, -4)

    print(run_test((17, -4), x_range, y_range))
    print(run_test((9, 0), x_range, y_range))
    print(run_test((6, 3), x_range, y_range))
    print(run_test((7, 2), x_range, y_range))
    print(run_test((6, 9), x_range, y_range))


if __name__ == '__main__':
    main()

