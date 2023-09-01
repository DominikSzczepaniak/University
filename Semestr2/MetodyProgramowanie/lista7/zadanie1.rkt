#lang plait

(define-type (Tree23 'a)
  (leaf)
  (node2 (l : (Tree23 'a)) (elem : 'a) (r : (Tree23 'a)))
  (node3 (l : (Tree23 'a)) (elem1 : 'a) (m : (Tree23 'a)) (elem2 : 'a) (r : (Tree23 'a))))

(define (check-height t h)
  (cond
    [(node2? t) (if (= (check-height (node2-l t) (+ 1 h)) (check-height (node2-r t) (+ 1 h)))
                    (check-height (node2-l t) (+ 1 h))
                    +inf.0)]
    [(node3? t) (if (and (= (check-height (node3-l t) (+ 1 h)) (check-height (node3-m t) (+ 1 h))) (= (check-height (node3-m t) (+ 1 h)) (check-height (node3-r t) (+ 1 h))))
                    (check-height (node3-m t) (+ 1 h))
                    +inf.0)]
    [(leaf? t) h]))
                
(define (check-values t)
  (cond
    [(node3? t) (and (<= (node3-elem2 t) (find-min (node3-m t))) (>= (node3-elem1 t) (find-max (node3-m t))))]
    [(node2? t) (and (< (node2-elem t) (find-min (node2-r t))) (> (node2-elem t) (find-max (node2-l t))))]
    [(leaf? t) #t]))

(define (find-max t)
 (cond
      [(node2? t) (max (find-max (node2-l t)) (max (find-max (node2-r t)) (node2-elem t)))]
      [(node3? t) (max (find-max (node3-l t)) (max (find-max (node3-m t)) (max (find-max (node3-r t)) (max (node3-elem1 t) (node3-elem2 t)))))]
      [(leaf? t) -inf.0]))

(define (find-min t)
  (cond
      [(node2? t) (min (find-min (node2-l t)) (min (find-min (node2-r t)) (node2-elem t)))]
      [(node3? t) (min (find-min (node3-l t)) (min (find-min (node3-m t)) (min (find-min (node3-r t)) (min (node3-elem1 t) (node3-elem2 t)))))]
      [(leaf? t) +inf.0]))

(define (tree23? t)
  (if (and (not (= (check-height t 1) +inf.0)) (check-values t))
      #t
      #f))


(define test (node2 (node3 (leaf) 1 (leaf) 2 (leaf)) 3 (node2 (leaf) 7 (leaf))))
(define test2 (node2 (leaf) 3 (node2 (node2 (node2 (leaf) 4 (leaf)) 5 (leaf)) 7 (leaf))))