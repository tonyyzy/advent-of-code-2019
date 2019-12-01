def fuel(mass):
    return (mass // 3) - 2

if __name__ == "__main__":
    with open("input.txt") as file:
        masses = file.readlines()
    masses = [int(x.strip()) for x in masses]
    print(sum(fuel(mass) for mass in masses))