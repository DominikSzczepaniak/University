#lang racket
(require rackunit)
(define-struct matrix (a b c d) #:transparent)

; a b
; c d

(define (matrix-mult m n)
  (define nowe-a (+ (* (matrix-a m) (matrix-a n)) (* (matrix-b m) (matrix-c n))))
  (define nowe-b (+ (* (matrix-a m) (matrix-b n)) (* (matrix-b m) (matrix-d n))))
  (define nowe-c (+ (* (matrix-c m) (matrix-a n)) (* (matrix-d m) (matrix-c n))))
  (define nowe-d (+ (* (matrix-c m) (matrix-b n)) (* (matrix-d m) (matrix-d n))))
  (matrix nowe-a nowe-b nowe-c nowe-d))

(define matrix-id (matrix 1 0 0 1))

(define (matrix-expt m k)
  (define (it mac n)
    (if (= n 0)
        mac
        (it (matrix-mult mac m) (- n 1))))
  (it m (- k 1))) ;why k-1? because if not then m ^ 1 = m*m, which is false

(define (fib-matrix k)
  (matrix-b (matrix-expt (matrix 1 1 1 0) k)))

(check-equal? (matrix-mult (matrix 1 2 3 4) (matrix 7 8 9 7)) (matrix 25 22 57 52))
(check-equal? (matrix-expt (matrix 5 6 7 8) 3) (matrix 881 1026 1197 1394))
(check-equal? (fib-matrix 12) 144)
(check-equal? (fib-matrix 15) 610)

