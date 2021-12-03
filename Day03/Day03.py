
with open('input.txt') as my_file:
    input_lines = my_file.readlines()
input_lines = [s.strip() for s in input_lines]
line_count = len(input_lines)

def find_gas_histogram(kept_lines, gas_lines):
    gas_histogram = [0 for x in range(len(gas_lines[0]))]

    for line_index, line in enumerate(gas_lines):
        if kept_lines[line_index] == 1:
            for char_index, digit in enumerate(line):
                # print(f"{char_index, digit}")
                if digit == '1':
                    gas_histogram[char_index] += 1

    return gas_histogram


def find_gas(gas_lines, keep_mode):
    remaining = len(gas_lines)
    kept_lines = [1 for x in range(len(gas_lines))]

    gas_histogram = find_gas_histogram(kept_lines, gas_lines)
    for digit_index in range(len(gas_histogram)):
        count = gas_histogram[digit_index]
        print(f"{keep_mode} remaining = {remaining}, {gas_histogram}")
        remove_target = None
        if keep_mode == 1:
            if count < remaining / 2:
                # 0 is more common
                remove_target = '1'
            elif count == remaining / 2:
                remove_target = '0'
            else:
                remove_target = '0'
        else:
            if count < remaining / 2:
                # 0 is more common
                remove_target = '0'
            elif count == remaining / 2:
                remove_target = '1'
            else:
                # 1 is more common
                remove_target = '1'

        for line_index, line in enumerate(gas_lines):
            if kept_lines[line_index] == 1:
                if gas_lines[line_index][digit_index] == remove_target:
                    kept_lines[line_index] = 0
                    remaining -= 1
                    print(f"{digit_index}, {remove_target}: removed {gas_lines[line_index]}")
                else:
                    print(f"{digit_index}, {remove_target}: kept    {gas_lines[line_index]}")

            if (remaining == 1):
                break

        if (remaining == 1):
            break

        gas_histogram = find_gas_histogram(kept_lines, gas_lines)

    ret = 0
    for line_index, line in enumerate(gas_lines):
        if kept_lines[line_index] == 1:
            print(f"mode {keep_mode}: gas_lines[{line_index}] = {gas_lines[line_index]} ")
            ret = int(gas_lines[line_index], 2)

    return ret


# part one
histogram = [0 for x in range(len(input_lines[0]))]

for line in input_lines:
    for char_index, digit in enumerate(line):
        # print(f"{char_index, digit}")
        if digit == '1':
            histogram[char_index] += 1

print(f"{line_count=}")
print(histogram)

gamma = 0
epsilon = 0
for digit_index, count in enumerate(histogram):
    if count < line_count / 2:
        print('0', end='')
        epsilon += pow(2, len(histogram) - 1 - digit_index)
    else:
        print('1', end='')
        gamma += pow(2, len(histogram) - 1 - digit_index)

print()
print(f"gamma = {gamma}")
print(f"epsilon = {epsilon}")
print(f"product = {epsilon * gamma}")

# part two
print("Part two")
o2_rating = find_gas(input_lines, 1)
co2_rating = find_gas(input_lines, 0)

print(f"o2_rating = {o2_rating}")
print(f"co2_rating = {co2_rating}")
print(f"product = {o2_rating * co2_rating}")




