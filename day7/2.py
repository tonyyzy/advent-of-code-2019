from itertools import permutations

def mode(data, mode_code, num):
    if mode_code == "0":
        return data[num]
    elif mode_code == "1":
        return num

def IntComputer(data, inputs, position=0):
    input_counter = 0
    # print(inputs)
    while data[position] != 99:
        instruction = str(data[position])
        pad = 5 - len(instruction)
        instruction = "0" * pad + instruction
        # print(instruction, position, data)
        if instruction[-1] == "1":
            first = mode(data, instruction[2], data[position + 1])
            second = mode(data, instruction[1], data[position + 2])
            data[data[position + 3]] = first + second
            position += 4
        elif instruction[-1] == "2":
            first = mode(data, instruction[2], data[position + 1])
            second = mode(data, instruction[1], data[position + 2])
            data[data[position + 3]] = first * second
            position += 4
        elif instruction[-1] == "3":
            # print("3 is called")
            data[data[position + 1]] = inputs[input_counter]
            input_counter += 1
            position += 2
        elif instruction[-1] == "4":
            first = mode(data, instruction[2], data[position + 1])
            # print(first)
            position += 2
            return first, position, data 
        elif instruction[-1] == "5":
            first = mode(data, instruction[2], data[position + 1])
            second = mode(data, instruction[1], data[position + 2])
            if first != 0:
                position = second
            else:
                position += 3
        elif instruction[-1] == "6":
            first = mode(data, instruction[2], data[position + 1])
            second = mode(data, instruction[1], data[position + 2])
            if first == 0:
                position = second
            else:
                position += 3
        elif instruction[-1] == "7":
            first = mode(data, instruction[2], data[position + 1])
            second = mode(data, instruction[1], data[position + 2])
            if first < second:
                data[data[position + 3]] = 1
            else:
                data[data[position + 3]] = 0
            position += 4
        elif instruction[-1] == "8":
            first = mode(data, instruction[2], data[position + 1])
            second = mode(data, instruction[1], data[position + 2])
            if first == second:
                data[data[position + 3]] = 1
            else:
                data[data[position + 3]] = 0
            position += 4
        else:
            print(instruction, position)
            break

if __name__ == "__main__":
    with open("input.txt") as f:
        programme = f.read().strip().split(",")
    programme = [int(x) for x in programme]
    thrusts = []

    for seq in permutations(range(5, 10), 5):
        position = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
            "E": 0,
        }
        data_store = {
            "A": programme.copy(),
            "B": programme.copy(),
            "C": programme.copy(),
            "D": programme.copy(),
            "E": programme.copy(),
        }
        output = 0
        for i in zip(seq, ["A", "B", "C", "D", "E"]):
            try:
                output, position[i[1]], data_store[i[1]] = IntComputer(data_store[i[1]], [i[0], output], position=position[i[1]])
            except:
                print(output)
                thrusts.append(output)
        a = 0
        while a == 0:
            for i in ["A", "B", "C", "D", "E"]:
                try:
                    output, position[i], data_store[i] = IntComputer(data_store[i], [output], position = position[i])
                except:
                    thrusts.append(output)
                    a = 1
    print(max(thrusts))
