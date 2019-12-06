def mode(mode_code, num):
    if mode_code == "0":
        return data[num]
    elif mode_code == "1":
        return num


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip().split(",")
    data = [int(x) for x in data]
    # data = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,
    #         20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
    #         999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    position = 0
    test_input = 5
    while data[position] != 99:
        instruction = str(data[position])
        pad = 5 - len(instruction)
        instruction = "0" * pad + instruction
        # print(instruction, position)
        # print(data)
        if instruction[-1] == "1":
            first = mode(instruction[2], data[position + 1])
            second = mode(instruction[1], data[position + 2])
            data[data[position + 3]] = first + second
            position += 4
        elif instruction[-1] == "2":
            first = mode(instruction[2], data[position + 1])
            second = mode(instruction[1], data[position + 2])
            data[data[position + 3]] = first * second
            position += 4
        elif instruction[-1] == "3":
            data[data[position + 1]] = test_input
            position += 2
        elif instruction[-1] == "4":
            first = mode(instruction[2], data[position + 1])
            print(first)
            position += 2
        elif instruction[-1] == "5":
            first = mode(instruction[2], data[position + 1])
            second = mode(instruction[1], data[position + 2])
            if first != 0:
                position = second
            else:
                position += 3
        elif instruction[-1] == "6":
            first = mode(instruction[2], data[position + 1])
            second = mode(instruction[1], data[position + 2])
            if first == 0:
                position = second
            else:
                position += 3
        elif instruction[-1] == "7":
            first = mode(instruction[2], data[position + 1])
            second = mode(instruction[1], data[position + 2])
            if first < second:
                data[data[position + 3]] = 1
            else:
                data[data[position + 3]] = 0
            position += 4
        elif instruction[-1] == "8":
            first = mode(instruction[2], data[position + 1])
            second = mode(instruction[1], data[position + 2])
            if first == second:
                data[data[position + 3]] = 1
            else:
                data[data[position + 3]] = 0
            position += 4
        else:
            print(instruction, position)
            break
