
import pprint

with open('input.txt') as my_file:
    input_lines = my_file.readlines()
input_lines = [s.strip() for s in input_lines]
line_count = len(input_lines)

print(f"{line_count} lines read")

score = 0
incomplete_scores = []

for line in input_lines:
    the_stack = []
    # print(line)

    corrupted = False

    for idx, ch in enumerate(line):
        if ch in "([{<":
            the_stack.append(ch)
        else:
            x = the_stack.pop()
            if ch == ')' and x == '(':
                continue
            if ch == '>' and x == '<':
                continue
            if ch == ']' and x == '[':
                continue
            if ch == '}' and x == '{':
                continue

            print(f"{line} corrupted: saw {x} and got {ch}")
            if ch == ')':
                score += 3
            elif ch == ']':
                score += 57
            elif ch == '}':
                score += 1197
            elif ch == '>':
                score += 25137
            corrupted = True
            break

    if not corrupted:
        print(f"{line} incomplete: ", end='')
        bunch = 0
        while len(the_stack) > 0:
            x = the_stack.pop()
            if x == '{':
                print('}', end='')
                bunch = bunch * 5 + 3
            elif x == '[':
                print(']', end='')
                bunch = bunch * 5 + 2
            elif x == '(':
                print(')', end='')
                bunch = bunch * 5 + 1
            elif x == '<':
                print('>', end='')
                bunch = bunch * 5 + 4
        print(f"; score is {bunch}")
        incomplete_scores.append(bunch)

    # print(f"stack has {len(the_stack)}")
    # print()

print(f"total score is {score}")

incomplete_scores.sort()
print(f"incomplete len is {len(incomplete_scores)}")
print(f"middle is {incomplete_scores[int(len(incomplete_scores)/2)]}")

