import copy

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
        assert level == self.depth, f"{level=} == {self.depth=}"
        if self.value is None:
            self.left.traverse(level + 1)

        if self.value is not None:
            print(f"{' ' * level}({self.depth}): {self.value}; parent = {self.parent}")

        if self.value is None:
            self.right.traverse(level + 1)

    def magnitude(self):
        if self.value is not None:
            return self.value
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def explode(self):
        exploded, x, y = self.explode_impl(1, None, None)
        return exploded

    def explode_impl(self, level, previous_int, coming_right):
        if self.value is None:
            exploded, previous_int, coming_right = self.left.explode_impl(level + 1, previous_int, coming_right)
            if exploded:
                return True, None, None

        if self.value is not None:
            if coming_right is not None:
                # print(f"adding {coming_right.value} to {self.value}")
                self.value += coming_right.value
                coming_right.parent.value = 0
                coming_right.parent.left = None
                coming_right.parent.right = None
                coming_right = None
                return True, None, None

            if self.depth == 5:
                if self.parent.left == self:
                    # print("LLL: ", end='')
                    if previous_int is not None:
                        previous_int.value += self.value
                        previous_int = None
                elif self.parent.right == self:
                    # print("RRR: ", end='')
                    coming_right = self
            # print(f"{' ' * level}({self.depth}, prev={previous_int}, coming={coming_right}): {self.value}")
            return False, self, coming_right

        if self.value is None:
            exploded, previous_int, coming_right = self.right.explode_impl(level + 1, previous_int, coming_right)
            if exploded:
                return True, None, None

        if level == 1 and coming_right is not None:
            # print(f"exiting {level} with coming_right == {coming_right}")
            coming_right.parent.value = 0
            coming_right.parent.left = None
            coming_right.parent.right = None
            coming_right = None
            return True, None, None

        return False, previous_int, coming_right

    def split(self):
        return self.split_impl(0)

    def split_impl(self, level):
        if self.value is None:
            ret = self.left.split_impl(level + 1)
            if ret:
                return ret

        if self.value is not None:
            if self.value >= 10:
                self.left = XNode(None, None, int(self.value / 2), self.depth + 1)
                self.left.parent = self
                self.right = XNode(None, None, int((self.value+1) / 2), self.depth + 1)
                self.right.parent = self
                self.value = None
                return True
            return False

        if self.value is None:
            ret = self.right.split_impl(level + 1)
            if ret:
                return ret

        return False

    def adjust_depth(self, delta):
        if self.value is None:
            self.left.adjust_depth(delta)

        self.depth += delta

        if self.value is None:
            self.right.adjust_depth(delta)


def add(lhs, rhs):
    lh = copy.deepcopy(lhs)
    rh = copy.deepcopy(rhs)
    rh.adjust_depth(1)
    lh.adjust_depth(1)
    # print(f"\nadd lhs:")
    # lhs.traverse(0)
    # print(f"add rhs:")
    # rhs.traverse(0)

    result = XNode(rh, lh, None, 0)
    rh.parent = result
    lh.parent = result

    while True:
        # print(result)
        if result.explode():
            # print("exploded")
            continue
        if result.split():
            # print("split")
            continue
        break
    return result


def sum_all(input_numbers):

    temp = None

    lhs = None
    for num in input_numbers:

        if lhs is None:
            lhs = num
            temp = lhs
        else:
            rhs = num
            temp = add(lhs, rhs)
            # print(f"\n  {lhs}")
            # print(f"+ {rhs}")
            # print(f"= {temp}")
            # print("lhs:")
            # lhs.traverse(0)
            # print("rhs:")
            # rhs.traverse(0)
            # print("temp:")
            # temp.traverse(0)
            lhs = temp
            rhs = None

    if temp is None:
        return None
    else:
        return temp.magnitude()


def dump_all(input_numbers):

    for num in input_numbers:
        print(f"num = {num}")
        print(f"magnitude = {num.magnitude()}")
        num.traverse(0)
        print(f"-----")


def explode_all(input_numbers):

    for num in input_numbers:
        print(f"before: {num}")
        ret = num.explode()
        print(f"after: {ret} gave {num}")
        print(f"-----")


def main():
    with open('input.txt') as my_file:
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
        # stak[0].traverse(0)

    # dump_all(input_numbers)

    # print("--- exploding!")
    # explode_all(input_numbers)

    result = sum_all(input_numbers)
    print(f"magnitude of total sum is {result}")

    max_found = None
    for outer_idx, outer in enumerate(input_numbers):
        for inner_idx, inner in enumerate(input_numbers):

            if inner_idx == outer_idx:
                continue

            result = add(outer, inner)
            result_magnitude = result.magnitude()
            if max_found is None or max_found < result_magnitude:
                max_found = result_magnitude

    print(f"best magnitude is {max_found}")


if __name__ == '__main__':
    main()