#lang racket

(define (size_list xs)
  (define (it xs answer)
    (if (null? xs)
        answer
        (it (cdr xs) (+ answer 1))))
  (it xs 0))

(define (split xs)
  (define size (size_list xs))
  (define (it xs left right k)
    (if (null? xs)
        (append (list left) right)
        (if (<= k (/ size 2))
            (it (cdr xs) (append left (list (car xs))) right (+ k 1))
            (it (cdr xs) left (append right (list (car xs))) (+ k 1)))))
  (it xs (list) (list) 1))

;if both xs and ys are empty - return answer
;if only xs is empty then add ys to answer and return it
;if only ys is empty then add xs to answer and return it
(define (merge xs ys)
  (define (it xs ys answer)
    (if (and (null? xs) (null? ys))
        answer
        (cond
          [(null? xs) (append answer ys)]
          [(null? ys) (append answer xs)]
          [else
           (if (<= (car xs) (car ys))
               (it (cdr xs) ys (append answer (list (car xs))))
               (it xs (cdr ys) (append answer (list (car ys)))))])))
            
  (it xs ys (list)))

;merge-sort gets list
;if list is longer than 1 split it for 2 new lists - list1 and list2
;if their length is 1 then (merge list1 list2)
;if not then split them again

(define (merge-sort xs)
  (if (= 1 (size_list xs))
      xs
      (merge (merge-sort (car (split xs))) (merge-sort (cdr (split xs))))))
; (list 5 4 1)
; null? no:
; (split xs):
; (list 5 4) (list 1)
; merge-sort (list 5 4)
; null? no:
; (split (list 5 4)):
; (list 5) (list 4)
; merge (list 4) (list 5) -> (list 4 5)
; merge (list 4 5) (list 1) -> (list 1 4 5)
; end.


;merge-sort is structural recurensive because its always dividing its list until its size 1, then it merges two answers

      
     
  