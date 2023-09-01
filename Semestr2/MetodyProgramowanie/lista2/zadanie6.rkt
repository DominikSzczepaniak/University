#lang racket

(define (maximum xs)
  (define (it xs nowMax)
    (if (null? xs)
        nowMax
        (it (cdr xs) (max nowMax (car xs)))))
  (it xs -inf.0))
    