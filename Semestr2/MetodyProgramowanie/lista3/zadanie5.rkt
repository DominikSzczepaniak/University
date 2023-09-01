#lang racket

(define (negative n)
  (build-list n (lambda (x) (* -1 (+ x 1)))))

(define (reciprocals n)
  (build-list n (lambda (x) (/ 1 (+ x 1)))))

(define (evens n)
  (build-list n (lambda (x) (* 2 x))))


(define (identityM n)
  (define (it id xs)
    (if (= id 0)
        xs
        (it (- id 1) (append xs (list (build-list n (lambda (x) (if (= (- n id) x) 1 0))))))))
  (it n (list)))