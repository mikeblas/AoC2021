
import pprint

def two_fuel(pos, target):
    dist = abs(pos - target)
    return (dist*(dist+1))/2

with open('input.txt') as my_file:
    input_lines = my_file.readlines()
input_lines = [s.strip() for s in input_lines]
line_count = len(input_lines)

print(f"{line_count} lines read")
# pprint.pprint(input_lines)

places = [[int(x) for x in digit] for digit in input_lines]
pprint.pprint(places)

step_count = 1
total_flashes = 0


def test_flash(y, x):

    global total_flashes
    if flashed[y][x]:
        return

    if places[y][x] >= 10:
        places[y][x] = 0
        flashed[y][x] = True
        total_flashes += 1

        for dy in [-1,0,1]:
            for dx in [-1,0,1]:
                if x+dx < 0 or x+dx >= len(flashed[0]):
                    continue
                if y+dy < 0 or y+dy >= len(flashed):
                    continue
                if not flashed[y+dy][x+dx]:
                    places[y+dy][x+dx] += 1
                    test_flash(y+dy, x+dx)

while step_count <= 2000:
    # add one to everyone
    for y in range(0, len(places)):
        for x in range(0, len(places[y])):
            places[y][x] += 1

    flashed = [[False for x in range(len(places))] for y in range(len(places[0]))]
    # pprint.pprint(flashed)

    # see who flashes
    before = total_flashes
    for y in range(0, len(places)):
        for x in range(0, len(places[y])):
            test_flash(y, x)
    after = total_flashes

    print(f"step {step_count}: {total_flashes} total flashes, {after - before} flashes this time")
    if after - before == len(places) * len(places[y]):
        print("Found it!")
        break
    # pprint.pprint(places)
    # pprint.pprint(flashed)
    # print()

    step_count += 1