
import pprint

with open('input.txt') as my_file:
    input_lines = my_file.readlines()
input_lines = [s.strip() for s in input_lines]
line_count = len(input_lines)

crab_positions = [int(x) for x in input_lines[0].split(",")]

# pprint.pprint(crab_positions)

crab_positions.sort()

# pprint.pprint(crab_positions)
# 345 wrong
print(crab_positions[int(len(crab_positions)/2)-1])
print(len(crab_positions))
median = crab_positions[int(len(crab_positions)/2)-1]
print(f"{median=}")

total_fuel = 0
for position in crab_positions:
    total_fuel += abs(median - position)

print(total_fuel)

