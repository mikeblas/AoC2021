import pprint


def main():

    with open('sample.txt') as my_file:
        input_lines = my_file.readlines()
    input_lines = [s.strip() for s in input_lines]
    line_count = len(input_lines)
    print(f"{line_count} lines read")


    p1_pos = 10
    p2_pos = 9
    p1_score = 0
    p2_score = 0

    rolls = 0
    next_roll = 1
    while p1_score < 1000 and p2_score < 1000:

        distance = 3 * (rolls+1) + 3
        rolls += 3
        p1_pos += distance
        p1_pos = ((p1_pos - 1) % 10) + 1

        p1_score += p1_pos
        print(f"p1 distance = {distance}, position = {p1_pos}, total score = {p1_score}")

        if p1_score >= 1000:
            break

        distance = 3 * (rolls+1) + 3
        rolls += 3
        p2_pos += distance
        p2_pos = ((p2_pos - 1) % 10) + 1

        p2_score += p2_pos

    print(f"{rolls} rolls, {p1_score} vs {p2_score}")
    print(f"{min(p1_score, p2_score) * rolls}")

if __name__ == '__main__':
    main()
