
import pprint


def get_pixel(image_data, x, y, blank_default):

    # imaginary pixels beyond bounds
    if x < 0 or y < 0:
        return blank_default
    if y >= len(image_data):
        return blank_default
    if x >= len(image_data[0]):
        return blank_default

    pixel = 0 if image_data[y][x] == '.' else 1
    return pixel


def get_index(image, x, y, blank_default):

    index = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            bit = get_pixel(image, x + dx, y + dy, blank_default)
            index *= 2
            index += bit
    return index


# offer 2.275
# counter 2.340
# counter

def process_image(decoder, image, blank_default):

    # 4 taller and 4 wider; top corner leaves 2 more left and 2 more up
    # (for example)
    output = [['.' for x in range(len(image[0])+4)] for y in range(len(image) + 4)]

    for y in range(len(output)):
        for x in range(len(output[0])):
            index = get_index(image, x-2, y-2, blank_default)
            pixel = decoder[index]
            output[y][x] = '.' if pixel == '.' else '#'

    if blank_default == 0:
        # 9 bits of 0
        t = decoder[0]
        blank_default = 0 if t == '.' else 1
    else:
        # 9 bits of 1
        t = decoder[0b111111111]
        blank_default = 0 if t == '.' else 1

    return output, blank_default


def count_ones(image):
    counted = 0
    for y in range(len(image)):
        for x in range(len(image[0])):
            if image[y][x] == '#':
                counted += 1
    return counted


def main():
    with open('input.txt') as my_file:
        input_lines = my_file.readlines()
    input_lines = [s.strip() for s in input_lines]
    line_count = len(input_lines)
    print(f"{line_count} lines read")

    decoder = input_lines[0]

    image_data = input_lines[2:]

    print(image_data)

    input_image = image_data
    blank_default = 0
    (output_image, blank_default) = process_image(decoder, input_image, 0)
    for y in output_image:
        print("".join(y))
    print(f"{blank_default}, {count_ones(output_image)}")

    (output_image, blank_default) = process_image(decoder, output_image, blank_default)
    for y in output_image:
        print("".join(y))
    print(f"{blank_default}, {count_ones(output_image)}")


if __name__ == '__main__':
    main()

