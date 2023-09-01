#lang racket
;wystapienie pozytywne - drugie a
;wystapienie negatywne pierwsze a i pierwsze b

(define/contract (func1 x y)
  (parametric->/c [a b] (-> a b a))
  x)

;pozytywne - pierwsze i drugie a, pierwsze b, ostatnie c
;negatywne - pierwsze c, drugie b, trzecie c
(define/contract (func2 f g x)
  (parametric->/c [a b c] (-> (-> a b c) (-> a b) a c))
  (f x (g x)))
;positiv - first b, first a, last a and last c
;negative - first c, second b
(define/contract (func3 f g h)
  (parametric->/c [a b c] (-> (-> b c) (-> a b) (-> a c)))
  (lambda (x) (f (g x))))

;negatywne - pierwsze a
;pozytywne - drugie a, trzecie a, ostatnie a
(define/contract (func4 x)
  (parametric->/c [a] (-> (-> (-> a a) a) a))
  (identity (x (lambda (y) y))))
  