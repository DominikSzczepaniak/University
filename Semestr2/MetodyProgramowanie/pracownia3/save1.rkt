#lang plait

(module+ test
  (print-only-errors #t))

;============================
; abstract syntax

(define-type Op
  (add) (sub) (mul) (leq))

(define-type Exp
  (numE [n : Number])
  (opE [l : Exp] [op : Op] [r : Exp])
  (ifE [b : Exp] [l : Exp] [r : Exp])
  (varE [x : Symbol])
  (letE [x : Symbol] [e1 : Exp] [e2 : Exp])
  (appE [e1 : Exp] [e2 : Exp])
  (funE [name : Symbol] [args : (Listof Exp)] [body : Exp])
  (defE [definitions : (Listof Exp)] [e : Exp]))

;============================
;parse

(define (parse-arg-list s answer)
  (if (empty? s)
      answer
      (parse-arg-list (rest s) (append answer (list (parse (first s)))))))

(define (parse-func-list s answer)
  (if (empty? s)
      answer
      (parse-func-list (rest s) (append answer (list (parse-func (first s)))))))

(define (parse-main [s : S-Exp]) : Exp
  (cond
    [(s-exp-match? `{define {ANY ...} for ANY} s)
     (defE (parse-func-list (s-exp->list (second (s-exp->list s))) '())
           (parse (fourth (s-exp->list s))))]
    [else (error 'parse "invalid input")]))

(define (parse-func [s : S-Exp]) : Exp
  (cond
   [(s-exp-match? `{fun SYMBOL {ANY ...} = ANY} s)
     (funE (s-exp->symbol (second (s-exp->list s)))
           (parse-arg-list (s-exp->list (third (s-exp->list s))) '())
           (parse (list-ref (s-exp->list s) 4)))]
   [else (error 'parse "invalid input")]))

(define (parse [s : S-Exp]) : Exp
  (cond
    [(s-exp-match? `NUMBER s)
     (numE (s-exp->number s))]
    [(s-exp-match? `{ANY SYMBOL ANY} s)
     (opE (parse (first (s-exp->list s)))
          (parse-op (s-exp->symbol (second (s-exp->list s))))
          (parse (third (s-exp->list s))))]
    [(s-exp-match? `{ifz ANY then ANY else ANY} s)
     (ifE (parse (second (s-exp->list s)))
          (parse (fourth (s-exp->list s)))
          (parse (list-ref (s-exp->list s) 5)))]
    [(s-exp-match? `SYMBOL s)
     (varE (s-exp->symbol s))]
    [(s-exp-match? `{let SYMBOL be ANY in ANY} s)
     (letE (s-exp->symbol (second (s-exp->list s)))
           (parse (list-ref (s-exp->list s) 3))
           (parse (list-ref (s-exp->list s) 5)))]
    [(s-exp-match? `{ANY {ANY}} s)
     (appE (parse (first (s-exp->list s)))
           (parse (first (s-exp->list (second (s-exp->list s))))))]
    [else (error 'parse "invalid input")]))

(define (parse-op [op : Symbol]) : Op
  (cond
    [(eq? op '+) (add)]
    [(eq? op '-) (sub)]
    [(eq? op '*) (mul)]
    [(eq? op '<=) (leq)]
    [else (error 'parse "unknown operator")]))

(module+ test
  (test (parse `2)
        (numE 2))
  (test (parse `{2 + 1})
        (opE (numE 2) (add) (numE 1)))
  (test (parse `n)
        (varE 'n))
  (test (parse `{ifz {3 <= 1} then 1 else 0})
        (ifE (opE (numE 3) (leq) (numE 1)) (numE 1) (numE 0)))
  (test (parse-main `{define
                  {[fun fact (n) = {ifz n then 1 else {n * {fact ({n - 1})}}}]}
                  for
                  {fact (5)}})
        (defE
          (list
           (funE
            'fact
            (list (varE 'n))
            (ifE
             (varE 'n)
             (numE 1)
             (opE
              (varE 'n)
              (mul)
              (appE
               (varE 'fact)
               (opE (varE 'n) (sub) (numE 1)))))))
          (appE (varE 'fact) (numE 5))))
  (test (parse-main `{define {{fun fact {x y z} = 1}
                         {fun notfact {x y z} = 2}}
                  for {let x be 3 in x}})
        (defE
          (list
           (funE 'fact (list (varE 'x) (varE 'y) (varE 'z)) (numE 1))
           (funE 'notfact (list (varE 'x) (varE 'y) (varE 'z)) (numE 2)))
          (letE 'x (numE 3) (varE 'x)))))

;============================
;eval
(define-type-alias Value Number)
(define-type Binding
  (bind [name : Symbol]
        [val : Value]))

;; environments

(define-type-alias Env (Listof Binding))

(define mt-env empty)
(define (extend-env [env : Env] [x : Symbol] [v : Value]) : Env
  (cons (bind x v) env))
(define (lookup-env [n : Symbol] [env : Env]) : Value
  (type-case (Listof Binding) env
    [empty (error 'lookup "unbound variable")]
    [(cons b rst-env) (cond
                        [(eq? n (bind-name b))
                         (bind-val b)]
                        [else (lookup-env n rst-env)])]))

; operations

(define (op-num-num->proc [f : (Number Number -> Number)]) : (Value Value -> Value)
  (λ (v1 v2)
    (f v1 v2)))

(define (op-num-bool->proc [f : (Number Number -> Boolean)]) : (Value Value -> Value)
  (λ (v1 v2)
    (if (eq? #t (f v1 v2))
        0
        1)))

(define (op->proc [op : Op]) : (Value Value -> Value)
  (type-case Op op
    [(add) (op-num-num->proc +)]
    [(sub) (op-num-num->proc -)]
    [(mul) (op-num-num->proc *)]
    [(leq) (op-num-bool->proc <=)]))

(define (in-list [l : (Listof Exp)] [arg : Exp]) : Boolean
  (if (empty? l)
      #f
      (if (equal? arg (first l))
          #t         
          (in-list (rest l) arg))))

(define (check-argument-corectness [args : (Listof Exp)] [done : (Listof Exp)]) : Boolean
  (if (empty? args)
      #t
      (if (eq? (in-list done (first args)) #t)
          #f
          (check-argument-corectness (rest args) (append done (list (first args)))))))

(define (eval [e : Exp] [env : Env]) : Value
  (type-case Exp e
    [(numE n) n]
    [(opE l o r) ((op->proc o) (eval l env) (eval r env))]
    [(ifE b l r)
     (if (= (eval b env) 0)
         (eval l env)
         (eval r env))]
    [(varE x)
     (lookup-env x env)]
    [(letE x e1 e2)
     (let ([v1 (eval e1 env)])
       (eval e2 (extend-env env x v1)))]
    [(appE e1 e2)
     1] ;TODO
    [(defE def e)
     1]
    [(funE name args body)
     (if (eq? (check-argument-corectness args '()) #f)
         (error 'eval "Nazwy argumentow nie moga sie potwarzac")
         1)]))



(define (run [s : S-Exp]) : Value
  (eval (parse s) mt-env))