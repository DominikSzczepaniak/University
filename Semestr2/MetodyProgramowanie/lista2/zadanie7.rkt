#lang racket

(define (suffixes xs)
  (define (it xs answer)
    (if (null? xs)
        answer
        (it (cdr xs) (append answer (list xs)))))
  (it xs (list (list))))