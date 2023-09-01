#lang racket

(define (my-foldl f x xs)
  (define (it xs acc)
    (if (null? xs)
        acc
        (it (cdr xs) (f (car xs) acc))))
  (it xs x))


(define (product xs)
  (if (null? xs)
      null
      (my-foldl * 1 xs)))