import sys


class XNode:
    def __init__(self, b, a, value, depth):
        # print(f"init: {b}, {a}, {value}, {depth}")
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

        if self.value is None:
            self.left.traverse(level + 1)

        if self.value is not None:
            print(f"{' ' * level}({self.depth}): {self.value}")

        if self.value is None:
            self.right.traverse(level + 1)

    def traverse2(self, level):
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

        if self.value is None:
            previous_int, coming_right = self.left.explode(level + 1, previous_int, coming_right)

        if self.value is not None:
            if coming_right is not None:
                print(f"adding {coming_right.value} to {self.value}")
                self.value += coming_right.value
                coming_right = None
            if self.depth == 5:
                if self.parent.left == self:
                    print("LLL: ", end='')
                    if previous_int is not None:
                        previous_int.value += self.value
                        previous_int = None
                elif self.parent.right == self:
                    print("RRR: ", end='')
                    coming_right = self
            print(f"{' ' * level}({self.depth}, prev={previous_int}, coming={coming_right}): {self.value}")
            return self, coming_right

        if self.value is None:
            previous_int, coming_right = self.right.explode(level + 1, previous_int, coming_right)

        return previous_int, coming_right


def add(lhs, rhs):
    result = XNode(rhs, lhs)
    result.explode(1, None, None)
    return result


def sum_all(input_numbers):
    lhs = None
    rhs = None

    for num in input_numbers:

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


def dump_all(input_numbers):

    for num in input_numbers:
        print(f"num = {num}")
        print(f"magnitude = {num.magnitude()}")
        num.traverse(0)
        print(f"-----")


def explode_all(input_numbers):

    for num in input_numbers:
        print(f"before: {num}")
        num.explode(1, None, None)
        print(f"after: {num}")
        print(f"-----")


def main():
    with open('explode1.txt') as my_file:
        input_lines = my_file.readlines()
    input_lines = [s.strip() for s in input_lines]
    line_count = len(input_lines)
    print(f"{line_count} lines read")

    input_numbers = []

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

        input_numbers.append(stak[0])
        num = stak[0]

    dump_all(input_numbers)

    print("--- exploding!")
    explode_all(input_numbers)

    # sum_all(input_numbers)



if __name__ == '__main__':
    main()