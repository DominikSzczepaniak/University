#lang racket

(define (morse-decode str)
  (define (parse-spaces str answer)
    (if (equal? "" (substring str 0))
        answer
        (if (equal? #\ (string-ref str 0))
            (if (and (equal? (make-string 1 (string-ref answer (- (string-length answer) 1))) " ") (equal? (make-string 1 (string-ref answer (- (string-length answer) 2))) " "))
                (parse-spaces (substring str 1) answer)
                (parse-spaces (substring str 1) (string-append answer " ")))
            (parse-spaces (substring str 1) (string-append answer (make-string 1 (string-ref str 0)))))))
  (set! str (parse-spaces str ""))
  (define (parse-to-list str ans l)
    (if (equal? "" (substring str 0))
        (append l (list ans))
        (if (equal? #\ (string-ref str 0))
            (if (equal? #\ (string-ref str 1))
                (parse-to-list (substring str 2) "" (append l (list ans) (list " ")))
                (parse-to-list (substring str 1) "" (append l (list ans))))
            (parse-to-list (substring str 1) (string-append ans (make-string 1 (string-ref str 0))) l))))
  (define lista (parse-to-list str "" (list)))
  ;lista)
  (define (decoding l answer)
    (if (null? l)
        answer
        (let ((sym (first l)))
          (let ((litera
                 (cond
                   [(equal? sym "_____") "0"]
                   [(equal? sym ".____") "1"]
                   [(equal? sym "..___") "2"]
                   [(equal? sym "...__") "3"]
                   [(equal? sym "...._") "4"]
                   [(equal? sym ".....") "5"]
                   [(equal? sym "_....") "6"]
                   [(equal? sym "__...") "7"]
                   [(equal? sym "___..") "8"]
                   [(equal? sym "____.") "9"]
                   [(equal? sym "._") "A"]
                   [(equal? sym "_...") "B"]
                   [(equal? sym "_._.") "C"]
                   [(equal? sym "_..") "D"]
                   [(equal? sym ".") "E"]
                   [(equal? sym ".._.") "F"]
                   [(equal? sym "__.") "G"]
                   [(equal? sym "....") "H"]
                   [(equal? sym "..") "I"]
                   [(equal? sym ".___") "J"]
                   [(equal? sym "_._") "K"]
                   [(equal? sym "._..") "L"]
                   [(equal? sym "__") "M"]
                   [(equal? sym "_.") "N"]
                   [(equal? sym "___") "O"]
                   [(equal? sym ".__.") "P"]
                   [(equal? sym "__._") "Q"]
                   [(equal? sym "._.") "R"]
                   [(equal? sym "...") "S"]
                   [(equal? sym "_") "T"]
                   [(equal? sym ".._") "U"]
                   [(equal? sym "..._") "V"]
                   [(equal? sym ".__") "W"]
                   [(equal? sym "_.._") "X"]
                   [(equal? sym "_.__") "Y"]
                   [(equal? sym "__..") "Z"]
                   [(equal? sym " ") " "])))
            (decoding (rest l) (string-append answer litera))))))
  (decoding lista ""))

(morse-decode "__ .__.              ..___ _____ ..___ ..___")