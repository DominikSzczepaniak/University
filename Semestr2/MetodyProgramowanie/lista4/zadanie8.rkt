#lang racket

(define-struct ord (val priority) #:transparent)
(define-struct hleaf ())
(define-struct hnode (elem rank l r) #:transparent)

(define (make-node elem heap-a heap-b)
  (if (> (rank heap-a) (rank heap-b))
      (make-hnode elem heap-a heap-b)
      (make-hnode elem heap-b heap-a)))

(define (heap-merge heap-a heap-b)
  (cond ((hleaf? heap-a) heap-b)
        ((hleaf? heap-b) heap-a)
        ((< (ord-priority (hnode-elem heap-a)) (ord-priority (hnode-elem heap-b)))
         (make-hnode (hnode-elem heap-a)
                     (hnode-rank heap-a)
                     (hnode-l heap-a)
                     (heap-merge (hnode-r heap-a) heap-b)))
        (else (make-hnode (hnode-elem heap-b)
                          (hnode-rank heap-b)
                          (hnode-l heap-b)
                          (heap-merge heap-a (hnode-r heap-b))))))

(define (hord? p h)
  (or (hleaf? h)
      (<= p (ord-priority (hnode-elem h)))))

(define (rank h)
  (if (hleaf? h)
      0
      (hnode-rank h)))

(define (heap? h)
  (or (hleaf? h)
      (and (hnode? h)
           (heap? (hnode-l h))
           (heap? (hnode-r h))
           (<= (rank (hnode-r h)) (rank (hnode-l h)))
           (= (hnode-rank h) (+ 1 (hnode-rank (hnode-r h))))
           (hord? (ord-priority (hnode-elem h)) (hnode-l h))
           (hord? (ord-priority (hnode-elem h)) (hnode-r h))))))

