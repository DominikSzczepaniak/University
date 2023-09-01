#lang plait

(define-type (NNF 'v)
  (nnf-lit [polarity : Boolean] [var : 'v])
  (nnf-conj [l : (NNF 'v)] [r : (NNF 'v)])
  (nnf-disj [l : (NNF 'v)] [r : (NNF 'v)]))

(define (neg-nnf form)
  (cond
    [(nnf-lit? form) (nnf-lit (not (nnf-lit-polarity form)) (nnf-lit-var form))]
    [(nnf-conj? form) (nnf-disj (neg-nnf (nnf-conj-l form)) (neg-nnf (nnf-conj-r form)))]
    [(nnf-disj? form) (nnf-conj (neg-nnf (nnf-disj-l form)) (neg-nnf (nnf-disj-r form)))]))

(define formula (nnf-lit #f 1))
(define formula2 (nnf-conj (nnf-disj (nnf-lit #t 1) (nnf-lit #f 2)) (nnf-lit #t 3)))

; let A be any formula in Y
; we want to prove that (neg-nnf (neg-nnf A)) == A

; if A is conj:
; A = C v D where C and D are literals
; (neg-nnf A) = ~C ^ ~D
; (neg-nnf ~C ^ ~D) = C v D = A
; so (neg-nnf (neg-nnf A)) = C v D = A
; if A is disj:
; A = C ^ D where C and D are literals
; (neg-nnf A) = ~C v ~D
; (neg-nnf ~C v ~D) = C ^ D = A
; so (neg-nnf (neg-nnf A)) = C ^ D = A
; if A is literal:
; (neg-nnf A) = ~A
; (neg-nnf ~A) = A
; (neg-nnf (neg-nnf A)) = A
; so if A is disj A = C^D and C and D are not literals, then inductive C and D
; are either disj or conj, which can split for conj or disj or literals, but inductive they are
; equal
