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

(define (flatten t)
  (flat-append t '()))

(define (flat-append t xs)
  (cond
    ((leaf? t) xs)
    ((node? t) (flat-append (node-l t) (cons (node-elem t) (flat-append (node-r t) xs))))
    (else (error "Unknown tree node"))))

;; przykładowe użycie:
(define t (node (node
                      (node (leaf) 2 (leaf))
                      3
                      (node (leaf) 4 (leaf)))
                5
                      (node
                          (node (leaf) 6 (leaf))
                           7
                           (node (leaf) 8 (leaf)))))
(flatten t) ; => '(2 3 4 5 6 7 8)
