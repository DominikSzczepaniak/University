#lang racket
;https://rosettacode.org/wiki/Hamming_numbers
(define-syntax-rule
  (stream-cons v s)
  (cons v (delay s)))

(define stream-car car)

(define (stream-cdr s)
  (force (cdr s)))

(define stream-null null)
(define stream-null? null?)

(define (map2 f xs ys)
  (stream-cons
   (f (stream-car xs)
      (stream-car ys))
   (map2 f (stream-cdr xs) (stream-cdr ys))))


(define (merge s1 s2)
  (cond ((stream-null? s1) s2)
        ((stream-null? s2) s1)
        ((< (stream-car s1) (stream-car s2))
         (stream-cons (stream-car s1)
                      (merge (stream-cdr s1) s2)))
        ((> (stream-car s1) (stream-car s2))
         (stream-cons (stream-car s2)
                      (merge s1 (stream-cdr s2))))
        (else
         (stream-cons (stream-car s1)
                      (merge (stream-cdr s1) (stream-cdr s2))))))

(define (scale-stream n s)
  (stream-cons (* n (stream-car s))
               (scale-stream n (stream-cdr s))))

(define hamming
  (stream-cons 1
               (merge (merge (scale-stream 2 hamming)
                            (scale-stream 3 hamming))
                      (scale-stream 5 hamming))))

(displayln (stream-car hamming))
(displayln (stream-car (stream-cdr hamming)))
(displayln (stream-car (stream-cdr (stream-cdr (stream-cdr hamming)))))
(displayln (stream-car (stream-cdr (stream-cdr (stream-cdr (stream-cdr hamming))))))
(displayln (stream-car (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr hamming)))))))
(displayln (stream-car (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr hamming))))))))
(displayln (stream-car (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr hamming)))))))))
(displayln (stream-car (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr hamming))))))))))
(displayln (stream-car (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr hamming)))))))))))
(displayln (stream-car (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr hamming))))))))))))
(displayln (stream-car (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr hamming)))))))))))))
(displayln (stream-car (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr hamming))))))))))))))
(displayln (stream-car (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr hamming)))))))))))))))
(displayln (stream-car (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr hamming))))))))))))))))


