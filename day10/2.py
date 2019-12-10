from math import atan2, pi


def transform(coord, station):
    new_coord = []
    for i in coord:
        new_coord.append((i[0] - station[0], station[1] - i[1]))
    new_coord.remove((0, 0))
    return new_coord



if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.readlines()
    coord = []
    for yind, line in enumerate(data):
        for xind, pos in enumerate(line.strip()):
            if pos == "#":
                coord.append((xind, yind))
    best = []
    station = (13, 17)
    new_coord = transform(coord, station)
    angles = {}
    for pos in new_coord:
        angle = atan2(*pos)
        if angle < 0:
            angle += 2 * pi
        if angle not in angles.keys():
            angles[angle] = []
        angles[angle].append(pos)
    counter = 0
    while counter <= 200:
        for i in sorted(angles.keys()):
            if len(angles[i]) > 0:
                counter += 1
                smallest = [x[0] + x[1] for x in angles[i]]
                smallest_index = smallest.index(min(smallest))
                popped = angles[i].pop(smallest_index)
            if counter == 200:
                print(counter, (popped[0] + station[0], station[1] - popped[1]))
                break