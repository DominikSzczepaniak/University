#lang racket

(define-struct leaf () #:transparent)
(define-struct node (l elem r) #:transparent)

(define (insert-bst x t)
  (cond [(leaf? t) (node (leaf) x (leaf))]
        [(node? t)
         (cond [(= x (node-elem t)) t]
                [(< x (node-elem t))
                 (node (insert-bst x (node-l t))
                       (node-elem t)
                       (node-r t))]
                [else
                 (node (node-l t)
                       (node-elem t)
                       (insert-bst x (node-r t)))])]))

(define example-tree
  (node (node (leaf) 1 (leaf))
        2
        (node (node (leaf) 5 (node (leaf) 6 (leaf)))
              7
              (leaf))))

(define (bst-delete node value)
  (cond
    [(leaf? node) #f] ; wartość nie została znaleziona
    [(< value (node-elem node))
     (make-node (bst-delete (node-l node) value)
                (node-elem node)
                (node-r node))]
    [(> value (node-elem node))
     (make-node (node-l node)
                (node-elem node)
                (bst-delete (node-r node) value))]
    [else ; wartość została znaleziona
     (cond
       [(leaf? (node-l node)) (node-r node)]
       [(leaf? (node-r node)) (node-l node)]
       [else
        (let* ([next-node (tree-min (node-r node))]
               [new-value (node-elem next-node)]
               [new-right (bst-delete (node-r node) new-value)])
          (make-node (node-l node)
                     new-value
                     new-right))])]))

(define (tree-min node)
  (cond
    [(leaf? node) node]
    [(leaf? (node-l node)) node]
    [else (tree-min (node-l node))]))


  