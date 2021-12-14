
with open('sample.txt') as my_file:
    input_lines = my_file.readlines()
input_lines = [s.strip() for s in input_lines]
line_count = len(input_lines)
print(f"{line_count} lines read")

polymer = input_lines[0]
rules_dict = {}

for rule in input_lines[2:]:
    rule_split = rule.split(" -> ")
    # print(f"{rule}, {rule_split}")
    rules_dict[rule_split[0]] = rule_split[1]


for step in range(10):
    new_polymer = ""
    for idx in range(len(polymer)-1):
        two = polymer[idx:idx+2]
        # print(f"{two}")
        if two in rules_dict:
            new_polymer += two[0] + rules_dict[two]
        else:
            new_polymer += two
        # print(new_polymer)

    new_polymer += polymer[-1]

    print(f"{step+1}: length is {len(new_polymer)}")
    polymer = new_polymer

histogram = {}
for molecule in polymer:
    if molecule not in histogram:
        histogram[molecule] = 1
    else:
        histogram[molecule] += 1

print(histogram)

min_element, min_count = None, None
max_element, max_count = None, None
for k,v in histogram.items():
    if min_count is None or min_count > v:
        min_element = k
        min_count = v
    if max_count is None or max_count < v:
        max_element = k
        max_count = v

print(f"{min_element}, {min_count}")
print(f"{max_element}, {max_count}")
print(f"difference is {max_count - min_count}")