use std::io::{self, BufRead};
use std::cmp::max;

fn dfs(node: usize, dp: &mut Vec<(u32, u32)>, adj: &Vec<Vec<usize>>, visited: &mut Vec<bool>) {
    visited[node] = true;
    for &i in &adj[node] {
        if !visited[i] {
            dfs(i, dp, adj, visited);
            if 1 + dp[i].0 > dp[node].0{
                dp[node].0 = 1 + dp[i].0;
                dp[node].1 = i as u32;
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
    let mut visited = vec![false; n + 1];
    let mut adj = vec![vec![]; n + 1];
    let mut dp: Vec<(u32, u32)> = vec![(0, 0); n + 1];
    for _i in 1..=m {
        input.clear();
        handle.read_line(&mut input).unwrap();
        let mut iter = input.split_whitespace();
        let a: usize = iter.next().unwrap().parse().unwrap();
        let b: usize = iter.next().unwrap().parse().unwrap();
        adj[a].push(b);
    }

    for i in 1..=n {
        if !visited[i] {
            dfs(i, &mut dp, &adj, &mut visited);
        }
    }
    let mut ans = 0;
    let mut ktory = 0;
    for i in 1..=n {
        if dp[i].0 > ans {
            ans = dp[i].0;
            ktory = i;
        }
    }
    println!("{}", ans);
    let mut res = vec![];
    while ktory != 0 {
        res.push(ktory);
        ktory = dp[ktory].1 as usize;
    }
    res = res.into_iter().rev().collect();
    for i in (0..res.len()).rev() {
        print!("{} ", res[i]);
    }
}
