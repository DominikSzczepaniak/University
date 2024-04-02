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

fn merg(foo: &[(i32, i32)], p: f64) -> Triangle {
    let mut res = Triangle::new();
    let mut aux: Vec<(i32, i32)> = Vec::new();
    let size = foo.len();
    for i in 0..size {
        aux.clear();
        aux.push(foo[i]);
        let mut j = i + 1;
        while j < size && foo[j].1 as f64 <= foo[i].1 as f64 + p {
            aux.push(foo[j]);
            j += 1;
        }

        if aux.len() >= 3 {
            for k in 0..aux.len() {
                for l in 0..aux.len() {
                    for m in 0..aux.len() {
                        if k != l && k != m && l != m {
                            let s = Triangle {
                                distance: triangle_perimeter(aux[k], aux[l], aux[m]),
                                a: aux[k],
                                b: aux[l],
                                c: aux[m],
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
    if end - start < 3 {
        return Triangle::new(); 
    }

    let m = start + (end - start) / 2;
    let xm = points[m].0;

    let left_triangle = preprocess(points, start, m);
    let right_triangle = preprocess(points, m, end);

    let mut best_triangle = if left_triangle.distance < right_triangle.distance {
        left_triangle
    } else {
        right_triangle
    };

    let mut mid_triangles: Vec<(i32, i32)> = points[start..end]
        .iter()
        .filter(|&&(x, _)| (x - xm).abs() as f64 <= best_triangle.distance / 2.0)
        .cloned()
        .collect();

    mid_triangles.sort_by(|a, b| a.1.cmp(&b.1));

    let mid_triangle = merg(&mid_triangles, best_triangle.distance / 2.0);
    if mid_triangle.distance < best_triangle.distance {
        best_triangle = mid_triangle;
    }

    best_triangle
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
