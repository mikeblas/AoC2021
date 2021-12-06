
import pprint

with open('input.txt') as my_file:
    input_lines = my_file.readlines()
input_lines = [s.strip() for s in input_lines]
line_count = len(input_lines)

fish_list = input_lines[0].split(",")
fish_list = [int(x) for x in fish_list]

# convert to a histogram
fish_dict = dict()
for fish in fish_list:
    if fish in fish_dict:
        fish_dict[fish] += 1
    else:
        fish_dict[fish] = 1

pprint.pprint(fish_dict)

days = 256

day = 0
while day <= days:
    print(f"day {day}: ", end='')
    pprint.pprint(fish_dict)

    total = 0
    for age, age_count in fish_dict.items():
        total += age_count
    print(f"there are {total}")

    new_dict = dict()
    new_dict[8] = fish_dict[0] if 0 in fish_dict else 0
    new_dict[6] = fish_dict[0] if 0 in fish_dict else 0
    new_dict[0] = fish_dict[1] if 1 in fish_dict else 0
    new_dict[1] = fish_dict[2] if 2 in fish_dict else 0
    new_dict[2] = fish_dict[3] if 3 in fish_dict else 0
    new_dict[3] = fish_dict[4] if 4 in fish_dict else 0
    new_dict[4] = fish_dict[5] if 5 in fish_dict else 0
    new_dict[5] = fish_dict[6] if 6 in fish_dict else 0
    new_dict[6] = new_dict[6] + (fish_dict[7] if 7 in fish_dict else 0)
    new_dict[7] = fish_dict[8] if 8 in fish_dict else 0

    fish_dict.clear()
    fish_dict = {k:v for k, v in new_dict.items()}

    day += 1
