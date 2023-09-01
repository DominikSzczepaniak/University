#lang plait

(module+ test
  (print-only-errors #t))

;; abstract syntax -------------------------------

(define-type Op
  (add) (sub) (mul))

(define-type Exp
  (numE [n : Number])
  (opE [op : Op] [e1 : Exp] [e2 : Exp])
  (varE [x : Symbol])
  (lamE [x : Symbol] [e : Exp])
  (appE [e0 : Exp] [e1 : Exp])
  (countE))

;; semantics: the identity monad and values
(define-type-alias State Number)
(define-type-alias (M 'a) ('a * State))

(define (returnM [v : 'a]) : (M 'a)
  (pair v 0))

(define (bindM [c : (M 'a)] [f : ('a -> (M 'b))]) : (M 'b)
  (f (fst c)))

(define (errorM [l : Symbol] [m : String]) : (M 'a)
  (error l m))

(define (showM [c : (M Value)]) : String
  (string-append "value: " (string-append (value->string (fst c)) (string-append ", state: " (to-string (snd c))))))

(define (tickM (wyr : (M 'a))) : (M 'a)
  (pair (fst wyr) (add1 (snd wyr))))
  

(define-type Value
  (numV [n : Number])
  (funV [f : (Value -> (M Value))]))

(define (value->string [v : Value]) : String
  (type-case Value v
    [(numV n) (to-string n)]
    [(funV _) "#<procedure>"]))

;; environments

(define-type Binding
  (bind [name : Symbol]
        [val : Value]))

(define-type-alias Env (Listof Binding))

(define mt-env empty)

(define (extend-env [env : Env] [x : Symbol] [v : Value]) : Env
  (cons (bind x v) env))

(define (lookup-env [x : Symbol] [env : Env]) : (M Value)
  (type-case (Listof Binding) env
    [empty
     (errorM 'lookup-env "unbound variable")]
    [(cons b rst-env)
     (cond
       [(eq? x (bind-name b))
        (returnM (bind-val b))]
       [else
        (lookup-env x rst-env)])]))

;; primitive operations

(define (op-num-num->proc [f : (Number Number -> Number)]) : ((M Value) (M Value) -> (M Value))
  (λ (v1 v2) (pair (numV (f (numV-n (fst v1)) (numV-n (fst v2)))) (+ (+ 1 (snd v1)) (snd v2)))))

(define (op->proc [op : Op]) : ((M Value) (M Value) -> (M Value))
  (type-case Op op
    [(add) (op-num-num->proc +)]
    [(sub) (op-num-num->proc -)]
    [(mul) (op-num-num->proc *)]))

;; evaluation function (eval/apply)

(define (eval [e : Exp] [env : Env]) : (M Value)
  (type-case Exp e
    [(numE n)
     (returnM (numV n))]
    [(opE o e1 e2)
     (let ([one (eval e1 env)]
           [two (eval e2 env)])
         ((op->proc o) one two))]
    [(varE x)
     (lookup-env x env)]
    [(lamE x b)
     (returnM (funV (λ (v) (eval b (extend-env env x v)))))]
    [(appE e0 e1)
     (let ([one (eval e0 env)]
           [two (eval e1 env)])
       (apply one two))]
    [(countE)
     (pair (numV 1) 0)]))

(define (apply [v0 : (M Value)] [v1 : (M Value)]) : (M Value)
  (type-case Value (fst v0)
    [(funV f)
     (let ([wynik (f (fst v1))])
       (pair (fst wynik) (+ 1 (+ (snd wynik) (+ (snd v0) (snd v1))))))]
    [else (errorM 'apply "not a function")]))

(define (run [e : S-Exp]) : String
  (showM (eval (parse e) mt-env)))

(module+ test
  (test (run `2)
        "2")
  (test (run `{+ 2 1})
        "3")
  (test (run `{* 2 1})
        "2")
  (test (run `{+ {* 2 3} {+ 5 8}})
        "19")
  (test (run `{{lambda {x} {+ x 1}} 5})
        "6")
  (test/exn (run `{1 2})
            "not a function")
  (test (run `{+ {+ count count}
                 {+ count count}})
        "value: 4, state: 3"))

;; parse ----------------------------------------

(define (parse [s : S-Exp]) : Exp
  (cond
    [(s-exp-match? `NUMBER s)
     (numE (s-exp->number s))]
    [(s-exp-match? `count s)
     (countE)]
    [(s-exp-match? `{lambda {SYMBOL} ANY} s)
     (lamE (s-exp->symbol
            (first (s-exp->list 
                    (second (s-exp->list s)))))
           (parse (third (s-exp->list s))))]
    [(s-exp-match? `{SYMBOL ANY ANY} s)
     (opE (parse-op (s-exp->symbol (first (s-exp->list s))))
          (parse (second (s-exp->list s)))
          (parse (third (s-exp->list s))))]
    [(s-exp-match? `SYMBOL s)
     (varE (s-exp->symbol s))]
    [(s-exp-match? `{ANY ANY} s)
     (appE (parse (first (s-exp->list s)))
           (parse (second (s-exp->list s))))]
    [else (error 'parse "invalid input")]))

(define (parse-op [op : Symbol]) : Op
  (cond
    [(eq? op '+) (add)]
    [(eq? op '-) (sub)]
    [(eq? op '*) (mul)]
    [else (error 'parse "unknown operator")]))
