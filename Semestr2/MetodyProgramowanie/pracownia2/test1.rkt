#lang racket
(require "circuitsim.rkt")
;(require "circuitsum_not_working_faster.rkt")
(require rackunit)
(define make_true (make-sim))
(define wire_A0 (make-wire make_true)) ;0 #f #f
(define wire_A1 (make-wire make_true)) ;0 #f #t
(define wire_A2 (make-wire make_true)) ;0 #f #f
(define wire_A3 (make-wire make_true)) ;0 #f #t
(define wire_A4 (make-wire make_true)) ;0 #f #t
(define wire_A5 (make-wire make_true)) ;0 #f #t
(define wire_B0 (wire-not wire_A2)) ;1 #t #t
(define wire_B1 (wire-and wire_A1 wire_B0)) ;2 #f #t
(define wire_B2 (wire-and wire_A3 wire_A4)) ;1 #t #t
(define wire_B3 (wire-and wire_A0 wire_B1)) ;3 #t #f
(define wire_B4 (wire-and wire_B0 wire_B2)) ;2 #t #t
(define wire_B5 (wire-and wire_B2 wire_A5)) ;2 #f #t
(define wire_B6 (wire-not wire_B3)) ;4 #f #t
(define wire_B7 (wire-and wire_B1 wire_B6)) ;5 #t #t
(define wire_B8 (wire-and wire_B4 wire_B5)) ;3 #f #t
(define wire_output (wire-and wire_B7 wire_B8)) ;6 #f #t
(sim-wait! make_true 20)
(check-equal? (wire-value wire_output) #f)
(wire-set! wire_A1 #t)
(wire-set! wire_A3 #t)
(wire-set! wire_A4 #t)
(wire-set! wire_A5 #t)
(sim-wait! make_true 20)
(check-equal? (wire-value wire_output) #t)
