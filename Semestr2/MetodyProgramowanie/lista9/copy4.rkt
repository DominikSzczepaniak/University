#lang racket
;(substring str 1) - rest of the string
;(string-ref str 0) - first letter

(define (make_string l answer)
  (if (null? l)
      (string-append answer " ")
      (make_string (rest l) (string-append answer (make-string 1 (first l))))))

(define (morse_code_list value)
  (if (= value -33)
      " "
  (list-ref (list (make_string (list #\. #\_) "") ;A
                  (make_string (list #\_ #\. #\. #\.) "") ;B
                  (make_string (list #\_ #\. #\_ #\.) "") ;C
                  (make_string (list #\_ #\. #\.) "") ;D
                  (make_string (list #\.) "") ;E
                  (make_string (list #\. #\. #\_ #\.) "") ;F
                  (make_string (list #\_ #\_ #\.) "") ;G
                  (make_string (list #\. #\. #\. #\.) "") ;H
                  (make_string (list #\. #\.) "") ;I
                  (make_string (list #\. #\_ #\_ #\_) "") ;J
                  (make_string (list #\_ #\. #\_) "") ;K
                  (make_string (list #\. #\_ #\. #\.) "") ;L
                  (make_string (list #\_ #\_) "") ;M
                  (make_string (list #\_ #\.) "") ;N
                  (make_string (list #\_ #\_ #\_) "") ;O
                  (make_string (list #\. #\_ #\_ #\.) "") ;P
                  (make_string (list #\_ #\_ #\. #\_) "") ;Q
                  (make_string (list #\. #\_ #\.) "") ;R
                  (make_string (list #\. #\. #\.) "") ;S
                  (make_string (list #\_) "") ;T
                  (make_string (list #\. #\. #\_) "") ;U
                  (make_string (list #\. #\. #\. #\_) "") ;V
                  (make_string (list #\. #\_ #\_) "") ;W
                  (make_string (list #\_ #\. #\. #\_) "") ;X
                  (make_string (list #\_ #\. #\_ #\_) "") ;Y
                  (make_string (list #\_ #\_ #\. #\.) "") ;Z
                  (make_string (list #\. #\_ #\_ #\_ #\_) "") ;1
                  (make_string (list #\. #\. #\_ #\_ #\_) "") ;2
                  (make_string (list #\. #\. #\. #\_ #\_) "") ;3
                  (make_string (list #\. #\. #\. #\. #\_) "") ;4
                  (make_string (list #\. #\. #\. #\. #\.) "") ;5
                  (make_string (list #\_ #\. #\. #\. #\.) "") ;6
                  (make_string (list #\_ #\_ #\. #\. #\.) "") ;7
                  (make_string (list #\_ #\_ #\_ #\. #\.) "") ;8
                  (make_string (list #\_ #\_ #\_ #\_ #\.) "") ;9
                  (make_string (list #\_ #\_ #\_ #\_ #\_) "")) value))) ;0
                  

(define (morse-code str)
  (define (iter str answer)
    (if (equal? "" (substring str 0))
        answer
        (iter (substring str 1) (string-append answer (morse_code_list (- (char->integer (char-upcase (string-ref str 0))) 65))))))
  (iter str ""))
  