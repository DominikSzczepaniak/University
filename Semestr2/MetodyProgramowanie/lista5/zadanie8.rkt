#lang plait

(define-type Prop
  (var [v : String])
  (conj [l : Prop][r : Prop])
  (disj [l : Prop][r : Prop])
  (neg [f : Prop]))

(define (eval val p)
           (cond [(var? p) (some-v (hash-ref val (var-v p)))]
                 [(conj? p) (and (eval val (conj-l p))(eval val (conj-r p)))]
                 [(disj? p) (or (eval val (disj-l p))(eval val (disj-r p)))]
                 [(neg? p) (not (eval val (neg-f p)))]))

(define proc (neg (conj (var "a") (disj (var "b") (neg (conj (var "a") (var "c")))))))
(define val (make-hash (list (pair "a" #t)(pair "b" #f)(pair "c" #f))))
(eval val proc)