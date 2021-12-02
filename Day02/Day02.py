

with open('input.txt') as my_file:
    input_lines = my_file.readlines()


# -- part 1

depth = 0
horizontal = 0

for line in input_lines:
    param_index = line.index(" ")
    param = int(line[param_index:])
    if (line.startswith("forward")):
        horizontal += param
    elif (line.startswith("down")):
        depth += param
    elif (line.startswith("up")):
        depth -= param

print(f"Ended at depth = {depth}, horizontal = {horizontal}")
print(f"product is {depth * horizontal}")

# -- part 2

depth = 0
horizontal = 0
aim = 0

for line in input_lines:
    param_index = line.index(" ")
    param = int(line[param_index:])
    if (line.startswith("forward")):
        horizontal += param
        depth += (aim * param)
    elif (line.startswith("down")):
        aim += param
    elif (line.startswith("up")):
        aim -= param

print(f"Ended at depth = {depth}, horizontal = {horizontal}")
print(f"product is {depth * horizontal}")


