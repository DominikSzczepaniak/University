#lang plait

(define-type Prop
  (var [v : String])
  (conj [l : Prop] [r : Prop])
  (disj [l : Prop] [r : Prop])
  (neg [f : Prop]))

(define (remove-duplicates lst)
  (foldr (lambda (x y) (cons x (filter (lambda (z) (not (string=? x z))) y))) empty lst))

(define (accumulate-vars t)
  (cond
    [(var? t) (cons (var-v t) empty)]
    [(neg? t) (accumulate-vars (neg-f t))]
    [(conj? t) (append (accumulate-vars (conj-l t)) (accumulate-vars (conj-r t)))]
    [(disj? t) (append (accumulate-vars (disj-l t)) (accumulate-vars (disj-r t)))]))

(define (free-vars t)
  (remove-duplicates (accumulate-vars t)))
