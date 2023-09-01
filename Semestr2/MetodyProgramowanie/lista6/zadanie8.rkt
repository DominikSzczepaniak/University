#lang plait

(define (insert x xs)
  (if (empty? xs)
      (cons x empty)
      (if (< x (first xs))
          (cons x xs)
          (cons (first xs) (insert x (rest xs))))))

(define (bound? x xs)
  (if (empty? xs)
      #t
      (<= x (first xs))))

(define (sorted? xs)
  (if (empty? xs)
      #t
      (and (sorted? (rest xs)) (bound? x (rest xs)))))


;base:
;if xs = empty then (sorted? xs) = #t
;Take any x and do (insert x xs) then list xs has only one element hence it is sorted.

;step:
;take any xs and let (sorted? xs) = #t
;take any x and show (sorted? (insert x xs)) = #t

;we have two possibilities:
;1) x < (first xs)
;then we are and doing (cons x xs)
;so we are putting x in the first element.
;we know from step assumption that (sorted? xs) = #t
;so if x < (first xs) then (bound? x (rest xs) also is fulfilled
;hence (sorted? (insert x xs)) = #t

;2) if x >= (first xs) then we are calling (cons (first xs) (insert x (rest xs))
;let (insert x (rest xs)) = ys
;(sorted? ys) = #t from inductive assumption
;we also know that (bound? (first xs) ys) = #t because (first ys) = x when (rest xs) is empty
;so ys is either empty
;then it is the analogical situation that is in base
;or ys is not empty
; and x is either < than (first ys) or >= (first ys)
; then if x < (first ys)
; we have analogical situation from 1)
; if x >= (first ys) then we call 2) again on (rest ys)
;hence (sorted? (insert x xs)) = #t

;for all posibilities (sorted? (insert x xs)) = #t hence it is fulfilled for any x and xs that is fulfilling (sorted? xs) = #t







;podstawa indukcji:
;Dla xs będącego pustą listą (sorted? xs) ≡ #t
;Weźmy dowolne x, wtedy (insert x xs) zwróci listę zawierającą x, a skoro zarówno (sorted? (rest xs)) i (bound? x (rest xs))
;będą spełnione, ponieważ zostaną wykonane dla empty, to (sorted? (insert x xs)) ≡ #t

;krok indukcyjny:
;Weźmy dowolne xs i załóżmy, że zachodzi (sorted? xs) ≡ #t
;Weźmy dowolne x i pokażmy, że zachodzi (sorted? (insert x xs)) ≡ #t

;1) jeśli x < (first xs)) zostanie wywołane (cons x xs)
;z założenia wiemy, że dla xs zachodzi (sorted? xs) ≡ #t i skoro x < (first xs) to warunek (bound? x (rest xs))
;jest spełniony, więc (sorted? (insert x xs)) ≡ #t

;2) jeśli x >= (first xs) zostanie wywołane (cons (first xs) (insert x (rest xs)))
;oznaczmy listę (insert x (rest xs)) jako ys
;wtedy lista ys spełnia sorted? z założenia indukcyjnego
;zachodzi też (bound? (first xs) ys) ≡ #t, ponieważ (first ys) jest równe x gdy (rest xs) jest listą pustą,
;przez wystąpienie sytuacji analogicznej do podstawy indukcji, lub gdy x < (first (rest xs)),
;czyli wystąpienia sytuacji analogicznej do pierwszego warunku, wtedy z założenia warunku 2 (first xs) <= x,
;lub (first ys) jest równe (first (rest xs)) w przeciwnym przypadku, a z założenia (sorted? xs) ≡ #t mamy (first xs) <= (first ys)
;a więc (sorted? (insert x xs)) ≡ #t

;Skoro dla wszystkich możliwości spełnione są , to na mocy zasady indukcji dla dowolnych list xs i elementu x
;jeśli (sorted? xs) ≡ #t to (sorted? (insert x xs)) ≡ #t.
