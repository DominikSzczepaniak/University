use std::f64;
use std::io::{self, BufRead};

#[derive(Debug, Clone, Copy)]
struct Triangle {
    distance: f64,
    a: (i32, i32),
    b: (i32, i32),
    c: (i32, i32),
}

impl Triangle {
    fn new() -> Self {
        Triangle {
            distance: f64::INFINITY,
            a: (0, 0),
            b: (0, 0),
            c: (0, 0),
        }
    }
}

fn dist(a: (i32, i32), b: (i32, i32)) -> f64 {
    (((a.0 as i64 - b.0 as i64)*(a.0 as i64 - b.0 as i64) + (a.1 as i64 - b.1 as i64)*(a.1 as i64 - b.1 as i64)) as f64).sqrt()
}

fn triangle_perimeter(a: (i32, i32), b: (i32, i32), c: (i32, i32)) -> f64 {
    dist(a, b) + dist(a, c) + dist(c, b)
}

fn merg(triangles: &[(i32, i32)], p: f64) -> Triangle {
    let mut res = Triangle::new();
    let mut poss: Vec<(i32, i32)> = Vec::new();
    let size = triangles.len();
    for i in 0..size {
        poss.clear();
        poss.push(triangles[i]);
        let mut j = i + 1;
        while j < size && triangles[j].1 as f64 <= triangles[i].1 as f64 + p {
            poss.push(triangles[j]);
            j += 1;
        }

        if poss.len() >= 3 {
            for k in 0..poss.len() {
                for l in 0..poss.len() {
                    for m in 0..poss.len() {
                        if k != l && k != m && l != m {
                            let s = Triangle {
                                distance: triangle_perimeter(poss[k], poss[l], poss[m]),
                                a: poss[k],
                                b: poss[l],
                                c: poss[m],
                            };
                            if res.distance >= s.distance{
                                res = s;
                            }
                        }
                    }
                }
            }
        }
    }
    res
}

fn preprocess(points: &[(i32, i32)], start: usize, end: usize) -> Triangle {
    let mut low = Triangle::new();
    if end - start < 3 {
        low.distance = f64::INFINITY;
    } else {
        let m = start + (end-start) / 2;
        let xm = (points[m].0 + points[m + 1].0) / 2;
        let l = preprocess(points, start, m);
        let r = preprocess(points, m, end);
        if l.distance < r.distance {
            low = l;
        } else {
            low = r;
        }
        let p = low.distance / 2.0;
        let mut possible_triangles: Vec<(i32, i32)> = Vec::new();
        let mut mid = m as isize;
        while mid >= start as isize && points[mid as usize].0 >= (xm as f64 - p) as i32 {
            possible_triangles.push(points[mid as usize]);
            mid -= 1;
        }

        mid = (m + 1) as isize;
        while mid < points.len() as isize && mid < end as isize && points[mid as usize].0 <= (xm as f64 + p) as i32 {
            possible_triangles.push(points[mid as usize]);
            mid += 1;
        }
        possible_triangles.sort_by(|a, b| a.1.cmp(&b.1));

        let oblicz = merg(&possible_triangles, p);
        if low.distance >= oblicz.distance{
            low = oblicz;
        }
    }
    low
}

fn main() {
    let stdin = io::stdin();
    let mut points: Vec<(i32, i32)> = Vec::new();
    let mut buffer = String::new();
    stdin.lock().read_line(&mut buffer).unwrap();
    let n: usize = buffer.trim().parse().unwrap();
    for _ in 0..n {
        buffer.clear();
        stdin.lock().read_line(&mut buffer).unwrap();
        let mut iter = buffer.split_whitespace().map(|x| x.parse::<i32>().unwrap());
        let a = iter.next().unwrap();
        let b = iter.next().unwrap();
        points.push((a, b));
    }
    points.sort();
    let s = preprocess(&points, 0, n);
    let mut triangle: Vec<(i32, i32)> = Vec::new();
    triangle.push(s.a);
    triangle.push(s.b);
    triangle.push(s.c);
    triangle.sort();
    for point in triangle {
        println!("{} {}", point.0, point.1);
    }
}
