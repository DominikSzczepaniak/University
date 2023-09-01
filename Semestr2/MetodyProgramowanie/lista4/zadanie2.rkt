#lang racket

(define-struct leaf () #:transparent)
(define-struct node (l elem r) #:transparent)

(define (fold-tree f x t)
    (cond [(leaf? t) x]
          [(node? t)
           (f
            (fold-tree f x (node-l t))
            (node-elem t)
            (fold-tree f x (node-r t)))]))

(define example-tree
  (node (node (leaf) 1 (leaf))
        2
        (node (node (leaf) 3 (leaf))
              4
              (leaf))))

(define (tree-sum t)
  (fold-tree (lambda (x y z) (+ x y z)) 0 t))

(define (tree-flip t)
  (fold-tree (lambda (x y z) (make-node (tree-flip z) y (tree-flip x))) (leaf) t))

(define (tree-height t)
  (fold-tree (lambda (x y z) (+ 1 (max x z))) 0 t))

(define (tree-span t)
  (define maxV (fold-tree (lambda (x y z) (max x y z)) 0 t))
  (define minV (fold-tree (lambda (x y z) (min x y z)) +inf.0 t))
  (cons minV maxV))

(define (flatten t)
  (fold-tree (lambda (x y z) (cons x (cons y (cons z null)))) null t))



      
  






  