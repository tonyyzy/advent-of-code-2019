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
    # ]
    for relation in data:
        a, b = relation.strip().split(")")
        parent[b] = a
    orbit = []
    for node in parent.keys():
        key = node
        orbit.append("->".join([node, parent[key]]))
        while parent[key] != "COM":
            key = parent[key]
            orbit.append("->".join([node, parent[key]]))
    print(len(set(orbit)))
    # print([x for x in direct.values() if x not in direct.keys()])