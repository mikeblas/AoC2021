
import pprint

with open('input.txt') as my_file:
    input_lines = my_file.readlines()
input_lines = [s.strip() for s in input_lines]
line_count = len(input_lines)

fish_list = input_lines[0].split(",")
fish_list = [int(x) for x in fish_list]

# pprint.pprint(fish_list)

days = 256

day = 0
while day <= days:
    print(f"day {day}: ", end='')
    # pprint.pprint(fish_list)
    print(f"there are {len(fish_list)}")

    new_fish = []
    for idx, fish in enumerate(fish_list):

        if fish == 0:
            fish_list[idx] = 6
            new_fish.append(8)
        else:
            fish_list[idx] -= 1

    fish_list.extend(new_fish)

    day += 1
