use std::fs;

fn fuel(mass: i32) -> i32 {
    mass / 3 - 2
}

fn main() {
    let data = fs::read_to_string("input.txt")
        .expect("Something went wrong reading the file");
    let mut total_fuel = 0;
    for mass in data.lines() {
        total_fuel += fuel(mass.parse().unwrap());
    };
    print!("total_fuel is {}", total_fuel);
}