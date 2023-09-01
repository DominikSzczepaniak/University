#lang plait

(define (apply f x) (f x))
;na wejsciu dostajemy funkcje jednoargumentowa f i jej argument
;zwracamy f x
;wiec wejscie ('a -> 'b)
;wyjscie 'a -> 'b
;czyli (('a -> 'b) 'a -> b)

(define (compose f g) (lambda (x) (f (g x))))
;na wejsciu mamy dwie funkcje - f i g
; g przyjmuje jeden argument i zwraca cos
;f przyjmuje jeden argument i zwraca cos
;compose zwraca funkcje tworzaca ktora zwraca g na stworzonej zmiennej
;a pozniej f na wyniku g
;czyli skoro f sie odpala na wyniku g, to g zwraca typ ktory f przyjmuje
;no a skoro mamy (f (g x)) to to jest zlozenie funkcji, wiec c->b
;czyli ('a -> 'b) ('c -> 'a) -> ('c -> 'b)

(define (flip f) (lambda (x y) (f y x)))
;na wejsciu dostajemy funkcje f ktora przyjmuje dwa argumenty
;zwracamy funkcje tworzaca ktora ma 'a i 'b
;i odpala funkcje f na 'b i 'a
; wiec mamy ('a 'b -> c) -> ('b 'a -> c))

(define (curry f) (lambda (x) (lambda (y) (f x y))))
;(('a 'b -> 'c) -> ('a -> ('b -> 'c)))
;funkcja f przyjmuje dwa argumenty i zwraca jakis trzeci
;czyli na wejsciu a b -> c
;na wyjsciu mamy funkcje tworzaca ktora zwraca
;funkcje tworzaca ktora zwraca funkcje f na stworzonych zmiennych
;w naszym przypadku x - 'a
; y - 'b





