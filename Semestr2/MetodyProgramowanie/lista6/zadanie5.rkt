#lang plait

(define-type (NNF 'v)
  (nnf-lit [polarity : Boolean] [var : 'v])
  (nnf-conj [l : (NNF 'v)] [r : (NNF 'v)])
  (nnf-disj [l : (NNF 'v)] [r : (NNF 'v)]))

(define (eval-nnf [f : 'a->Boolean] [N : (NNF 'a)])
  (cond [(nnf-lit? N)
         (if (nnf-lit-polarity N)
             (f (nnf-lit-var N))
             (not (f (nnf-lit-var N))))]
        [(nnf-conj? N)
         (and (eval-nnf f (nnf-conj-l N))
              (eval-nnf f (nnf-conj-r N)))]
        [else
         (or (eval-nnf f (nnf-disj-l N))
              (eval-nnf f (nnf-disj-r N)))]))


; Niech P(φ) = ∀σ (eval-nnf σ (neg-nnf φ)) ≡ (not (eval-nnf σ φ)).
; Chcemy pokazać, że P(φ) zachodzi dla dowolnego φ.

; 1) Weźmy dowolne p, v. Pokażemy, że P(nnf-lit p v).
;    Weżmy dowolne wartościowanie σ. Wtedy :

;    L = (eval-nnf σ (neg-nnf (nnf-lit p v))) =
;      = [z def. neg-nnf]
;        (eval-nnf σ (nnf-lit (not p) v)) =
;      = [z def. eval-nnf]
;        (σ v) <- gdy p=#f
;        lub
;        (not (σ v)) <- gdy p=#t

;    P = (not (eval-nnf σ (nnf-lit p v))) =
;      = [z def. eval-nnf]
;        (not (σ v)) <- gdy p=#t
;        lub
;        (not (not (σ v))) = (σ v) <- gdy p=#f

;    Zatem L=P, czyli P(nnf-lit p v) dla dowolnych p, v.

; 2) Weźmy dowolne φ1, φ2 i załóżmy, że P(φ1) oraz P(φ2).
;    Pokażemy, że P(nnf-conj φ1 φ2).
;    Weżmy dowolne wartościowanie σ. Wtedy :

;    L = (eval-nnf σ (neg-nnf (nnf-conj φ1 φ2))) =
;      = [z def. neg-nnf]
;        (eval-nnf σ (nnf-disj (neg-nnf φ1) (neg-nnf φ1)) =
;      = [z def. eval-nnf]
;        (or (eval-nnf σ (neg-nnf φ1))
;            (eval-nnf σ (neg-nnf φ2))) =
;      = [z zał. indukcyjnego]
;        (or (not (eval-nnf σ φ1))
;            (not (eval-nnf σ φ2)))

;    P = (not (eval-nnf σ (nnf-conj φ1 φ2))) =
;      = [z def. eval-nnf]
;        (not (and (eval-nnf σ φ1)
;                  (eval-nnf σ φ2))) =
;      = [z def. not]
;        (or (not (eval-nnf σ φ1))
;            (not (eval-nnf σ φ2)))

;    Zatem L=P, czyli P(nnf-conj φ1 φ2) dla dowolnych φ1, φ2.

; 3) Analogicznie dla P(nnf-disj φ1 φ2) dla dowolnych φ1, φ2.

; Na mocy zasady indukcji P(φ) zachodzi dla każdego φ typu (NNF 'v).



