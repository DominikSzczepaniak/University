#lang plait

;a) (curry compose)
;e) (compose curry flip)
;apply
;- (('a -> 'b) 'a -> 'b)
;> compose
;- (('a -> 'b) ('c -> 'a) -> ('c -> 'b))
;> flip
;- (('a 'b -> 'c) -> ('b 'a -> 'c))
;> curry
;- (('a 'b -> 'c) -> ('a -> ('b -> 'c)))

;a) (curry compose)
; typ1: (('a 'b -> 'c) -> ('a -> ('b -> 'c)))
; typ2: (('d -> 'e) ('f -> 'd) -> ('f -> 'e))
; typ1 bierze 'a 'b -> 'c
; 'a = ('d -> 'e)
; 'b = ('f -> 'd)
; 'c = ('f -> 'e)
; wynik podstawiamy odpowiednio w ('a -> ('b -> 'c))):
; (('d -> 'e) -> (('f -> 'd) -> ('f -> 'e)))) =
; (('a -> 'b) -> (('c -> 'a) -> ('c -> 'b))))

;b) ((curry compose) (curry compose))
; typ1: (('d->'e) -> [('f->'d) -> ('f -> 'e)])
; typ2: (('a->'b) -> [('c->'a) -> ('c -> 'b)])
; typ1 bierze funkcje 'd -> 'e
; więc 'd = ('a -> 'b)
; 'e = [('c->'a) -> ('c -> 'b)])
; podstawmy do [('f->'d) -> ('f -> 'e)])
; [('f->('a -> 'b)) -> ('f -> [('c->'a) -> ('c -> 'b)]))])


;c 0.5) (curry apply)
; typ1: (('a 'b -> 'c) -> ('a -> ('b -> 'c)))
; typ2: (('d -> 'e) 'd -> 'e)
; typ1 przyjmuje 'a 'b -> 'c
; 'a = ('d -> 'e)
; 'b = 'd
; 'c = 'e
; wynik:
; (('d -> 'e) -> ('d -> 'e))

;c) ((curry compose) (curry apply))
; typ1: (('a->'b) -> [('c->'a) -> ('c -> 'b)])
; typ2: (('d -> 'e) -> ('d -> 'e))
; typ1 przyjmuje 'a->'b
; 'a = ('d -> 'e)
; 'b = ('d -> 'e)
; wynik:
; [('c->('d -> 'e)) -> ('c -> ('d -> 'e))])

;d) ((curry apply) (curry compose))
; typ1: (('d -> 'e) -> ('d -> 'e))
; typ2: (('a -> 'b) -> (('c -> 'a) -> ('c -> 'b))))
; typ1 przyjmuje ('d -> 'e)
; 'd = ('a -> 'b)
; 'e = (('c -> 'a) -> ('c -> 'b))
; wynik:
; (('a -> 'b) -> (('c -> 'a) -> ('c -> 'b))))


;===========================================

;> compose
;- (('a -> 'b) ('c -> 'a) -> ('c -> 'b))
;> flip
;- (('a 'b -> 'c) -> ('b 'a -> 'c))
;> curry
;- (('a 'b -> 'c) -> ('a -> ('b -> 'c)))


;e) (compose curry flip)
;wykonujemy (f (g x))
;czyli wykonujemy (curry (flip x))

;skoro curry i flip maja takie samo wejscie, to wejsciem jest
; ('a 'b -> 'c)
; co bedzie wyjsciem?
; curry zwraca ('a -> ('b -> 'c)))
; flip zwraca ('b 'a -> 'c))
; wykona sie (curry (flip a b))
; czyli (curry ('b 'a -> 'c))
; wiec 'a = 'b
; 'b = 'a
; 'c = 'c
; czyli curry zwroci ('b -> ('a -> 'c)
; wiec mamy ('a 'b -> 'c) -> ('b -> ('a -> 'c)