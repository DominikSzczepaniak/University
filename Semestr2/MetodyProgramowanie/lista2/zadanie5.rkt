#lang racket

(define (elem? x xs)
  (if (null? xs)
      #f
      (if (= x (car xs))
             #t
             (elem? x (cdr xs)))))