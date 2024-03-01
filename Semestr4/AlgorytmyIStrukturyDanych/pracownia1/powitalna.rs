use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut handle = stdin.lock();
    let mut input = String::new();
    handle.read_line(&mut input).unwrap();
    let mut iter = input.split_whitespace();
    let mut a: i32 = iter.next().unwrap().parse().unwrap();
    let b: i32 = iter.next().unwrap().parse().unwrap();

    let reszta = a % 2024;
    let dodac = 2024 - reszta;
    a += dodac;

    while a <= b {
        print!("{} ", a);
        a += 2024;
    }
    println!();
}
