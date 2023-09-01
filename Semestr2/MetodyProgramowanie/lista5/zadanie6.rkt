#lang plait

(define-type (RoseTree 'a)
  (leaf2 [elem : 'a])
  (node2 [child : (Listof (RoseTree 'a))] ))


(define test
  (node2 (list (leaf2 3) (leaf2 4) (node2 (list (leaf2 5) (leaf2 6))) (node2 (list)))))

(define (InOrderRoseTreev2 tree xs)
  (cond [(leaf2? tree) (cons (leaf2-elem tree) xs)]
        [(node2? tree)(foldr (λ (t xs) (InOrderRoseTreev2 t xs)) xs (node2-child tree))]))
