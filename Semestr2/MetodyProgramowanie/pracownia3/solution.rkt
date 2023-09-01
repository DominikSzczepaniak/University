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
  (appE [e1 : Exp] [e2 : (Listof Exp)])
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
    [(s-exp-match? `{ANY {ANY ...}} s)
     (appE (parse (first (s-exp->list s)))
           (parse-arg-list (s-exp->list (second (s-exp->list s))) '()))]
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
               (list (opE (varE 'n) (sub) (numE 1))))))))
          (appE (varE 'fact) (list (numE 5)))))
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
;; environments

(define-type Binding
  (bind [name : Symbol]
        [val : Value]))

(define-type func
  (funC [arg : (Listof Exp)] [b : Exp]))

(define-type StorableF
  (funS [f : func])
  (undefS))

(define-type BindingF
  (bindF [name : Symbol]
         [ref : (Boxof StorableF)]))

(define-type-alias Env (Listof Binding))
(define-type-alias EnvF (Listof BindingF))

(define mt-env empty)
(define mt-envF empty)
(define (extend-env [env : Env] [x : Symbol] [v : Value]) : Env
  (cons (bind x v) env))
(define (lookup-env [n : Symbol] [env : Env]) : Value
  (type-case (Listof Binding) env
    [empty (error 'lookup "unbound variable")]
    [(cons b rst-env) (cond
                        [(eq? n (bind-name b))
                         (bind-val b)]
                        [else (lookup-env n rst-env)])]))



(define (extend-envF-undef [env : EnvF] [x : Symbol]) : EnvF
  (cons (bindF x (box (undefS))) env))

(define (extend-envF [env : EnvF] [x : Symbol] [args : (Listof Exp)] body) : EnvF
  (cons (bindF x (box (funS (funC args body)))) env))

(define (find-var [env : EnvF] [x : Symbol]) : (Boxof StorableF)
  (type-case (Listof BindingF) env
    [empty (error 'lookup "unbound variable")]
    [(cons b rst-env) (cond
                        [(eq? x (bindF-name b))
                         (bindF-ref b)]
                        [else
                         (find-var rst-env x)])]))
  
(define (lookup-envF [x : Symbol] [env : EnvF]) : func
  (type-case StorableF (unbox (find-var env x))
    [(funS f) f]
    [(undefS) (error 'lookup-env "undefined variable")]))
   
(define (update-env! [env : EnvF] [x : Symbol] [args : (Listof Exp)] body) : Void
  (set-box! (find-var env x) (funS (funC args body))))

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

(define (checking-app [args : (Listof Exp)] [appGet : (Listof Exp)])
  (if (empty? appGet)
      #t
      (if (eq? (check-body-corectness args (first appGet)) #f)
          #f
          (checking-app args (rest appGet)))))

(define (check-body-corectness [args : (Listof Exp)] [body : Exp])
  (type-case Exp body
    [(numE n) #t]
    [(opE l o r) (and (check-body-corectness args l) (check-body-corectness args r))]
    [(ifE b l r)
     (and (check-body-corectness args b) (and (check-body-corectness args l) (check-body-corectness args r)))]
    [(varE x)
     (if (not (in-list args (varE x)))
         #f
         #t)]
    [(letE x e1 e2)
     (and (check-body-corectness args e1) (check-body-corectness (append args (list (varE x))) e2))]
    [(appE e1 e2)
     (and (check-body-corectness args e1) (checking-app args e2))]
    [else (error 'checking "cant be there")]))

(define (put-names-in-env [names : (Listof Exp)] [env : EnvF]) : EnvF
  (if (empty? names)
      env
      (put-names-in-env (rest names) (extend-envF-undef env (funE-name (first names))))))

(define (put-values-in-env [functions : (Listof Exp)] [envF : EnvF] functionsName) : EnvF
  (if (empty? functions)
      envF
      (put-values-in-env (rest functions) (eval-function (first functions) envF functionsName) functionsName)))

(define (get-functions-names funcs [ans : (Listof Exp)])
  (if (empty? funcs)
      ans
      (get-functions-names (rest funcs) (append ans (list (varE (funE-name (first funcs))))))))
                            

(define (eval-function [e : Exp] [envF : EnvF] [functions-name : (Listof Exp)]) : EnvF
  (type-case Exp e
    [(funE name args body)
     (if (eq? (check-argument-corectness args '()) #f)
         (error 'eval "Nazwy argumentow nie moga sie potwarzac")
         (if (eq? (check-body-corectness (append (append args functions-name) (list (varE name))) body) #f)
             (error 'eval "W ciele funkcji wystepuje zmienna ktora nie jest przyjmowana")
             (extend-envF envF name args body)))]
     ;a pozniej rozszerzyc srodowisko o obliczona wartosc funkcji (eval)
    [else (error 'eval "unpossible")]))

(define (eval-main [e : Exp] [env : Env] [envF : EnvF])
  (type-case Exp e
    [(defE def ex)
     (eval ex env (eval-functions def envF))]
    [else (error 'eval "blad")]))


(define (eval-functions [func : (Listof Exp)] [env : EnvF]) : EnvF
  (let ([nazwy (get-functions-names func '())])
    (let ([new-env (put-names-in-env func env)])
      (let ([now-env (put-values-in-env func new-env nazwy)])
        now-env))))
    

(define (eval [e : Exp] [env : Env] [envF : EnvF]) : Value
  (type-case Exp e
    [(numE n) n]
    [(appE e1 e2)
     (let ([lista_argumentow (eval-list-values e2 '() env envF)])
       (apply e1 lista_argumentow env envF))] 
    [(opE l o r) ((op->proc o) (eval l env envF) (eval r env envF))]
    [(ifE b l r)
     (if (= (eval b env envF) 0)
         (eval l env envF)
         (eval r env envF))]
    [(varE x)
     (lookup-env x env)]
    [(letE x e1 e2)
     (let ([v1 (eval e1 env envF)])
       (eval e2 (extend-env env x v1) envF))]
    [else (error 'eval "Cant be there")])) ;define, functions

(define (nadaj-wartosci [args : (Listof Exp)] [values : (Listof Value)] [env : Env])
  (if (and (empty? args) (empty? values))
      env
      (if (empty? args)
          (error 'eval "Too many values for function")
          (if (empty? values)
              (error 'eval "Not enough values for function")
              (nadaj-wartosci (rest args) (rest values) (extend-env env (varE-x (first args)) (first values)))))))

(define (eval-list-values [l : (Listof Exp)] [answer : (Listof Value)] [env : Env] [envF : EnvF]) : (Listof Value)
  (if (empty? l)
      answer
      (eval-list-values (rest l) (append answer (list (eval (first l) env envF))) env envF)))
  

(define (apply v1 v2 env envF)
  (let ([funkcja (lookup-envF (varE-x v1) envF)]) ;typ func (args body)
    (let ([new-env (nadaj-wartosci (funC-arg funkcja) v2 env)])
      (eval (funC-b funkcja) new-env envF))))
  #;(type-case Value v1
    [(funV x b env)
     (eval b (extend-env env x v2))]
    [(primopV f)
     (f v2)]
    [else (error 'apply "not a function")])

(define (run [s : S-Exp]) : Value
  (eval-main (parse-main s) mt-env mt-envF))
(module+ test
  (test
   (run `{define {[fun fact (n) = n]} for {let fact be 5 in {fact (1)}}})
   1)
  (test
   (run `{define {[fun fact (n) = {ifz n then 1 else {n * {fact ({n - 1})}}}]} for {fact (5)}})
        120)
  (test
   (run `{define {[fun even (n) = {ifz n then 0 else {odd ({n - 1})}}] [fun odd (n) = {ifz n then 42 else {even ({n - 1})}}]} for {even (1024)}})
   0)
  (test
   (run `{define
{[fun gcd (m n) = {ifz n
then m
else {ifz {m <= n}
then {gcd (m {n - m})}
else {gcd ({m - n} n)}}}]}
for
{gcd (81 63)}})
   9))
   
   