// mozliwe rozwiazania
// 1. in post order sortujemy wejscie pozniej gladko idzie
// 2. lca na potegach 8 O(n + q * 8 log8(n))
// 3. to co ja mam nizej
// 4. longest path decomposition
// 5. ladder decomposition (rownowazne z 4.)

use std::io::{self, BufRead};

const MAXN: usize = 1_000_005;

struct LCA {
    parent: Vec<usize>,
    poziom: Vec<usize>,
    dp: Vec<usize>,
}

impl LCA {
    fn new() -> Self {
        LCA {
            parent: vec![0; MAXN],
            poziom: vec![0; MAXN],
            dp: vec![0; MAXN],
        }
    }

    fn equal_levels(&self, mut a: usize, mut b: usize) -> usize {
        std::mem::swap(&mut a, &mut b);
        while self.poziom[b] < self.poziom[a] {
            if self.poziom[b] <= self.poziom[self.dp[a]] {
                a = self.dp[a];
            } else {
                a = self.parent[a];
            }
        }
        return a;
    }

    fn preprocess(&mut self, n: usize) {
        self.poziom[1] = 0;
        for i in 2..=n {
            self.poziom[i] = self.poziom[self.parent[i]] + 1;
            let ojciec1 = self.parent[i];
            let ojciec2 = self.dp[ojciec1];
            if self.dp[ojciec2] != 0 && self.poziom[ojciec1] - self.poziom[ojciec2] == self.poziom[ojciec2] - self.poziom[self.dp[ojciec2]] { //jesli skok ojca do dp[ojca] jest rowny odleglosci skok dp[ojca] do dp[dp[ojca]] to idziemy do dp[dp[ojca]] wpp idziemy do ojca
                self.dp[i] = self.dp[ojciec2];
            } else {
                self.dp[i] = ojciec1;
            }
        }
    }
}

fn main() {
    let stdin = io::stdin();
    let mut handle = stdin.lock();
    let mut input = String::new();
    handle.read_line(&mut input).unwrap();
    let mut iter = input.split_whitespace();
    let n: usize = iter.next().unwrap().parse().unwrap();
    let m: usize = iter.next().unwrap().parse().unwrap();

    let mut lca = LCA::new();

    for i in 2..=n {
        input.clear();
        handle.read_line(&mut input).unwrap();
        let parent_i: usize = input.trim().parse().unwrap();
        lca.parent[i] = parent_i;
    }

    lca.preprocess(n);
    // for i in 2..=n{
    //     dbg!(i, lca.dp[i]);
    // }

    for _ in 0..m {
        input.clear();
        handle.read_line(&mut input).unwrap();
        let mut iter = input.split_whitespace();
        let a: usize = iter.next().unwrap().parse().unwrap();
        let b: usize = iter.next().unwrap().parse().unwrap();
        if lca.poziom[b] < lca.poziom[a]{
            println!("NIE");
            continue;
        }
        let lca_node = lca.equal_levels(a, b);
        if lca_node != a {
            println!("NIE");
        } else {
            println!("TAK");
        }
    }
}
