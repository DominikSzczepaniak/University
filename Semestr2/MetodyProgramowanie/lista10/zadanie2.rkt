#lang plait

(module+ test
  (print-only-errors #t))

;; abstract syntax -------------------------------

(define-type Op
  (add)
  (sub)
  (mul)
  (div))

(define-type Exp
  (numE [n : Number])
  (opE [op : Op]
       [l : Exp]
       [r : Exp]))

;; parse ----------------------------------------

(define (parse [s : S-Exp]) : Exp
  (cond
    [(s-exp-match? `NUMBER s)
     (numE (s-exp->number s))]
    [(s-exp-match? `{SYMBOL ANY ANY} s)
     (opE (parse-op (s-exp->symbol (first (s-exp->list s))))
          (parse (second (s-exp->list s)))
          (parse (third (s-exp->list s))))]
    [else (error 'parse "invalid input")]))

(define (parse-op [op : Symbol]) : Op
  (cond
    [(eq? op '+) (add)]
    [(eq? op '-) (sub)]
    [(eq? op '*) (mul)]
    [(eq? op '/) (div)]
    [else (error 'parse "unknown operator")]))
                 
(module+ test
  (test (parse `2)
        (numE 2))
  (test (parse `{+ 2 1})
        (opE (add) (numE 2) (numE 1)))
  (test (parse `{* 3 4})
        (opE (mul) (numE 3) (numE 4)))
  (test (parse `{+ {* 3 4} 8})
        (opE (add)
             (opE (mul) (numE 3) (numE 4))
             (numE 8)))
  (test/exn (parse `{{+ 1 2}})
            "invalid input")
  (test/exn (parse `{+ 1})
            "invalid input")
  (test/exn (parse `{^ 1 2})
            "unknown operator"))
  
;; eval --------------------------------------

(define-type-alias Value Number)

(define (op->proc [op : Op]) : (Value Value -> Value)
  (type-case Op op
    [(add) +]
    [(sub) -]
    [(mul) *]
    [(div) /]))

(define (eval [e : Exp]) : Value
  (type-case Exp e
    [(numE n) n]
    [(opE o l r) ((op->proc o) (eval l) (eval r))]))

; ....
; (trace eval)

(define (run [e : S-Exp]) : Value
  (eval (parse e)))

(module+ test
  (test (run `2)
        2)
  (test (run `{+ 2 1})
        3)
  (test (run `{* 2 1})
        2)
  (test (run `{+ {* 2 3} {+ 5 8}})
        19))

;; printer ———————————————————————————————————-

(define (print-value [v : Value]) : Void
  (display v))

(define (main [e : S-Exp]) : Void
  (print-value (eval (parse e))))

;; abstract machine ---------------------------

(define-type Stack
  (emptyS)
  (rightS [op : Op] [exp : Exp] [s : Stack])
  (leftS [op : Op] [val : Value] [s : Stack]))

(define (evalAM [e : Exp] [s : Stack]) : Value
  (type-case Exp e
    [(numE n)
     (continueAM s n)]
    [(opE op e1 e2)
     (evalAM e1 (rightS op e2 s))]))

(define (continueAM [s : Stack] [v : Value]) : Value
  (type-case Stack s
    [(emptyS)
     v]
    [(rightS op e s)
     (evalAM e (leftS op v s))]
    [(leftS op u s)
     (continueAM s ((op->proc op) v u))]))
  
(define (runAM [e : S-Exp]) : Value
  (evalAM (parse e) (emptyS)))

(module+ test
  (test (run `2)
        (runAM `2))
  (test (run `{+ 2 1})
        (runAM `{+ 2 1}))
  (test (run `{* 2 1})
        (runAM `{* 2 1}))
  (test (run `{+ {* 2 3} {+ 5 8}})
        (runAM `{+ {* 2 3} {+ 5 8}})))

;; virtual machine and compiler ----------------

;; byte code

(define-type Instr
  (pushI [n : Value])
  (opI [op : Op]))
 
(define-type-alias Code (Listof Instr))

;; stack

(define-type-alias StackVM (Listof Value))
(define mtS : StackVM empty)
(define (pushS [v : Value] [s : StackVM]) : StackVM
  (cons v s))
(define (popS [s : StackVM]) : (Value * StackVM)
  (type-case StackVM s
    [empty
     (error 'popS "empty stack")]
    [(cons v s)
     (pair v s)]))

(define (evalVM [c : Code] [s : StackVM]) : Value
  (type-case Code c
    [empty
     (fst (popS s))]
    [(cons i c)
     (type-case Instr i
       [(pushI n)
        (evalVM c (pushS n s))]
       [(opI op)
        (let* ([n2-s2 (popS s)]
               [n2 (fst n2-s2)]
               [s2 (snd n2-s2)]
               [n1-s1 (popS s2)]
               [n1 (fst n1-s1)]
               [s1 (snd n1-s1)]
               [s0 (pushS ((op->proc op) n1 n2) s1)])
          (evalVM c s0))])]))

(module+ test
  (test/exn (evalVM (list (opI (add))) mtS)
            "empty stack"))

;; compiler


;decompile - idziemy od konca. pierwszy znak to najmocniejsza operacja ktora przyjmuje dwa wejscia
; drugi znak to albo operacja albo pushI liczba
; jesli operacja to jest to nowa lista ktora przyjmuje znowu dwa operatory
; pozniej znowu chcemy dostac dwa znaki
; jesli liczba to to jest prawa strona naszej rownosci
; jesli znak to otwieramy znowu skladanie

     
; jak wyglada ogolna sytuacja
; opI? -> (lewe) (prawe)
; pushI -> (prawe)
; lewe wiemy jak szukac, jak szukac prawe?

; za kazdym razem jak jest opI i dwa nastepne to pushI to laczyc to w jedno exp i zaczynac od nowa?

                     
; modyfikujemy rekurencyjnie
; jesli dostajemy opI to robimy tak
; (lista e do miejsca opI) + (opE (opI (funkcja-reku na nastepnym) (funkcja-reku na 2 dalej)) + reszta
; jesli pushI to zwracamy numE z wartosci
; jednak nie bo sie typy wypierdalaja
; tzn ine mozemy przerobic czegos na opE bo type-case nie bedzie dzialal

; moze nowy typ?
; (list
;  (opI (add))
;  (opI (div))
;  (opI (mul))
;  (opI (mul))
;  (pushI 2)
;  (pushI 1)
;  (pushI 1)
;  (opI (sub))
;  (pushI 7)
;  (pushI 8)
;  (opI (mul))
;  (pushI 4)
;  (pushI 3))


; po kolei
; type-case stare nowe

; wyjdzie stare

; teraz na tym type-case
; opI  - chcemy zwrocic opE (rekurencja na nastepnym elemencie) (rekurencja na elemencie o dwa dalej po zakonczeniu pierwszej reku)

; no to robimy rekurencje na nastepnym

; mamy znowu stare -> opI 
; znowu reku na kolejnym 
; mamy znowu stare -> opI 
; znowu reku na kolejnym (opI mul)
; teraz mamy stare -> pushI 
; wiec mamy lewy element i robimy reku na elemencie o dwa dalej 
; czyli stare -> pushI i mamy prawy
; zwracamy (opE mul 2 1)
; jestesmy w opI div
; mamy lewy -> (opE mul 2 1)
; robimy reku o dwa dalej czyli na opI sub 

; dziala

; musimy modyfikowac za kazdym razem liste gdy wracamy
; np gdy wrocimy do (opI div) to elementem o dwa dalej jest pushI 1 w liscie ktora on dostal 
; czyli chcemy robic tak:
; (rekurencja (lista do miejsca ktore sprawdzamy wlacznie) + (lista reku na kolejnym elemencie)
;  + reszta czyli element po prawym elemencie (bo jak sie wykona reku na wewnetrznych elementach to zawsze beda tylko dwa elementy

; (list
;  (opI (add))
;  (opI (sub))
;  (pushI 5)
;  (opI (div))
;  (pushI 1)
;  (pushI 2)
;  (opI (mul))
;  (pushI 3)
;  (pushI 3))

; zaczynamy od opI add
; lewy to kolejny element - opI sub
; musimy wiec sprawdzic gdzie sie skonczy opI sub
; wchodzimy do opI sub
; lewy to pushI wiec koniec na 3
; prawy to opI div wiec wchodzimy
; 2x pushI wiec koniec na 6
; wraca informacja 6 do opI sub
; opisub przekazuje do opI add 6
; wiec prawy zaczyna sie w 7


;czyli jakie funkcje potrzebujemy?
;jedna - gdzie konczy sie wyrazenie ktore zaczyna sie w miejscu i
;jak sie tego dowiedziec?
;sprawdzamy gdzie konczy sie wyrazenie na nastepnym miejscu i oznaczamy ta wartosc jako x
;i pozniej sprawdzamy gdzie konczy sie wyrazenie z miejsca x+1
;i ten wynik przekazujemy wyzej jako y
;w miejscu y+1 mamy kolejne wyrazenie

;operujemy tylko na jednym typie - Instr, nie potrzeba nam Decompiling
;wejscie jest zreversowane

(define (sprawdz-koniec [e : (Listof Instr)] [i : Number]) : Number
  (type-case Instr (list-ref e i)
    [(opI c) (let* ((koniec-lewy (sprawdz-koniec e (+ i 1)))
                    (koniec-prawy (sprawdz-koniec e (+ koniec-lewy 1))))
               koniec-prawy)]
    [(pushI d) i]))
                     
(define (decompiling-to-exp e i)
  (type-case Instr (list-ref e i)
    [(opI c)
     (let ((prawy (decompiling-to-exp e (+ i 1)))
           (koniec-lewego-wyrazenia (sprawdz-koniec e (+ i 1))))
       (opE c (decompiling-to-exp e (+ 1 koniec-lewego-wyrazenia)) prawy))]
    [(pushI d) (numE d)]))

(define (op->s-exp [op : Op])
  (type-case Op op
    [(add) `+]
    [(sub) `-]
    [(mul) `*]
    [(div) `/]))

(define (exp-to-s-exp input)
  (type-case Exp input
    [(opE a b c)
     (let ((znak (op->s-exp a))
           (wartosc1 (exp-to-s-exp b))
           (wartosc2 (exp-to-s-exp c)))
       `(,znak ,wartosc1 ,wartosc2))]
    [(numE a)
     (number->s-exp a)]))
           

(define (decompile [e : Code]) ;code = Listof Instr ; first - (opE (opfirst) (second) (third)) then second = (opsecond (third) (fourth)) (third) = ...
  (exp-to-s-exp (decompiling-to-exp (reverse e) 0)))

  
  

(define (compile [e : Exp]) : Code
  (type-case Exp e
    [(numE n)
     (list (pushI n))]
    [(opE op e1 e2)
     (append (compile e1)
             (append (compile e2)
                     (list (opI op))))]))

(module+ test
  (test (compile (parse `2))
        (list (pushI 2)))
  (test (compile (parse `{+ {* 2 3} {+ 5 8}}))
        (list (pushI 2) (pushI 3) (opI (mul)) (pushI 5) (pushI 8) (opI (add)) (opI (add)))))

(define (testFunc [e : S-Exp])
  (compile (parse e)))

(define (runVM [e : S-Exp]) : Value
  (evalVM (compile (parse e)) mtS))

(module+ test
  (test (run `2)
        (runVM `2))
  (test (run `{+ 2 1})
        (runVM `{+ 2 1}))
  (test (run `{* 2 1})
        (runVM `{* 2 1}))
  (test (run `{- {* 2 3} {+ 5 8}})
        (runVM `{- {* 2 3} {+ 5 8}})))