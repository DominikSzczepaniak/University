#lang plait
(require "syntax.rkt")

(define-type (ParseResult 'a)
  (parse-err)
  (parse-ok [v : 'a] [rest : (Listof S-Exp)]))

(define (parse-op0 ss)
  (type-case (Listof S-Exp) ss
    [empty (parse-err)]
    [(cons op rest)
     (cond
       [(s-exp-match? `+ op) (parse-ok (op-add) rest)]
       [(s-exp-match? `- op) (parse-ok (op-sub) rest)]
       [else (parse-err)])]))

(define (parse-exp0 ss)
  (type-case (ParseResult Exp) (parse-exp1 ss)
    [(parse-err) (parse-err)]
    [(parse-ok e1 rest)
     (type-case (ParseResult Op) (parse-op0 rest)
       [(parse-err)         (parse-ok e1 rest)]
       [(parse-ok op rest2)
        (type-case (ParseResult Exp) (parse-exp0 rest2)
          [(parse-err) (parse-err)]
          [(parse-ok e2 rest3) (parse-ok (exp-op op e1 e2) rest3)])])]))

(define (parse-exp1 ss)
  (type-case (ParseResult Exp) (parse-exp2 ss)
    [(parse-err) (parse-err)]
    [(parse-ok e2 rest)
     (type-case (ParseResult Op) (parse-op1 rest)
       [(parse-err) (parse-ok e2 rest)]
       [(parse-ok op rest2)
        (type-case (ParseResult Exp) (parse-exp1 rest2)
          [(parse-err) (parse-err)]
          [(parse-ok e3 rest3) (parse-ok (exp-op op e2 e3) rest3)])])]))
       

(define (parse-op1 ss)
  (type-case (Listof S-Exp) ss
    [empty (parse-err)]
    [(cons op rest)
     (cond
       [(s-exp-match? `* op) (parse-ok (op-mul) rest)]
       [(s-exp-match? `/ op) (parse-ok (op-div) rest)]
       [else (parse-err)])]))

(define (parse-exp2 ss)
  (type-case (Listof S-Exp) ss
    [empty (parse-err)]
    [(cons s rest)
     (cond
       [(s-exp-number? s) (parse-ok (exp-number (s-exp->number s)) rest)]
       [(s-exp-list? s)
        (type-case (ParseResult Exp) (parse-exp0 (s-exp->list s))
          [(parse-err) (parse-err)]
          [(parse-ok e rest2)
           (if (empty? rest2)
               (parse-ok e rest)
               (parse-err))])])]))
 


  
 
(define (parse-exp s)
  (type-case (ParseResult Exp) (parse-exp0 (list s))
    [(parse-err) (error 'parse-exp "Syntax error")]
    [(parse-ok e rest) 
     (if (empty? rest)
         e
         (error 'parse-exp "Syntax error"))]))
 
(define (eval-op op)
  (type-case Op op
    [(op-add) +]
    [(op-sub) -]
    [(op-mul) *]
    [(op-div) /]))

(define (eval e)
  (type-case Exp e
    [(exp-number n)    n]
    [(exp-op op e1 e2)
     ((eval-op op) (eval e1) (eval e2))]))

(define (calc s)
  (eval (parse-exp s)))    
          