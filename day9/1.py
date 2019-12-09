def IntComputer(data, inputs, position=0):
    def mode(data, mode_code, num):
        if mode_code == "0":
            if num >= len(data):
                data += [0 for i in range(num - len(data) + 1)]
            return data, data[num]
        elif mode_code == "1":
            return data, num
        elif mode_code == "2":
            if relative_base + num >= len(data):
                data += [0 for i in range(relative_base + num - len(data) + 1)]
            return data, data[relative_base + num]
    
    def extend_data(data, position):
        length = max(data[position + 1: position + 4])
        if length >= len(data):
            data += [0 for i in range(length - len(data))]
        return data

    relative_base = 0
    # print(inputs)
    while data[position] != 99:
        instruction = str(data[position])
        pad = 5 - len(instruction)
        instruction = "0" * pad + instruction
        # data = extend_data(data, position)
        # print(instruction, position, data)
        if instruction[-1] == "1":
            data, first = mode(data, instruction[2], data[position + 1])
            data, second = mode(data, instruction[1], data[position + 2])
            if data[position + 3] >= len(data):
                data += [0 for i in range(data[position + 3] - len(data) + 1)]
            data[data[position + 3]] = first + second
            position += 4
        elif instruction[-1] == "2":
            data, first = mode(data, instruction[2], data[position + 1])
            data, second = mode(data, instruction[1], data[position + 2])
            if data[position + 3] >= len(data):
                data += [0 for i in range(data[position + 3] - len(data) + 1)]
            data[data[position + 3]] = first * second
            position += 4
        elif instruction[-1] == "3":
            print("3 is called")
            print(data[position: position + 2])
            data, first = mode(data, instruction[2], data[position + 1])
            print(position, instruction, relative_base, first)
            print(len(data))
            data[first] = inputs
            position += 2
        elif instruction[-1] == "4":
            data, first = mode(data, instruction[2], data[position + 1])
            print(first)
            position += 2
            # return first, position, data 
        elif instruction[-1] == "5":
            data, first = mode(data, instruction[2], data[position + 1])
            data, second = mode(data, instruction[1], data[position + 2])
            if first != 0:
                position = second
            else:
                position += 3
        elif instruction[-1] == "6":
            data, first = mode(data, instruction[2], data[position + 1])
            data, second = mode(data, instruction[1], data[position + 2])
            if first == 0:
                position = second
            else:
                position += 3
        elif instruction[-1] == "7":
            data, first = mode(data, instruction[2], data[position + 1])
            data, second = mode(data, instruction[1], data[position + 2])
            if data[position + 3] >= len(data):
                data += [0 for i in range(data[position + 3] - len(data) + 1)]
            if first < second:
                data[data[position + 3]] = 1
            else:
                data[data[position + 3]] = 0
            position += 4
        elif instruction[-1] == "8":
            data, first = mode(data, instruction[2], data[position + 1])
            data, second = mode(data, instruction[1], data[position + 2])
            if data[position + 3] >= len(data):
                data += [0 for i in range(data[position + 3] - len(data) + 1)]
            if first == second:
                data[data[position + 3]] = 1
            else:
                data[data[position + 3]] = 0
            position += 4
        elif instruction[-1] == "9":
            data, first = mode(data, instruction[2], data[position + 1])
            # print(relative_base)
            relative_base += first
            position += 2
        else:
            print(instruction, position)
            break

if __name__ == "__main__":
    # data = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    # data = [1102,34915192,34915192,7,4,7,99,0]
    # data = [104,1125899906842624,99]
    with open("input.txt") as f:
        data = f.read().strip().split(",")
    data = [int(x) for x in data]
    print(len(data))
    IntComputer(data, 1)