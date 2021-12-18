import sys


class XNode:
    def __init__(self, b, a):
        if type(a) == int:
            self.left_int = a
            self.left_child = None
        else:
            self.left_int = None
            self.left_child = a

        if type(b) == int:
            self.right_int = b
            self.right_child = None
        else:
            self.right_int = None
            self.right_child = b

    def __repr__(self):
        lhs = f"{self.left_int}" if self.left_int is not None else f"{self.left_child}"
        rhs = f"{self.right_int}" if self.right_int is not None else f"{self.right_child}"
        return f"({lhs}, {rhs})"

    def traverse(self, level):

        if self.left_int is not None:
            print(f"{' ' * level}: {self.left_int}")
        else:
            self.left_child.traverse(level+1)

        if self.right_int is not None:
            print(f"{' ' * level}: {self.right_int}")
        else:
            self.right_child.traverse(level+1)


    def magnitude(self):

        if self.left_int is not None:
            lhs = self.left_int
        else:
            lhs = self.left_child.magnitude()

        if self.right_int is not None:
            rhs = self.right_int
        else:
            rhs = self.right_child.magnitude()

        return 3 * lhs + 2 * rhs




def add(lhs, rhs):
    result = XNode(rhs, lhs)
    return result


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
                xa = stak.pop()
                xb = stak.pop()
                x = XNode(xa, xb)
                stak.append(x)

        num = stak[0]
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