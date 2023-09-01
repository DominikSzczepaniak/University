#lang racket

(define (min_element xs)
  (define (it xs nowMIN)
    (if (null? xs)
        nowMIN
        (it (cdr xs) (min nowMIN (car xs)))))
  (it xs +inf.0))

(define (select xs)
  (define minEL (min_element xs))
  (define (it xs ys)
    (if (null? xs)
        ys
        (if (= (car xs) minEL)
            (it (cdr xs) (append (list (car xs)) ys))
            (it (cdr xs) (append ys (list (car xs)))))))
  (it xs (list)))

(define (select-sort xs)
  (define (it xs ys)
    (if (null? xs)
        ys
        (it (cdr (select xs)) (append ys (list (car (select xs)))))))
  (it xs (list)))
    
  