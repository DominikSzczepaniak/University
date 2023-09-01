#lang plait

(define (zad1 x y) 
  x)

(define (zad2 x y z)
  (x z(y z)))

(define (id x) x)

(define (zad3 [x : (('a -> 'a) -> 'a)]) (x id))

(define (zad4 a b)
  (lambda (x) (pair (a x) (b x))))

(define (zad5 [y : ('a -> (Optionof ('a * 'b)))] x) 
  (let ([elem (y x)])
    (if (none? elem)
        empty
        (cons (snd(some-v elem)) empty))))

