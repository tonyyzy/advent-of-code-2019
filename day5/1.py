def mode(mode_code, num):
    if mode_code == "0":
        return data[num]
    elif mode_code == "1":
        return num


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip().split(",")
    data = [int(x) for x in data]
    position = 0
    while data[position] != 99 or position < len(data):
        instruction = str(data[position])
        pad = 5 - len(instruction)
        instruction = "0" * pad + instruction
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
            data[data[position + 1]] = 1
            position += 2
        elif instruction[-1] == "4":
            print(data[data[position + 1]])
            position += 2
        else:
            break
