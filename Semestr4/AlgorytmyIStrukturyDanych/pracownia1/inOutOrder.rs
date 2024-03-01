use std::collections::LinkedList;
use std::io::{self, BufRead};

const MAXN: usize = 1_000_005;

fn main() {
    let stdin = io::stdin();
    let mut handle = stdin.lock();
    let mut input = String::new();
    handle.read_line(&mut input).unwrap();
    let mut iter = input.split_whitespace();
    let n: usize = iter.next().unwrap().parse().unwrap();
    let m: usize = iter.next().unwrap().parse().unwrap();

    let mut inOrder: Vec<usize> = vec![0; MAXN];
    let mut outOrder: Vec<usize> = vec![0; MAXN];

    let mut edges: Vec<(usize, usize)> = vec![(0, 0); n + 1];

    for i in 2..=n {
        input.clear();
        handle.read_line(&mut input).unwrap();
        let a = input.trim().parse().unwrap();
        edges[i] = (a, i);
    }

    //sort edges by first element then by second
    edges.sort_by(|a, b| a.0.cmp(&b.0).then(a.1.cmp(&b.1)));
    let mut licznik = 1;
    inOrder[edges[0].0] = licznik;
    licznik += 1;
    for i in 0..n {
        let a = edges[i].0;
        let b = edges[i].1;
        inOrder[b] = licznik;
        if (i != 0 && edges[i - 1].0 != a) {
            outOrder[a] = licznik;
        }
        licznik += 1;
    }

    for _ in 0..m {
        input.clear();
        handle.read_line(&mut input).unwrap();
        let mut iter = input.split_whitespace();
        let a: usize = iter.next().unwrap().parse().unwrap();
        let b: usize = iter.next().unwrap().parse().unwrap();
        if (inOrder[a] < inOrder[b] && outOrder[a] > outOrder[b]) {
            println!("TAK");
        } else {
            println!("NIE");
        }
    }
}
