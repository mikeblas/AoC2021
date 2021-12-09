

import pprint

def two_fuel(pos, target):
    dist = abs(pos - target)
    return (dist*(dist+1))/2

with open('input.txt') as my_file:
    input_lines = my_file.readlines()
input_lines = [s.strip() for s in input_lines]
line_count = len(input_lines)

print(line_count)
# pprint.pprint(input_lines)

my_count = 0
for line in input_lines:
    in_out = line.split("|")

    # print(in_out[1])
    for digit in in_out[1].strip().split(" "):
        this_len = len(digit.strip())
        if this_len == 2 or this_len == 4 or this_len == 3 or this_len == 7:
            # print(digit)
            my_count += 1

print(my_count)



