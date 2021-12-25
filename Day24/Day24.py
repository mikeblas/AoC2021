


def main():
    with open('input.txt') as my_file:
        input_lines = my_file.readlines()
    input_lines = [s.strip() for s in input_lines]
    line_count = len(input_lines)
    print(f"{line_count} lines read")

    instructions = [x.split(' ') for x in input_lines]
    print(instructions)

    #       12345678901234
    args = 'abcdefghijklmn'
    arg_idx = 0
    registers = { 'x': '0', 'w': '0', 'y': '0', 'z': '0' }
    is_variant = { 'x': False, 'y': False, 'z': False, 'w': False}

    for step in instructions:
        print(f"{step}:   :", end='')
        if step[0] == 'inp':
            registers[step[1]] = args[arg_idx]
            arg_idx += 1
            is_variant[step[1]] = True
            print(f"{step[1]} == {registers[step[1]]}")
        else:
            is_variant[step[1]] = False
            if step[2] in ['w', 'x', 'y', 'z']:
                variant = True
                arg2 = registers[step[2]]
            else:
                variant = False
                arg2 = step[2]
            # arg2 = step[2]

            if step[0] == 'mul':
                registers[step[1]] = f"({registers[step[1]]}) * {arg2}"
                registers[step[1]] = eval(registers[step[1]])
            elif step[0] == 'div':
                registers[step[1]] = f"({registers[step[1]]}) // {arg2}"
                registers[step[1]] = eval(registers[step[1]])
            elif step[0] == 'mod':
                registers[step[1]] = f"({registers[step[1]]}) % {arg2}"
                registers[step[1]] = eval(registers[step[1]])
            elif step[0] == 'add':
                registers[step[1]] = f"({registers[step[1]]}) + {arg2}"
                registers[step[1]] = eval(registers[step[1]])
            elif step[0] == 'eql':
                if not is_variant[step[1]] and (not variant or not is_variant[step[2]]):
                    registers[step[1]] = f"(({registers[step[1]]}) == {arg2})"
                    result = eval(registers[step[1]])
                    registers[step[1]] = '1' if result else '0'
                else:
                    if int(registers[step[1]]) >= 10 or int(registers[step[1]]) <= 0:
                        registers[step[1]] = '0'

            print(f"{step[1]} == {registers[step[1]]}")

    print(registers)


if __name__ == '__main__':
    main()

