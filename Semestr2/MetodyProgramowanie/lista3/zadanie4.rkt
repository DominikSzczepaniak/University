#lang racket

(define (square x)
  (* x x))

(define (inc x)
  (+ x 1))

(define (my-compose f g)
  (lambda (x)
    (f (g x))))