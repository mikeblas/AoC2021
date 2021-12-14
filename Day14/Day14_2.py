
from collections import defaultdict

with open('input.txt') as my_file:
    input_lines = my_file.readlines()
input_lines = [s.strip() for s in input_lines]
line_count = len(input_lines)
print(f"{line_count} lines read")

# build a dictionary of the rules
rules_dict = {}
for rule in input_lines[2:]:
    rule_split = rule.split(" -> ")
    # print(f"{rule}, {rule_split}")
    rules_dict[rule_split[0]] = rule_split[1]

# build the polymer into a dictionary
polymer = input_lines[0]
polymer_dict = defaultdict(int)
for idx in range(len(polymer) - 1):
    two = polymer[idx:idx + 2]
    polymer_dict[two] += 1

# do the steps!
for step in range(40):
    new_polymer_dict = polymer_dict.copy()

    for two,two_count in polymer_dict.items():
        if two_count > 0:
            if two in rules_dict:
                new_left = two[0] + rules_dict[two]
                new_right = rules_dict[two] + two[1]

                new_polymer_dict[two] -= two_count
                new_polymer_dict[new_left] += two_count
                new_polymer_dict[new_right] += two_count
            else:
                print(f"not in rules: {two}")

    # print(new_polymer_dict)
    print(f"{step+1}: dict is {len(new_polymer_dict)}, total is {sum(new_polymer_dict.values())}")
    polymer_dict = new_polymer_dict.copy()

histogram = defaultdict(int)
last = None
last_count = None
for two,two_count in polymer_dict.items():
    histogram[two[0]] += two_count
    last = two
    last_count = two_count
histogram[polymer[-1]] += 1

min_element, min_count = None, None
max_element, max_count = None, None
for k,v in histogram.items():
    if min_count is None or min_count > v:
        min_element = k
        min_count = v
    if max_count is None or max_count < v:
        max_element = k
        max_count = v

print(f"min element is {min_element}, {min_count}")
print(f"max element is {max_element}, {max_count}")
print(f"difference is {max_count - min_count}")
