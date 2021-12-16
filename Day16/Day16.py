version_sum = 0




def get_version_type(bits, idx):
    version = int(bits[idx:idx+3], 2)
    global version_sum
    version_sum += version
    packet_type = int(bits[idx+3:idx+6], 2)
    return version, packet_type, idx+6


def get_operator(bits, idx):

    length_type = bits[idx]
    if length_type == '0':
        length = int(bits[idx+1:idx+16], 2)
        internal_bits = idx + 1 + 15
        idx += length + 1 + 15
        print(f" operator bits, len = {length}")
        while internal_bits < idx:
            internal_bits = read_packet(bits, internal_bits)
        print(f" done, {idx} and {internal_bits}")
    else:
        packet_count = int(bits[idx+1:idx+12], 2)
        idx += 12
        print(f" operator packets, count = {packet_count}")
        while packet_count > 0:
            idx = read_packet(bits, idx)
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


def read_packet(bits, idx):
    version, packet_type, idx = get_version_type(bits, idx)
    print(f"version = {version}, type = {packet_type}")

    if packet_type == 4:
        value, idx = get_literal(bits, idx)
        print(f" literal: {value}")
    else:
        idx = get_operator(bits, idx)

    return idx


def main():
    with open('sample1_8.txt') as my_file:
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
        idx = read_packet(total, idx)
        break

    print(f"version_sum = {version_sum}")

if __name__ == '__main__':
    main()

