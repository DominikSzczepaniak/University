#lang racket

(define (fib n)
  (if (= n 0)
      0
      (if (= n 1)
          1
          (+ (fib (- n 1)) (fib (- n 2))))))

(define (fib.v2 n)
  (cond
    [(= n 0) 0]
    [(= n 1) 1]
    [else (+ (fib.v2 (- n 1)) (fib.v2 (- n 2)))]))


(define (fib-iter n)
  (define (it x previous1 previous2)
     (if (= x n)
         (+ previous1 previous2)
         (it (+ x 1) (+ previous1 previous2) previous1))) ;so if we are keeping
  ;2 previous numbers then answer for x is previous1+previous2
  ;but if x is not equal to n then we just proceed, hence previous1+previous2 is answer for
  ;current x in next step and previous2 is answer for x-1 = previous1
  (if (= n 0) ;special case - n is 0 then we just return 0
      0
      (it 1 0 1)))

