from itertools import product

def output(intlist):
    for optcode in range(0, len(intlist), 4):
        if intlist[optcode] == 1:
            intlist[intlist[optcode + 3]] = intlist[intlist[optcode + 1]] + intlist[intlist[optcode + 2]]
        elif intlist[optcode] == 2:
            intlist[intlist[optcode + 3]] = intlist[intlist[optcode + 1]] * intlist[intlist[optcode + 2]]
        elif intlist[optcode] == 99:
            break
    return intlist[0]



if __name__ == "__main__":
    with open("input.txt") as file:
        intcode = file.readlines()[0].strip()
    intcode = [int(x) for x in intcode.split(",")]
    int_bak = intcode.copy()
    for i, j in product(range(100), repeat=2):
        intcode = int_bak.copy()
        intcode[1] = i
        intcode[2] = j
        try:
            out = output(intcode)
            if out == 19690720:
                print(i, j)
                break
        except:
            pass
