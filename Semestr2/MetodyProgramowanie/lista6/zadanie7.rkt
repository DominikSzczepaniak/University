#lang plait
;zadanie 7
( define-type ( Formula 'v )
   ( var [ var : 'v ])
   ( neg [ f : ( Formula 'v ) ])
   ( conj [ l : ( Formula 'v ) ] [ r : ( Formula 'v ) ])
   ( disj [ l : ( Formula 'v ) ] [ r : ( Formula 'v ) ]) )

(define (positive-eval interpretation form)
  (cond [(var? form) (interpretation (var-var form))]
        [(conj? form)
         (and (positive-eval interpretation (conj-l form))
              (positive-eval interpretation (conj-r form)))]
        [(disj? form)
         (or (positive-eval interpretation (disj-l form))
              (positive-eval interpretation (disj-r form)))]
        [(neg? form) (not(positive-eval interpretation (neg-f form)))]))

(define (eval interpretation form)
  (positive-eval interpretation form))
#|
Zasada indukcji strukturalnej dla FORMUŁ:
Niech P będzie taką własnością typu FORMUŁ, że
i) P(var)
ii) Dla każdego l i r (typu Formula)
Jeśli P(l) i P(r) to P(conj(l r)) oraz P(disj(l r))
iii) Dla każdego l (typu Formula) jeśli P(l) to P(neg(l)) też

Dowód: (eval-nnf Sigma (to-nnf fi)) ≡ (eval-formula Sigma fi)
-> Dowód: (eval-nnf Sigma (to-nnf-postive fi)) ≡ (eval-formula Sigma fi) oraz (eval-nnf Sigma (to-nnf-negative fi)) ≡ (eval-formula Sigma (neg fi))
Niech P będzie dowolną formułą:
i) Jeśli P ≡ var:
I. (eval-nnf Sigma (to-nnf-postive var)) ≡ (eval-nnf Sigma var) ≡ (eval-formula Sigma var)
II. (eval-nnf Sigma (to-nnf-negative var)) ≡ (not (eval-nnf Sigma var)) ≡  (eval-formula Sigma (neg fi))
ii i iii) Weźmy dowolne l i r takie że l i r należą do formuł i załużmy że
(eval-nnf Sigma (to-nnf-postive l)) ≡ (eval-formula Sigma l) oraz (eval-nnf Sigma (to-nnf-negative l)) ≡ (eval-formula Sigma (neg l))
i analogicznie dla r.
I. Pokażmy że (conj l r) spełnia również ten warunek
(eval-nnf Sigma (to-nnf-postive (conj l r))) ≡ (and (eval-nnf Sigma (to-nnf-postive l)) (eval-nnf Sigma (to-nnf-postive r))) ≡
≡ (and (eval-formula Sigma l) (eval-formula Sigma r)) ≡ (eval-formula Sigma (conj l r))
(eval-nnf Sigma (to-nnf-negative (conj l r))) ≡ (or (eval-nnf Sigma (to-nnf-negative l)) (eval-nnf Sigma (to-nnf-negative r)))
≡ (or (eval-formula Sigma (neg l)) (eval-formula Sigma (neg r))) ≡ (eval-formula Sigma (neg (conj l r)))
II.disj analogicznie jak I.
III. (eval-nnf Sigma (to-nnf-postive (neg l))) ≡ (eval-formula Sigma (neg l))
(eval-nnf Sigma (to-nnf-postive (neg l))) ≡ (eval-nnf Sigma (to-nnf-negative l)) ≡ z zalozenia ≡ (eval-formula Sigma (neg l))

Na mocy zasady indukcji zachodzi to dla każdej Formuły.
|#
