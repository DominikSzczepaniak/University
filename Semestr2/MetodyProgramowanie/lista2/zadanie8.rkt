#lang racket

(define (sorted? xs)
  (define (it xs nowMAX) ;lista nie jest posortowana niemalejaco jezeli przed dowolnym elementem wystapil
    ;kiedykolwiek wczesniej element > od niego
    (if (null? xs)
        #t
        (if (> nowMAX (car xs))
            #f
            (it (cdr xs) (max nowMAX (car xs))))))
  (it xs -inf.0))
    