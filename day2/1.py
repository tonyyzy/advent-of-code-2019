if __name__ == "__main__":
    with open("input.txt") as file:
        intcode = file.readlines()[0].strip()
    intcode = [int(x) for x in intcode.split(",")]
    intcode[1] = 12
    intcode[2] = 2
    for optcode in range(0, len(intcode), 4):
        if intcode[optcode] == 1:
            intcode[intcode[optcode + 3]] = intcode[intcode[optcode + 1]] + intcode[intcode[optcode + 2]]
        elif intcode[optcode] == 2:
            intcode[intcode[optcode + 3]] = intcode[intcode[optcode + 1]] * intcode[intcode[optcode + 2]]
        elif intcode[optcode] == 99:
            break
    print(intcode[0])
        