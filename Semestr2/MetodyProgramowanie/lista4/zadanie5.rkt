#lang racket

(define-struct leaf () #:transparent)
(define-struct node (l elem r) #:transparent)

(define example-tree
  (node (node (leaf) 1 (leaf))
        2
        (node (node (leaf) 3 (leaf))
              4
              (leaf))))

(define example-tree2
  (node (node (leaf) 4 (leaf))
        2
        (node (node (leaf) 3 (leaf))
              4
              (leaf))))

(define (insert-bst x t)
  (cond [(leaf? t) (node (leaf) x (leaf))]
        [(node? t)
         (cond [(< x (node-elem t))
                 (node (insert-bst x (node-l t))
                       (node-elem t)
                       (node-r t))]
                [else
                 (node (node-l t)
                       (node-elem t)
                       (insert-bst x (node-r t)))])]))

(define (flatten t)
  (flat-append t '()))

(define (flat-append t xs)
  (cond
    ((leaf? t) xs)
    ((node? t) (flat-append (node-l t) (cons (node-elem t) (flat-append (node-r t) xs))))
    (else (error "Unknown tree node"))))

(define (treesort xs)
  (define (it xs t)
    (if (null? xs)
        t
        (it (cdr xs) (insert-bst (car xs) t))))
  (flatten (it xs (leaf))))
      
