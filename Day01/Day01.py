
with open('input1.txt') as f:
    lines = [ int(i) for i in f ]

print(f"Length is {len(lines)}")

# part 1
higher = 0
for i in range(len(lines)):
    if i+1 < len(lines):
        if lines[i+1] > lines[i]:
            higher += 1

print(f"{higher}")


# part 2

higher = 0
for i in range(len(lines)):
    if i+3 < len(lines):
        sum1 = lines[i] + lines[i+1] + lines[i+2]
        sum2 = lines[i+1] + lines[i+2] + lines[i+3]
        if int(sum1 < sum2):
            higher += 1

print(f"{higher}")


