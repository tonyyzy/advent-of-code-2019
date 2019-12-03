def find_coord(path):
    coord = []
    current = [0,0]
    steps = {}
    step_count = 0
    for move in path:
        if move[0] == "U":
            for step in range(0, int(move[1:])):
                current[1] += 1
                step_count += 1
                coord.append(tuple(current))
                if tuple(current) not in steps.keys():
                    steps[tuple(current)] = step_count

        elif move[0] == "R":
            for step in range(0, int(move[1:])):
                current[0] += 1
                step_count += 1
                coord.append(tuple(current))
                if tuple(current) not in steps.keys():
                    steps[tuple(current)] = step_count

        elif move[0] == "D":
            for step in range(0, int(move[1:])):
                current[1] -= 1
                step_count += 1
                coord.append(tuple(current))
                if tuple(current) not in steps.keys():
                    steps[tuple(current)] = step_count

        elif move[0] == "L":
            for step in range(0, int(move[1:])):
                current[0] -= 1
                step_count += 1
                coord.append(tuple(current))
                if tuple(current) not in steps.keys():
                    steps[tuple(current)] = step_count
    
    return set(coord), steps

def manhattan(coord):
    return abs(coord[0]) + abs(coord[1])

if __name__ == "__main__":
    with open("input.txt") as file:
        data = file.readlines()
    a, a_steps = find_coord(data[0].strip().split(","))
    b, b_steps = find_coord(data[1].strip().split(","))
    common = a.intersection(b)
    dist = [a_steps[x] + b_steps[x] for x in common]
    print(min(dist))

