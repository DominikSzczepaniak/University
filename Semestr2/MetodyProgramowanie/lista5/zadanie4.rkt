#lang plait

; chcemy wywolac n funkcji gdzie mamy liczbe na i-tym miejscu (0<=i<n)
; umieszczamy ta liczbe jako wynik (i, (f (rest xs))
; i robimy tak w niesoknczonosc
; czyli jesli mamy liste 1 2 3
; mamy (1, (funkcja '(2 3))
; z funkcji '(2 3) dostaniemy:
; (2, (funkcja '(3))
; (3, (funkcja '(2))
; z funkcja '(3) mamy (3, null)
; z funkcja '(2) mamy (2, null)
; dodajemy obie do 1
; mamy (1, (2, (3, null)
; (1, (3, (2, null))
; to samo robimy dla 2
; a pozniej 3


(define (perms2 xs)
  (local [(define (insert-perms e xs)
    (local [(define (insert pref e perm)
              (if (empty? perm)
                  (list (append pref (list e)))
                  (append (list (append pref (cons e perm)))
                          (insert
                           (append pref (list (first perm))) e (rest perm)))))]
    (if (empty? xs) empty
        (append
         (insert empty e (first xs))
         (insert-perms e (rest xs))))))]
  (if (empty? xs) (list xs)
      (let ([e (first xs)]
           [perms_rest (perms (rest xs))])
      (if (empty? perms_rest)
          (list (list e))
          (insert-perms e perms_rest))))))

(define (concat-map f xs)
  (if (empty? xs)
      '()
      (append (f (first xs))
              (concat-map f (rest xs)))))

(define (insert-all x xs)
  (if (empty? xs)
      (list (list x))
      (cons (cons x xs)
            (map (λ (ys) (cons (first xs) ys))
                 (insert-all x (rest xs))))))

(define (perms xs)
  (if (empty? xs)
      (list xs)
      (concat-map (λ (ys) (insert-all (first xs) ys))
                  (perms (rest xs)))))


