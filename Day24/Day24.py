


def main():
    with open('input.txt') as my_file:
        input_lines = my_file.readlines()
    input_lines = [s.strip() for s in input_lines]
    line_count = len(input_lines)
    print(f"{line_count} lines read")

    instructions = [x.split(' ') for x in input_lines]
    print(instructions)

    args = '13579246899999'
    arg_idx = 0
    registers = { 'x': 0, 'w': 0, 'y': 0, 'z': 0 }

    for step in instructions:
        print(f"{step}:   :", end='')
        if step[0] == 'inp':
            registers[step[1]] = int(args[arg_idx])
            arg_idx += 1
            print(f"{step[1]} == {registers[step[1]]}")
        else:
            if step[2] in ['w', 'x', 'y', 'z']:
                arg2 = registers[step[2]]
            else:
                arg2 = int(step[2])

            if step[0] == 'mul':
                registers[step[1]] = registers[step[1]] * arg2
            elif step[0] == 'div':
                registers[step[1]] = registers[step[1]] // arg2
            elif step[0] == 'mod':
                registers[step[1]] = registers[step[1]] % arg2
            elif step[0] == 'add':
                registers[step[1]] = registers[step[1]] + arg2
            elif step[0] == 'eql':
                registers[step[1]] = 1 if registers[step[1]] == arg2 else 0
            print(f"{step[1]} == {registers[step[1]]}")

    print(registers)


if __name__ == '__main__':
    main()

