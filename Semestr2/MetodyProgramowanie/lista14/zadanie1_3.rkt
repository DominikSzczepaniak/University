#lang plait
(define-type-alias (M 'a) 'a)
(define (returnM [v : 'a]) : (M 'a)
  v)

(define (bindM [c : (M 'a)] [f : ('a -> (M 'b))]) : (M 'b)
  (f c))

;we want to proof that
;1. (bindM (returnM a) f) = (f a)
; let a be anything
; then (returnM a) from definition returns us a
; (bindM a f) from definition is (f a)
; so they are equal, so its true

;2. (bindM c returnM) = c
; (bindM c returnM) from definition is equal to (returnM c)
; and (returnM c) is equal to c from definition
; so its true

;3. (bindM (bindM c f) g) = (bindM c (λ (a) (bindM (f a) g)))
; (bindM c f) is (f c) from def
; then we got
; (bindM (f c) g) which from definition is
; (g (f c))

; now for right part
; (bindM (f a) g) = (g (f a))
; so we have (bindM c (λ (a) (g (f a)))
; and this from definition is
; ((λ (a) (g (f a))) c)
; and this is (a = c)
; (g (f c))
; which is equal to left part, hence this is true aswell