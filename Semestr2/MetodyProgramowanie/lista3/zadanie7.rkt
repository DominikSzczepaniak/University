#lang racket


(define (foldr-reverse xs)
  (foldr (lambda (y ys) (append ys (list y))) null xs))

(length (foldr-reverse (build-list 10000 identity)))

;despite (length) doing dogshit every step there is created a new sublist
;(y null) for every element in xs which is added to ys
;so we have 2n elements of initial list, because in list we have
;(elem1 (elem2 (elem3 ... (elemx null))...)
; and here we have ((elem1 null) (elem2 null) ... (elemx null))
;how many conses it creates? n , where n is length of list xs
;how many of them are useless? basically all of them, they cant be reordered