#lang racket

(require compatibility/mlist)

(define (cycle! xs)
  (define (iter ys)
    (if (null? (mcdr ys))
        (set-mcdr! ys xs)
        (iter (mcdr ys))))
  (iter xs))

    
      