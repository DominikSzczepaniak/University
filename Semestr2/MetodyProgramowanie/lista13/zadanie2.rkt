#lang racket

(define (stream-filter p s)
  (cond ((stream-null? s) null)
        ((p (stream-car s))
         (stream-cons (stream-car s)
                      (stream-filter p (stream-cdr s))))
        (else (stream-filter p (stream-cdr s)))))

(define (stream-cdr s)
  (force (cdr s)))

(define (stream-car s)
  (car s))

(define (stream-null? s)
  (null? s))

(define (stream-ref s n)
  (if (= n 0)
      (stream-car s)
      (stream-ref (stream-cdr s) (- n 1))))

(define-syntax-rule (stream-cons v s)
  (cons v (delay s)))

(define (square x)
  (* x x))

(define (integers-from n)
  (stream-cons n (integers-from (+ n 1))))

(define (divides? a b)
  (= (remainder b a) 0))

(define (prime? xs ys)
  (if (divides? (stream-car xs) ys)
      #f
      (if (promise? (cdr xs))
          #t
          (prime? (stream-cdr xs) ys))))

(define nats (integers-from 3))
(define prime (stream-cons 2 (stream-filter (lambda (x) (prime? prime x)) nats)))