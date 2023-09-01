#lang plait

(define-type Op
  (op-add) (op-mul) (op-sub) (op-div) (op-pow))

(define-type Op1
  (op1-fac) (op1-unaryminus))

(define-type Exp
  (exp-number [n : Number])
  (exp-op [op : Op] [e1 : Exp] [e2 : Exp])
  (exp-op1 [op1 : Op1] [e1 : Exp]))

(define (parse-Op s)
  (let ([sym (s-exp->symbol s)])
  (cond
    [(equal? sym '+) (op-add)]
    [(equal? sym '-) (op-sub)]
    [(equal? sym '*) (op-mul)]
    [(equal? sym '/) (op-div)]
    [(equal? sym '^) (op-pow)])))

(define (parse-Op1 s)
  (let ([sym (s-exp->symbol s)])
    (cond
      [(equal? sym '!) (op1-fac)]
      [(equal? sym '-) (op1-unaryminus)])))

(define (parse-Exp s)
  (cond
    [(s-exp-number? s) (exp-number (s-exp->number s))]
    [(s-exp-list? s)
     (let ([xs (s-exp->list s)])
       (cond
         [(= 2 (length xs)) (exp-op1 (parse-Op1 (first xs)) (parse-Exp (second xs)))]
         [(= 3 (length xs)) (exp-op (parse-Op (first xs)) (parse-Exp (second xs)) (parse-Exp (third xs)))]))]))

; ==============================================

(define (power a b)
  (if (= b 0)
      1
      (if (even? b)
          (power (* a a) (/ b 2))
          (* a (power (* a a) (/ (- b 1) 2))))))

(define (factorial a)
  (if (= a 0)
      1
      (* a (factorial (- a 1)))))

(define (eval-op op)
  (type-case Op op
    [(op-add) +]
    [(op-sub) -]
    [(op-mul) *]
    [(op-div) /]
    [(op-pow) power]))

(define (eval-op1 op)
  (type-case Op1 op
    [(op1-fac) factorial]
    [(op1-unaryminus) (lambda (x) (* -1 x))]))

(define (eval e)
  (type-case Exp e
    [(exp-number n)    n]
    [(exp-op op e1 e2)
     ((eval-op op) (eval e1) (eval e2))]
    [(exp-op1 op e1)
     ((eval-op1 op) (eval e1))]))