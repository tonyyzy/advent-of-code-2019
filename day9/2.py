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
            # print(position, positions)
            data += [0 for i in range(lim - len(data) + 1)]


    relative_base = 0
    # print(inputs)
    while data[position] != 99:
        instruction = str(data[position])
        pad = 5 - len(instruction)
        instruction = "0" * pad + instruction
        # data = extend_data(data, position)
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
            # print("3 is called")
            # print(data[position: position + 2])
            first = mode(instruction[2], position + 1)
            # print(position, instruction, relative_base, first)
            extend_data([first])
            data[first] = inputs
            position += 2
        elif instruction[-1] == "4":
            first = mode(instruction[2], position + 1)
            extend_data([first])
            print(data[first])
            position += 2
            # return first, position, data 
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
            # print(position, instruction, relative_base, first)
            position += 2
        else:
            print(instruction, position)
            break

if __name__ == "__main__":
    # data1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    # data2 = [1102,34915192,34915192,7,4,7,99,0]
    # data3 = [104,1125899906842624,99]
    # IntComputer(data1, 0)
    # IntComputer(data2, 0)
    # IntComputer(data3, 0)
    with open("input.txt") as f:
        data = f.read().strip().split(",")
    data = [int(x) for x in data]
    IntComputer(data, 2)