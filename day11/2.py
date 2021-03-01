def IntComputer(data, inputs, position=0):
    def mode(mode_code, pos):
        """Decode different mode
        
        Arguments:
            num {[type]} -- [description]
        
        Returns:
            int -- position of the value
        """
        nonlocal data
        if mode_code == "0":
            return data[pos]
        elif mode_code == "1":
            return pos
        elif mode_code == "2":
            return relative_base + data[pos]
    
    def extend_data(positions):
        nonlocal data
        lim = max(positions)
        if lim >= len(data):
            data += [0 for i in range(lim - len(data) - 10)]

    output = []
    relative_base = 0
    # print(inputs)
    while data[position] != 99:
        instruction = str(data[position])
        pad = 5 - len(instruction)
        instruction = "0" * pad + instruction
        # print(instruction, position, data)
        if instruction[-1] == "1":
            first = mode(instruction[2], position + 1)
            second = mode(instruction[1], position + 2)
            third = mode(instruction[0], position + 3)
            extend_data([first, second, third])
            data[third] = data[first] + data[second]
            position += 4
        elif instruction[-1] == "2":
            first = mode(instruction[2], position + 1)
            second = mode(instruction[1], position + 2)
            third = mode(instruction[0], position + 3)
            extend_data([first, second, third])
            data[third] = data[first] * data[second]
            position += 4
        elif instruction[-1] == "3":
            first = mode(instruction[2], position + 1)
            extend_data([first])
            data[first] = inputs
            position += 2
        elif instruction[-1] == "4":
            first = mode(instruction[2], position + 1)
            extend_data([first])
            position += 2
            if len(output) == 1:
                output.append(data[first])
                return data, position, output
            elif len(output) == 0:
                output.append(data[first])
        elif instruction[-1] == "5":
            first = mode(instruction[2], position + 1)
            second = mode(instruction[1], position + 2)
            extend_data([first, second])
            if data[first] != 0:
                position = data[second]
            else:
                position += 3
        elif instruction[-1] == "6":
            first = mode(instruction[2], position + 1)
            second = mode(instruction[1], position + 2)
            extend_data([first, second])
            if data[first] == 0:
                position = data[second]
                if position == 0:
                    print(instruction, first, second)
            else:
                position += 3
        elif instruction[-1] == "7":
            first = mode(instruction[2], position + 1)
            second = mode(instruction[1], position + 2)
            third = mode(instruction[0], position + 3)
            extend_data([first, second, third])
            if data[first] < data[second]:
                data[third] = 1
            else:
                data[third] = 0
            position += 4
        elif instruction[-1] == "8":
            first = mode(instruction[2], position + 1)
            second = mode(instruction[1], position + 2)
            third = mode(instruction[0], position + 3)
            extend_data([first, second, third])
            if data[first] == data[second]:
                data[third] = 1
            else:
                data[third] = 0
            position += 4
        elif instruction[-1] == "9":
            first = mode(instruction[2], position + 1)
            extend_data([first])
            relative_base += data[first]
            position += 2
        else:
            print(instruction, position)
            break
    return data, position, None

if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip().split(",")
    data = [int(x) for x in data]
    current_pos = [0, 0]
    direction = 1 #1, 2, 3, 4: up, left, down, right
    # painted = []
    color = {(0, 0): 1}
    data, position, output = IntComputer(data, color[tuple(current_pos)], position=0)
    while output != None:
        color[tuple(current_pos)] = output[0]
        if output[1] == 0:
            direction += 1
            if direction == 5:
                direction = 1
        elif output[1] == 1:
            direction -= 1
            if direction == 0:
                direction = 4
        if direction == 1:
            current_pos[1] += 1
        elif direction == 2:
            current_pos[0] -= 1
        elif direction == 3:
            current_pos[1] -= 1
        elif direction == 4:
            current_pos[0] += 1
        if tuple(current_pos) not in color.keys():
            color[tuple(current_pos)] = 0
        # print(color[tuple(current_pos)], position)
        # print(data)
        data, position, output = IntComputer(data, color[tuple(current_pos)], position=position)
    print(len(color.keys()))
    # x = [i[0] for i in color.keys()]
    # y = [i[1] for i in color.keys()]
    # x_max, x_min, y_max, y_min = max(x), min(x), max(y), min(y)
    # x_range = x_max - x_min + 1
    # y_range = y_max - y_min + 1
    # paint = [["*" for i in range(x_range)] for j in range(y_range)]
    # print(len(paint), len(paint[0]))
    # for key, val in color.items():
    #     if val == 1:
    #         paint[key[1] - y_min][key[0] - x_min] = "0"
    # for line in paint:
    #     print("".join(line))
