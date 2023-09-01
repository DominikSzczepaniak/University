#lang racket

; EXP -> EXP tier3op P | P 
; P -> P tier2op M | M
; M -> M tier1op X | X
; X -> F B | B
; B -> NUMBER | (EXP) | (-NUMBER)
; tier3op -> - | +
; tier2op -> * | /
; tier1op -> ^
; F -> !

; 2+2+4*7^4*5
; EXP -> EXP tier3op P -> EXP tier3op P tier3op P -> NUMBER + NUMBER + P tier2op M -> 2+2 + P * M tier1op X -> 2 + 2 + 4 * 7 ^ EXP ->
; 2 + 2 + 4 * 7 ^ P -> 2 + 2 + 4 * 7 ^ P tier2op M -> 2 + 2 + 4 * 7 ^ NUMBER * NUMBER -> 2 + 2 + 4 * 7 ^ 4 * 5










