use std::fs;

fn fuel(mass: i32) -> i32 {
    mass / 3 - 2
}

fn total_fuel(mass: i32) -> i32 {
    let mut total = 0;
    let mut fuel_mass = fuel(mass);
    while fuel_mass > 0 {
        total += fuel_mass;
        fuel_mass = fuel(fuel_mass);
    };
    total
}

fn main() {
    let data = fs::read_to_string("input.txt")
        .expect("Something went wrong reading the file");
    let mut fuel_sum = 0;
    for mass in data.lines() {
        fuel_sum += total_fuel(mass.parse().unwrap());
    };
    print!("total fuel is {} \n", fuel_sum);
}