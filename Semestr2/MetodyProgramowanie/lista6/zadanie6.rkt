#lang plait

( define-type ( NNF 'v )
   ( nnf-lit [ polarity : Boolean ] [ var : 'v ])
   ( nnf-conj [ l : ( NNF 'v ) ] [ r : ( NNF 'v ) ])
   ( nnf-disj [ l : ( NNF 'v ) ] [ r : ( NNF 'v ) ]))
;zadanie 6
( define-type ( Formula 'v )
   ( var [ var : 'v ])
   ( neg [ f : ( Formula 'v ) ])
   ( conj [ l : ( Formula 'v ) ] [ r : ( Formula 'v ) ])
   ( disj [ l : ( Formula 'v ) ] [ r : ( Formula 'v ) ]) )

(define (to-nnf-postive form)
  (cond [(var? form) (nnf-lit #t (var-var form))]
        [(conj? form) (nnf-conj (to-nnf-postive (conj-l form)) (to-nnf-postive (conj-r form)))]
        [(disj? form) (nnf-disj (to-nnf-postive (disj-l form)) (to-nnf-postive (disj-r form)))]
        [(neg? form) (to-nnf-negative (neg-f form))]))

(define (to-nnf-negative form)
  (cond [(var? form) (nnf-lit #f (var-var form))]
        [(conj? form) (nnf-disj (to-nnf-negative (conj-l form)) (to-nnf-negative (conj-r form)))]
        [(disj? form) (nnf-conj (to-nnf-negative (disj-l form)) (to-nnf-negative (disj-r form)))]
        [(neg? form) (to-nnf-postive (neg-f form))]))
(define (to-nnf form)
  (to-nnf-postive form))
(define formula2 (neg(conj (var "A") (var "B"))))