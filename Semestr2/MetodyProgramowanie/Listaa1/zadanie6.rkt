#lang racket
;(or (and (ifCond) ifTrue) ifFalse)
;why? (and) will return last value if ifCond is true -> ifTrue
; then we got (or ifTrue ifFalse)
; or will return first value that is not #f hence it will be ifTrue
; now, if ifCond is false then (and) will return it
; (or ifCond ifFalse) -> (or #f ifFalse) -> ifFalse
(or (and (< 3 4) 1) 0) 