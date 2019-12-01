def fuel(mass):
    return (mass // 3) - 2


def total_fuel(mass):
    total = []
    fuel_mass = fuel(mass)
    while fuel_mass > 0:
        total.append(fuel_mass)
        fuel_mass = fuel(fuel_mass)
    return sum(total)


if __name__ == "__main__":
    with open("input.txt") as file:
        masses = file.readlines()
    masses = [int(x.strip()) for x in masses]
    print(sum(total_fuel(mass) for mass in masses))