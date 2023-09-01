#lang racket

((lambda (x y) (+ x (* x y))) 1 2)
;->
;x=1, y=2
;(+ 1 (* 1 2))


;podpunkt 2
;((lambda (x) x) (lambda (x) x))
;function that calls itself once


;podpunkt 3
;((lambda (x) (x x)) (lambda (x) x))
;we call (we get function that calls herself two times

;->
;x = lambda(x) x
;(lambda (lambda (x) x) (x x))
;returns (x x)




;podpunkt 4
;((lambda (x) (x x)) (lambda (x) (x x)))
;function that callherself two times, but if she call herself two times
;then those two calls, call herself another two times, so we have 2^n calls
;->
;(x -> x . x) . (x -> x . x)
;lets call lambda (x) (x x) itself
;itself > itself
;itself > (x -> x > x)
;itself > (_____        >     _____)
;         (x -> x > x)     (x -> x > x)
;and in () we again have
;itself > (itself > itself)
;and goes on in infinite loop