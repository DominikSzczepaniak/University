#lang racket

(define empty-set (lambda (x) #f))


(define (singleton a)
  (lambda (x) (equal? a x)))

(define (in a s)
  (s a))


;if x is in s and t then one of (s x) and (t x) are true  
(define (union s t)
  (lambda (x) (or (s x) (t x))))



;if x is in intersection of s and t then both of (s x) and (t x) are true
(define (intersect s t)
  (lambda (x) (and (s x) (t x))))

(in 5 (intersect (union (singleton 5) (singleton 3)) (singleton 5)))
;is 5 in intersect of {3,5} and {5}?
;yes
(in 5 (union (singleton 5) empty-set))
;is 5 in union of {5} and {}? yes