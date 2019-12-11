use std::fs;

#[derive(Debug)]
struct Coord(i32, i32);

// fn transform(coord: &[Coord], station: Coord) {
//     let mut new_coord: [Coord; coord.len()];
// }



fn main() {
    let data = fs::read_to_string("test.txt")
            .expect("Something went wrong reading the file");
    let mut coord = Vec::new();
    for (i, dat) in data.lines().enumerate() {
        for (j, symb) in dat.chars().enumerate() {
            coord.push(Coord(j as i32, i as i32))
        }
    };
    let a = Coord(1, 2);
    print!("{:?}", a);
    print!("{:?}", coord)
    
}