#lang plait

(define (sprawdz a)
  (begin
    (display a)
    a))
      
(define-syntax my-and
  (syntax-rules ()
    [(my-and a)
     a]
    [(my-and a1 a2 ...)
     (if (eq? a1 #f)
         #f
         (my-and a2 ...))]))

(my-and #f (sprawdz #t))
(my-and #t (sprawdz #f))

(define-syntax my-or
  (syntax-rules ()
    [(my-or a)
     a]
    [(my-or a1 a2 ...)
     (if (eq? a1 #t)
         #t
         (my-or a2 ...))]))

(my-or #t (sprawdz #t))


(define-syntax my-let
  (syntax-rules ()
    ((my-let ((var expr) ...) body)
     ((lambda (var ...) body) expr ...))))

(define-syntax my-let*
  (syntax-rules ()
    ((my-let* () body)
     ((lambda () body)))
    ((my-let* ((var1 expr1) (var2 expr2) ...) body)
     ((lambda (var1)
        (my-let* ((var2 expr2) ...)
          body))
      expr1))))


(define x 5)
(my-let ((y 3)) (+ x y))
(my-let* ((x 4) (y 2)) (+ y x)) 