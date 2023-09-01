#lang plait

(module+ test
  (print-only-errors #t))

;; abstract syntax -------------------------------

(define-type Op
  (add)
  (sub)
  (mul)
  (div)
  (eql)
  (leq))

(define-type Selector
  (car)
  (cdr))

(define-type Mylist
  (mynull)
  (mylist [head : 'a] [rest : Mylist]))

(define-type Exp
  (numE [n : Number])
  (opE [op : Op]
       [l : Exp]
       [r : Exp])
  (ifE [b : Exp]
       [l : Exp]
       [r : Exp])
  (condE [cs : (Listof (Exp * Exp))])
  (null?E [e : Exp])
  (selectorE [s : Selector]
             [e : Exp])
  (myconsE [fst : 'a] [snd : 'b])
  (mylistE [l : Mylist])
  (nullE))

;; parse ----------------------------------------

(define (parse [s : S-Exp]) : Exp
  (cond
    [(s-exp-match? `null s)
     (nullE)]
    
    [(s-exp-match? `{null? ANY} s)
     (null?E (parse (second (s-exp->list s))))]
    
    [(s-exp-match? `{car ANY} s)
     (selectorE (parse-selector (first (s-exp->list s)))
           (parse (second (s-exp->list s))))]
    
    [(s-exp-match? `{cdr ANY} s)
     (selectorE (parse-selector (first (s-exp->list s)))
           (parse (second (s-exp->list s))))]
    
    [(s-exp-match? `{cons ANY ANY} s)
     (myconsE (parse (second (s-exp->list s)))
                     (parse (third  (s-exp->list s))))]
    
    [(s-exp-match? `{list ANY ...} s)
     (mylistE (parse-mylist (rest (s-exp->list s))))]

    
    [(s-exp-match? `NUMBER s)
     (numE (s-exp->number s))]
    [(s-exp-match? `{if ANY ANY ANY} s)
     (ifE (parse (second (s-exp->list s)))
          (parse (third (s-exp->list s)))
          (parse (fourth (s-exp->list s))))]
    [(s-exp-match? `{cond ANY ...} s)
     (condE (parse-cond (rest (s-exp->list s))))]
    [(s-exp-match? `{SYMBOL ANY ANY} s)
     (opE (parse-op (s-exp->symbol (first (s-exp->list s))))
          (parse (second (s-exp->list s)))
          (parse (third (s-exp->list s))))]
    [else (error 'parse "invalid input")]))

(define (parse-mylist xs)
  (type-case (Listof S-Exp) xs
    [empty (mynull)]
    [(cons x xs) (mylist (parse x) (parse-mylist xs))]))

(define (parse-selector s)
  (cond [(s-exp-match? s `car) (car)]
        [(s-exp-match? s `cdr) (cdr)]
        [else (error 'parse-selector "Wrong selector")]))

(define (parse-cond [ss : (Listof S-Exp)]) : (Listof (Exp * Exp))
  (type-case (Listof S-Exp) ss
    [empty
     empty]
    [(cons s ss)
     (if (s-exp-match? `{ANY ANY} s)
         (cons (pair (parse (first (s-exp->list s)))
                     (parse (second (s-exp->list s))))
               (parse-cond ss))
         (error 'parse "invalid input: cond"))]))

(define (parse-op [op : Symbol]) : Op
  (cond
    [(eq? op '+) (add)]
    [(eq? op '-) (sub)]
    [(eq? op '*) (mul)]
    [(eq? op '/) (div)]
    [(eq? op '=) (eql)]
    [(eq? op '<=) (leq)]
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
  (test (parse `{if {= 0 1} {* 3 4} 8})
        (ifE (opE (eql) (numE 0) (numE 1))
             (opE (mul) (numE 3) (numE 4))
             (numE 8)))
   (test/exn (parse `{{+ 1 2}})
            "invalid input")
  (test/exn (parse `{+ 1})
            "invalid input")
  (test/exn (parse `{^ 1 2})
            "unknown operator")
  (test (parse `{cond {{= 0 1} {* 3 4}}
                      {{= 1 1} 8}})
        (condE (list (pair (opE (eql) (numE 0) (numE 1))
                           (opE (mul) (numE 3) (numE 4)))
                     (pair (opE (eql) (numE 1) (numE 1))
                           (numE 8))))))
  
;; eval --------------------------------------

(define-type Value
  (numV [n : Number])
  (boolV [b : Boolean])
  (listV [l : (Listof Value)])
  (consV [l : Value] [r : Value])
  (nullV))

(define (op-num-num->proc [f : (Number Number -> Number)]) : (Value Value -> Value)
  (λ (v1 v2)
    (type-case Value v1
      [(numV n1)
       (type-case Value v2
         [(numV n2)
          (numV (f n1 n2))]
         [else
          (error 'eval "type error")])]
      [else
       (error 'eval "type error")])))

(define (op-num-bool->proc [f : (Number Number -> Boolean)]) : (Value Value -> Value)
  (λ (v1 v2)
    (type-case Value v1
      [(numV n1)
       (type-case Value v2
         [(numV n2)
          (boolV (f n1 n2))]
         [else
          (error 'eval "type error")])]
      [else
       (error 'eval "type error")])))

(define (isnull? [e : Value]) : Value
  (type-case Value e
    [(nullV) (boolV #t)]
    [else (boolV #f)]))

(define (op->proc [op : Op]) : (Value Value -> Value)
  (type-case Op op
    [(add) (op-num-num->proc +)]
    [(sub) (op-num-num->proc -)]
    [(mul) (op-num-num->proc *)]
    [(div) (op-num-num->proc /)]
    [(eql) (op-num-bool->proc =)]
    [(leq) (op-num-bool->proc <=)]))

(define (eval-listE xs)
  (type-case Mylist xs
    [(mynull) (nullV)]
    [(mylist first rest)
     (consV (eval first) (eval-listE rest))]))

(define (eval [e : Exp]) : Value
  (type-case Exp e
    [(numE n) (numV n)]
    [(opE o l r) ((op->proc o) (eval l) (eval r))]
    [(ifE b l r)
     (type-case Value (eval b)
       [(boolV v)
        (if v (eval l) (eval r))]
       [else
        (error 'eval "type error")])]
    [(condE cs)
     (eval (cond->if cs))]
    [(selectorE s e)
     (type-case Exp e
       [(mylistE xs)
        (type-case Selector s
          [(car) (eval (mylist-head (mylistE-l e)))]
          [(cdr) (eval (mylistE (mylist-rest (mylistE-l e))))])]
       [(myconsE a b)
        (type-case Selector s
          [(car) (eval a)]
          [(cdr) (eval b)])]
       [(selectorE a b)
        (type-case Selector s
          [(car) (consV-l (eval (selectorE a b)))]
          [(cdr) (consV-r (eval (selectorE a b)))])]
       [else (error 'selectorE "Wrong argument of selector")])]        
    [(myconsE a b) (consV (eval a)
                      (eval b))]
    [(mylistE xs) (eval-listE xs)]
    [(nullE) (nullV)]
    [(null?E e) (isnull? (eval e))]))

(define (cond->if [cs : (Listof (Exp * Exp))]) : Exp
  (type-case (Listof (Exp * Exp)) cs
    [empty
     (numE 42)]
    [(cons c cs)
     (ifE (fst c)
          (snd c )
          (cond->if cs))]))

(define (run [e : S-Exp]) : Value
  (eval (parse e)))

(module+ test)
  (test (run `2)
        (numV 2))
  (test (run `{+ 2 1})
        (numV 3))
  (test (run `{* 2 1})
        (numV 2))
  (test (run `{+ {* 2 3} {+ 5 8}})
        (numV 19))
  (test (run `{= 0 1})
        (boolV #f))
  (test (run `{if {= 0 1} {* 3 4} 8})
        (numV 8))
  (test (run `{cond {{= 0 1} {* 3 4}}
                    {{= 1 1} 8}})
        (numV 8))
  (test (run `{cons 1 2})
        (consV (numV 1) (numV 2)))
  (test (run `{null? null})
             (boolV #t))
  (test (run `{car {list 1 2 3}})
        (numV 1))
  (test (run `{cdr {list 1 2 3}})
        (consV (numV 2) (consV (numV 3) (nullV))))
  (test (run `{cons 1 {list 1 2 3}})
        (consV (numV 1)
               (consV (numV 1)
                      (consV (numV 2) (consV (numV 3) (nullV))))))

;; printer ———————————————————————————————————-

#|(define (value->string [v : Value]) : String
  (type-case Value v
    [(numV n) (to-string n)]
    [(boolV b) (if b "true" "false")]))

(define (print-value [v : Value]) : Void
  (display (value->string v)))

(define (main [e : S-Exp]) : Void
  (print-value (eval (parse e))))|#