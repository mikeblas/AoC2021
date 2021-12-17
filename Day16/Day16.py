import sys

version_sum = 0

op_root = None


class Operation:
    def __init__(self, level, is_operator, value):
        self.level = level
        self.is_operator = is_operator
        self.value = value
        self.children = []

    def __repr__(self):
        if self.is_operator:
            return f"{self.level}: operator {self.value}"
        else:
            return f"{self.level}: value {self.value}"

    def traverse(self, depth):
        print(f"{' ' * depth}{self}")
        for child in self.children:
            child.traverse(depth+1)

    def evaluate(self):
        result = None

        if not self.is_operator:
            result = self.value
        else:
            if self.value == 0:
                result = 0
                for child in self.children:
                    result += child.evaluate()
            elif self.value == -1:
                result = self.children[0].evaluate()
            elif self.value == 1:
                result = 1
                for child in self.children:
                    result *= child.evaluate()
            elif self.value == 2:
                result = sys.maxsize
                for child in self.children:
                    x = child.evaluate()
                    if x < result:
                        result = x
            elif self.value == 3:
                result = -sys.maxsize
                for child in self.children:
                    x = child.evaluate()
                    if x > result:
                        result = x
            elif self.value == 5:
                left = self.children[0].evaluate()
                right = self.children[1].evaluate()
                result = 1 if left > right else 0
            elif self.value == 6:
                left = self.children[0].evaluate()
                right = self.children[1].evaluate()
                result = 1 if left < right else 0
            elif self.value == 7:
                left = self.children[0].evaluate()
                right = self.children[1].evaluate()
                result = 1 if left == right else 0

        return result



def get_version_type(bits, idx):
    version = int(bits[idx:idx+3], 2)
    global version_sum
    version_sum += version
    packet_type = int(bits[idx+3:idx+6], 2)
    return version, packet_type, idx+6


def get_operator(level, bits, idx, parent):
    length_type = bits[idx]
    if length_type == '0':
        length = int(bits[idx+1:idx+16], 2)
        internal_bits = idx + 1 + 15
        idx += length + 1 + 15
        print(f" level {level} operator bits, len = {length}")
        while internal_bits < idx:
            internal_bits = read_packet(level + 1, bits, internal_bits, parent)
        print(f" done, {idx} and {internal_bits}")
    else:
        packet_count = int(bits[idx+1:idx+12], 2)
        idx += 12
        print(f" operator packets, count = {packet_count}")
        while packet_count > 0:
            idx = read_packet(level + 1, bits, idx, parent)
            packet_count -= 1

    return idx


def get_literal(bits, idx):
    value = 0
    while True:
        more = bits[idx]
        four = bits[idx+1:idx+5]

        idx += 5
        value = value * 16
        value = value + int(four, 2)

        if more == '0':
            break
    return value, idx


def read_packet(level, bits, idx, parent):
    version, packet_type, idx = get_version_type(bits, idx)
    print(f"level {level} version = {version}, type = {packet_type}")

    if packet_type == 4:
        value, idx = get_literal(bits, idx)
        print(f" level {level} literal: {value}")

        parent.children.append(Operation(level, False, value))
    else:
        new_parent = Operation(level, True, packet_type)
        parent.children.append(new_parent)
        idx = get_operator(level, bits, idx, new_parent)

    return idx


def main():
    with open('input.txt') as my_file:
        input_lines = my_file.readlines()
    input_lines = [s.strip() for s in input_lines]
    line_count = len(input_lines)
    print(f"{line_count} lines read")

    # read hex input and convert to binary, 2 at a time
    total = ""
    for idx in range(0, len(input_lines[0]), 2):
        two = input_lines[0][idx:idx+2]
        part = bin(int(two, 16))[2:].zfill(8)
        total += part

    print(total)

    idx = 0
    while idx < len(total):
        op_root = Operation(0, True, -1)
        idx = read_packet(0, total, idx, op_root)
        break

    print(f"version_sum = {version_sum}")

    print("\noperator tree:")
    op_root.traverse(0)
    res = op_root.evaluate()
    print(res)


if __name__ == '__main__':
    main()

