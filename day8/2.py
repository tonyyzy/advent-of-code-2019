if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip()
    height = 6
    width = 25
    layers = []
    total_length = len(data)
    layer_length = width * height
    no_layers = int(total_length / layer_length)
    position = 0
    for layer in range(no_layers):
        image = []
        for row in range(height):
            image.append(list(data[position:position + width]))
            position += width
        layers.append(image)

    message = []
    for row in range(height):
        message.append([])
        for column in range(width):
            points = []
            for layer in layers:
                points.append(layer[row][column])
            message[row].append([x for x in points if x != "2"][0])
    for row in message:
        print(" ".join(row))
            