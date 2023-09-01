#lang racket
(define y 6)
(define x 2)
(define z 1)
(let ([x 3]) (+ x y)) ;wolne - y, zwiazane - x
(let ([x 1] [y (+ x 2)]) (+ x y)) ;wolne - (+ x 2) zwiazane - x i y
(let ([x 1]) (let ([y (+ x 2)]) (* x y))) ;wolne - brak zwiazane - x i y
;(define (f x y) ;zwiazane x i y wolne z
 ; (* x y z))

(define (f x)
  (define (g y z) 
    (* x y z)) ;tu y i z sa zwiazane do funkcji g
  (f x x x)) ;to nie ma w ogole sensu, error

