import sys

def dissolve(num, level, tl):

    if type(num) == tuple:
        tl = dissolve(num[0], level+1, tl)
        tl = dissolve(num[1], level+1, tl)
        return tl
    else:
        print(f"{' ' * level}: {num}")
        tl.append((level, num))
        return tl


def main():
    with open('sample.txt') as my_file:
        input_lines = my_file.readlines()
    input_lines = [s.strip() for s in input_lines]
    line_count = len(input_lines)
    print(f"{line_count} lines read")


    lhs = None
    rhs = None

    for s in input_lines:
        stak = []
        for ch in s:
            if ch >= '0' and ch <= '9':
                stak.append(int(ch))
            elif ch == ',':
                continue
            elif ch == ']':
                a = stak.pop()
                b = stak.pop()
                stak.append((b, a))

        print(f"{stak}, {len(stak)}")
        num = stak[0]

        q = dissolve(num, 0, [])
        print(f"q = {q}")

        cur_level = 0
        first = True
        level_stack = []
        for level, number in q:
            if cur_level < level:
                print('(' * (level-cur_level), end='')
                for x in range(level - cur_level):
                    level_stack.append(True)
                cur_level = level
            elif cur_level > level:
                print(')' * (cur_level - level), end='')
                for x in range(cur_level - level):
                    level_stack.pop()
                cur_level = level
            else:
                if level_stack[-1]:
                    print(', ', end='')
                else:
                    print('(=', end='')
            print(number, end='')

        if  cur_level > 0:
            print(')' * cur_level, end='')
        print()






if __name__ == '__main__':
    main()