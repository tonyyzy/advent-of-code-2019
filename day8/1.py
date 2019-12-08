if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip()
    layers = []
    total_length = len(data)
    layer_length = 25 * 6
    no_layers = int(total_length / layer_length)
    position = 0
    for layer in range(no_layers):
        image = []
        for row in range(6):
            image.append(list(data[position:position + 25]))
            position += 25
        layers.append(image)
    no_zeros = []
    for layer in layers:
        no_zeros.append([y for x in layer for y in x].count('0'))
    loc = no_zeros.index(min(no_zeros))
    print([y for x in layers[loc] for y in x].count('1') * [y for x in layers[loc] for y in x].count('2'))
            