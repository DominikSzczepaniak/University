#lang racket

(define/contract (my-foldr-err f x xs)
  (parametric->/c [a] (-> (-> a a a) a (listof a) a))
  (if (empty? xs)
      x
      (f x (my-foldr-err f (first xs) (rest xs)))))

(define/contract (my-foldr-err2 f x xs)
  (parametric->/c [a b] (-> (-> a b b) b (listof a) b))
  (if (empty? xs)
      x
      (f x (my-foldr-err2 f (first xs) (rest xs)))))

(define (sum xs)
  (my-foldr-err2 + 0 xs))
(sum '(1 2 3))

;does changed contract limits use of foldr? no
;changed type? yes IT HAS TO BE TYPE A, SO CANT BE (foldr cons '1 '(1 2 3)) because '1 != 1


      