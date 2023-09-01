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
  (node
      (node
         (leaf)
         2
         (node
            (leaf)
            4
            (leaf)))
   3
   (leaf)))

;If the current node is leaf then return true
;If the value of the node is less than the minimum value or greater than the maximum value then return false
;Call the same function for the left and the right subtree and narrow down the minimum and maximum values
;for these calls accordingly (decrease max by 1 and increase min by 1)

(define (bst? t)
  (define (helper t minV maxV)
    (if (leaf? t)
        #t
        (if (or (< (node-elem t) minV) (> (node-elem t) maxV))
            #f
            (and (helper (node-l t) minV (- (node-elem t) 1))
                 (helper (node-r t) (+ 1 (node-elem t)) maxV)))))
  (helper t -inf.0 +inf.0))


(define (sum-paths t)
  (define (it x t)
    (node
     (if (leaf? (node-l t))
         (leaf)
         (it (+ x (node-elem (node-l t))) (node-l t)))
     x
     (if (leaf? (node-r t))
         (leaf)
         (it (+ x (node-elem (node-r t))) (node-r t)))))
  (if (leaf? t)
      (leaf)
      (it (node-elem t) t)))
          
  