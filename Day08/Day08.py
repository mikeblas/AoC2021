
import pprint

def two_fuel(pos, target):
    dist = abs(pos - target)
    return (dist*(dist+1))/2

with open('input.txt') as my_file:
    input_lines = my_file.readlines()
input_lines = [s.strip() for s in input_lines]
line_count = len(input_lines)

print(f"{line_count} lines read")
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

print(f"{my_count} digits are 1, 4, 7, or 8")


# -- part 2

output_total = 0

for line in input_lines:

    in_out = line.split("|")
    input_digits = ["".join(sorted(d.strip())) for d in in_out[0].strip().split(" ")]
    output_digits = ["".join(sorted(d.strip())) for d in in_out[1].strip().split(" ")]

    all_digits = input_digits + output_digits

    # print(all_digits)

    # find the identity characters by count
    # len 2 --> '1'
    # len 3 --> '7'
    # len 4 --> '4'
    # len 7 --> '8'
    # ---
    # len 5 --> '2' or '3' or '5'
    # len 6 --> '0' or '6' or '9'

    segs_to_num = {}
    num_to_segs = {}

    for digit in all_digits:
        if len(digit) == 7:
            segs_to_num[digit] = 8
            num_to_segs[8] = digit
        elif len(digit) == 2:
            segs_to_num[digit] = 1
            num_to_segs[1] = digit
        elif len(digit) == 3:
            segs_to_num[digit] = 7
            num_to_segs[7] = digit
        elif len(digit) == 4:
            segs_to_num[digit] = 4
            num_to_segs[4] = digit

    real_a = set(num_to_segs[7]).difference(set(num_to_segs[1]))
    real_bd = set(num_to_segs[4]).difference(set(num_to_segs[1]))

    # print(f"{real_a=}")
    # print(f"{real_bd=}")

    for digit in all_digits:
        if len(digit) == 6:
            if len(set(digit) - set(num_to_segs[4])) == 2:
                segs_to_num[digit] = 9
                num_to_segs[9] = digit
            elif len(set(digit) - set(num_to_segs[1])) == 4:
                segs_to_num[digit] = 0
                num_to_segs[0] = digit
            elif len(set(digit) - set(num_to_segs[1])) == 5:
                segs_to_num[digit] = 6
                num_to_segs[6] = digit
        elif len(digit) == 5:
            if len(set(digit) - set(num_to_segs[1])) == 3:
                segs_to_num[digit] = 3
                num_to_segs[3] = digit
            elif len(set(digit) - set(num_to_segs[4])) == 3:
                segs_to_num[digit] = 2
                num_to_segs[2] = digit
            else:
                segs_to_num[digit] = 5
                num_to_segs[5] = digit

    # print(segs_to_num)
    # print(num_to_segs)

    temp = 0
    for digit in output_digits:
        if digit in segs_to_num:
            temp = (10 * temp) + segs_to_num[digit]
        else:
            print(f"{digit} --> Not found")

    output_total += temp

print(output_total)


