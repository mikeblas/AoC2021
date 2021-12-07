
import pprint

def two_fuel(pos, target):
    dist = abs(pos - target)
    return (dist*(dist+1))/2

with open('input.txt') as my_file:
    input_lines = my_file.readlines()
input_lines = [s.strip() for s in input_lines]
line_count = len(input_lines)

crab_positions = [int(x) for x in input_lines[0].split(",")]

# pprint.pprint(crab_positions)

crab_positions.sort()

# pprint.pprint(crab_positions)
print(f"length is {len(crab_positions)}")
median = crab_positions[int(len(crab_positions)/2)]
print(f"{median=}")

total_fuel = 0
for position in crab_positions:
    total_fuel += abs(median - position)

print(f"total fuel is {total_fuel}")

# part two is brute force over a
# we know it must be in the range between the min and max positions occupied

print("\nPart Two:")

min_position = min(crab_positions)
max_position = max(crab_positions)

print(f"min = {min_position}")
print(f"max = {max_position}")

min_fuel = None
min_fuel_target = None

for target in range(min_position, max_position+1):

    total_fuel = sum([two_fuel(position, target) for position in crab_positions])

    # print(f"{target} gets {total_fuel}")

    if min_fuel is None or min_fuel > total_fuel:
        min_fuel = total_fuel
        min_fuel_target = position

print(f"min_fuel = {min_fuel}")
print(f"min_fuel_target = {min_fuel_target}")
