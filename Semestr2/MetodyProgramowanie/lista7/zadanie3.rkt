#lang racket

(define/contract (suffixes xs)
  (parametric->/c (A) (-> (list*of (not/c list?) '()) list?))
  (define/contract (iter ys answer)
    (parametric->/c [A] (-> (listof A) (listof A) (listof (listof A))))
    (if (null? ys)
        answer
        (iter (rest ys) (append answer (list ys)))))
  (iter xs '()))

(define/contract (suffixes_alternative xs)
  (parametric->/c (A) (-> (list*of (not/c list?) '()) list?))
  (match xs
    ['() (list null)]
    [xs (cons xs (suffixes_alternative (cdr xs)))]))

(define (suffixes2 xs)
  (define (iter ys answer)
    (if (null? ys)
        answer
        (iter (rest ys) (append answer (list ys)))))
  (iter xs '()))

;(time (suffixes (range 3000))) = cpu time: 151 real time: 162 gc time: 52
;(time (suffixes2 (range 3000))) = cpu time: 34 real time: 35 gc time: 4