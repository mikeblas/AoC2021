import sys


class XNode:
    def __init__(self, b, a, value, depth):
        self.left = a
        self.right = b
        self.value = value
        self.parent = None
        self.depth = depth

    def __repr__(self):
        if self.value is not None:
            return f"{self.value}"
        else:
            lhs = f"{self.left}"
            rhs = f"{self.right}"
            return f"({lhs}, {rhs})"

    def traverse(self, level):
        if self.value is not None:
            print(f"{' ' * level}({self.depth}): {self.value}")
        else:
            self.left.traverse(level + 1)
            self.right.traverse(level + 1)

    def magnitude(self):
        if self.value is not None:
            return self.value
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def explode(self, level, previous_int, coming_right):

        return


def add(lhs, rhs):
    result = XNode(rhs, lhs)
    result.explode(1, None, None)
    return result


def main():
    with open('explode1.txt') as my_file:
        input_lines = my_file.readlines()
    input_lines = [s.strip() for s in input_lines]
    line_count = len(input_lines)
    print(f"{line_count} lines read")


    lhs = None
    rhs = None

    for s in input_lines:
        stak = []
        depth = 0
        for ch in s:
            if ch == '[':
                depth += 1
            elif '0' <= ch <= '9':
                stak.append(XNode(None, None, int(ch), depth))
            elif ch == ',':
                continue
            elif ch == ']':
                xa = stak.pop()
                xb = stak.pop()
                depth -= 1
                x = XNode(xa, xb, None, depth)
                xa.parent = x
                xb.parent = x
                stak.append(x)

        num = stak[0]
        print(f"num = {num}")
        num.explode(1, None, None)
        print(f"num = {num}")
        print(f"magnitude = {num.magnitude()}")

        num.traverse(0)

        if lhs is None:
            lhs = num
        else:
            if rhs is None:
                rhs = num
                temp = add(lhs, rhs)
                print(f"  {lhs}")
                print(f"+ {rhs}")
                print(f"= {temp}")
                lhs = temp
                rhs = None




if __name__ == '__main__':
    main()