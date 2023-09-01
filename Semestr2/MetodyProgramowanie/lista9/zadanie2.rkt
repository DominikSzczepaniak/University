#lang plait

; ok so basically, this exercise is wrong, there are no S-EXP in racket, only in plait
; and then, using ' doesnt create S-exp in plait, its list
; also i cant use , in S-exp because it will cancel type "s-exp" and we get error
; so i can only use . () number/symbol/bool etc. inside s-exp

; exp -> `(s-exp)
; s-exp -> '(s-exp) | ('s-exp . 's-exp) | (s-exp) | s-exp s-exp | value
; value -> number | bool | symbol | char

