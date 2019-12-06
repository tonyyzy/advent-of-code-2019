if __name__ == "__main__":
    parent = {}
    with open("input.txt") as file:
        data = file.readlines()
    # data = [
    #     "COM)B",
    #     "B)C",
    #     "C)D",
    #     "D)E",
    #     "E)F",
    #     "B)G",
    #     "G)H",
    #     "D)I",
    #     "E)J",
    #     "J)K",
    #     "K)L",
    #     "K)YOU",
    #     "I)SAN"
    # ]
    for relation in data:
        a, b = relation.strip().split(")")
        parent[b] = a
    YOUpath = {}
    SANpath = {}
    node = "YOU"
    counter = 0
    node = parent[node]
    while parent[node] != "COM":
        YOUpath[node] = counter
        counter += 1
        node = parent[node]
    node = "SAN"
    counter = 0
    node = parent[node]
    while parent[node] != "COM":
        SANpath[node] = counter
        counter += 1
        node = parent[node]
    common_key = [x for x in SANpath.keys() if x in YOUpath.keys()]
    path = [YOUpath[x] + SANpath[x] for x in common_key]
    print(min(path))