#lang plait

(define-type MyRacket
  (r-variable [x : Symbol])
  (r-num [n : Number])
  (r-lambda [var : (Listof Symbol)] [exp : MyRacket])
  (r-func [f : Symbol] [var : (Listof MyRacket)])
  (r-let [l : (Listof (Symbol * MyRacket))] [exp : MyRacket])
  (r-if [con : MyRacket] [t : MyRacket] [f : MyRacket])
  (r-cond [cs : (Listof (MyRacket * MyRacket))]))

(define (parse-all xs)
  (if (empty? xs)
      empty
      (cons (parse-Exp (first xs)) (parse-all (rest xs)))))

(define (parse-pairs xs)
  (if (empty? xs)
      empty
      (let ([wyr (s-exp->list (first xs))])
        (cons (pair (parse-Exp (first wyr))
                  (parse-Exp (second wyr)))
            (parse-pairs (rest xs))))))

(define (parse-Exp s)
  (cond
    [(s-exp-number? s) (r-num (s-exp->number s))]
    [(s-exp-symbol? s) (r-variable (s-exp->symbol s))]
    [(s-exp-list? s)
     (let ([xs (s-exp->list s)])
       (cond [(equal? (s-exp->symbol (first xs)) 'lambda) (r-lambda (parse-all (second xs)) (parse-Exp (third xs)))]
             [(equal? (s-exp->symbol (first xs)) 'let) (r-let (parse-pairs (second xs)) (parse-Exp (third xs)))]
             [(equal? (s-exp->symbol (first xs)) 'if) (r-if (parse-Exp (second xs))(parse-Exp (third xs))(parse-Exp (fourth xs)))]
             [(equal? (s-exp->symbol (first xs)) 'cond) (r-cond (parse-pairs (rest xs)))]
             [else ;aplikacja
              (r-func (s-exp->symbol (second xs)) (parse-all (rest xs)))]))]))

