from math import atan2


def transform(coord, station):
    new_coord = []
    for i in coord:
        new_coord.append((i[0] - station[0], i[1] - station[1]))
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
    for station in coord:
        new_coord = transform(coord, station)
        angles = []
        for pos in new_coord:
            angles.append(atan2(pos[1], pos[0]))
        best.append((len(set(angles)), station))
    print(max(best))
