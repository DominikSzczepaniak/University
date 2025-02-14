#lang racket
(require "syntax.rkt")
(require (only-in plait s-exp-content))
(provide
 op-parser
 (contract-out
  [run-parser (-> any/c any/c void)]
  [match-sexp (-> any/c any/c boolean?)]))
(define (match-sexp pat s)
  (match pat
    ['ANY    (list s)]
    ['SYMBOL (and (symbol? s) (list s))]
    ['NUMBER (and (number? s) (list s))]
    ['()     (and (null? s)   null)]
    [(cons p1 p2)
     (and (pair? s)
          (let ([r1 (match-sexp p1 (car s))])
            (and r1
                 (let ([r2 (match-sexp p2 (cdr s))])
                   (and r2 (append r1 r2))))))]
    [_
     (cond
       [(symbol? pat) (and (symbol? s) (eq? pat s) null)])]))

(define (run-parser p s)
  (match p
    ['() (error "Syntax error")]
    [(cons (list pat action) rest-p)
     (let ([r (match-sexp pat s)])
       (if r
           (apply action r)
           (run-parser rest-p s)))]))


(define op-parser
  `((+ ,op-add)
    (- ,op-sub)
    (* ,op-mul)
    (/ ,op-div)))

