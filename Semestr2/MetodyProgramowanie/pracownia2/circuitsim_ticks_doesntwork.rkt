#lang racket

(require rackunit)
(require data/heap)
(provide sim? wire?
         (contract-out
          [make-sim        (-> sim?)] ;done
          [sim-wait!       (-> sim? positive? void?)] ;most prob done
          [sim-time        (-> sim? real?)] ;done
          [sim-add-action! (-> sim? positive? (-> any/c) void?)] ;done

          [make-wire       (-> sim? wire?)] ;done
          [wire-on-change! (-> wire? (-> any/c) void?)] ;to change?
          [wire-value      (-> wire? boolean?)] ;to change?
          [wire-set!       (-> wire? boolean? void?)] ;to change?

          [bus-value (-> (listof wire?) natural?)] ;done
          [bus-set!  (-> (listof wire?) natural? void?)] ;done

          [gate-not  (-> wire? wire? void?)] ;done
          [gate-and  (-> wire? wire? wire? void?)] ;done
          [gate-nand (-> wire? wire? wire? void?)] ;done
          [gate-or   (-> wire? wire? wire? void?)];done
          [gate-nor  (-> wire? wire? wire? void?)];done
          [gate-xor  (-> wire? wire? wire? void?)];done

          [wire-not  (-> wire? wire?)];done
          [wire-and  (-> wire? wire? wire?)];done
          [wire-nand (-> wire? wire? wire?)];done
          [wire-or   (-> wire? wire? wire?)];done
          [wire-nor  (-> wire? wire? wire?)];done
          [wire-xor  (-> wire? wire? wire?)];done

          [flip-flop (-> wire? wire? wire? void?)]));done

; ==============================
; event struct & methods

(struct event (time operation))

(define (event<=? e1 e2)
  (if (<= (event-time e1) (event-time e2))
      e1
      e2))
; ==============================
; sim struct & methods
(struct sim (eventq time) #:transparent #:mutable)

(define (make-sim)
  (sim (make-heap event<=?) 0))

(define (sim-wait! s t)
  (define (func s endt)
    (if (= (sim-time s) endt)
        (void)
        (if (= (heap-count (simq s)) 0)
            (set-sim-time! s endt)
            (if (<= (event-time (heap-min (simq s))) endt)
                (let ((event-heap (heap-min (simq s))))
                  (begin
                    (heap-remove-min! (simq s))
                    ((event-operation event-heap))
                    (set-sim-time! s (event-time event-heap))
                    (func s endt)))
            (set-sim-time! s endt)))))
  
  (if (= 0 (heap-count (simq s)))
      (set-sim-time! s (+ (sim-time s) t))
      (func s (+ (sim-time s) t))))
  
(define (simq s)
  (sim-eventq s))

(define (sim-add-action! s t f)
  (heap-add! (simq s) (event (+ (sim-time s) t) f)))

; ==============================
; wire struct & methods

(struct wire (val sim events) #:mutable #:transparent)

(define (make-wire s)
  (wire #f s null))

(define (wire-on-change! w f)
  (set-wire-events! w (append (wire-events w) (list f))))

(define (wire-value w) 
  (wire-val w))

(define (wire-set! w value)
  (begin
    (set-wire-val! w value)
    (do-wire-events w)))

(define (do-wire-events w)
  (define (iter event-list)
    (if (null? event-list)
        (void)
        (begin
          ((first event-list))
          (iter (rest event-list)))))
  (iter (wire-events w)))

; ===================================
(define xor (lambda (x y) (if (boolean=? x y) #f #t)))

; ==============================
; GATES

(define (gate-not outW w1)
  (begin
    (sim-add-action! (wire-sim outW) 1 (lambda () (wire-set! outW (not (wire-value w1)))))
    (wire-on-change! w1 (lambda () (sim-add-action! (wire-sim outW) 1 (lambda () (wire-set! outW (not (wire-value w1)))))))))

(define (gate-and outW w1 w2)
  (begin 
    (sim-add-action! (wire-sim outW) 1 (lambda () (wire-set! outW (and (wire-value w1) (wire-value w2)))))
    (wire-on-change! w1 (lambda () (sim-add-action! (wire-sim outW) 1 (lambda () (wire-set! outW (and (wire-value w1) (wire-value w2)))))))
    (wire-on-change! w2 (lambda () (sim-add-action! (wire-sim outW) 1 (lambda () (wire-set! outW (and (wire-value w1) (wire-value w2)))))))))

(define (gate-nand outW w1 w2)
  (begin 
    (sim-add-action! (wire-sim outW) 1 (lambda () (wire-set! outW (not (and (wire-value w1) (wire-value w2))))))
    (wire-on-change! w1 (lambda () (sim-add-action! (wire-sim outW) 1 (lambda () (wire-set! outW (not (and (wire-value w1) (wire-value w2))))))))
    (wire-on-change! w2 (lambda () (sim-add-action! (wire-sim outW) 1 (lambda () (wire-set! outW (not (and (wire-value w1) (wire-value w2))))))))))

(define (gate-or outW w1 w2)
  (begin 
    (sim-add-action! (wire-sim outW) 1 (lambda () (wire-set! outW (or (wire-value w1) (wire-value w2)))))
    (wire-on-change! w1 (lambda () (sim-add-action! (wire-sim outW) 1 (lambda () (wire-set! outW (or (wire-value w1) (wire-value w2)))))))
    (wire-on-change! w2 (lambda () (sim-add-action! (wire-sim outW) 1 (lambda () (wire-set! outW (or (wire-value w1) (wire-value w2)))))))))

(define (gate-nor outW w1 w2)
  (begin 
    (sim-add-action! (wire-sim outW) 1 (lambda () (wire-set! outW (not (or (wire-value w1) (wire-value w2))))))
    (wire-on-change! w1 (lambda () (sim-add-action! (wire-sim outW) 1 (lambda () (wire-set! outW (not (or (wire-value w1) (wire-value w2))))))))
    (wire-on-change! w2 (lambda () (sim-add-action! (wire-sim outW) 1 (lambda () (wire-set! outW (not (or (wire-value w1) (wire-value w2))))))))))

(define (gate-xor outW w1 w2)
  (begin 
    (sim-add-action! (wire-sim outW) 2 (lambda () (wire-set! outW (xor (wire-value w1) (wire-value w2)))))
    (wire-on-change! w1 (lambda () (sim-add-action! (wire-sim outW) 2 (lambda () (wire-set! outW (xor (wire-value w1) (wire-value w2)))))))
    (wire-on-change! w2 (lambda () (sim-add-action! (wire-sim outW) 2 (lambda () (wire-set! outW (xor (wire-value w1) (wire-value w2)))))))))

; ==============================
; WIRE LOGIC

(define (wire-not w)
  (let* ((outW (make-wire (wire-sim w)))
        (wykonaj (gate-not outW w)))
    outW))

(define (wire-and w1 w2)
  (let* ((outW (make-wire (wire-sim w1)))
        (wykonaj (gate-and outW w1 w2)))
    outW))

(define (wire-nand w1 w2)
  (let* ((outW (make-wire (wire-sim w1)))
        (wykonaj (gate-nand outW w1 w2)))
    outW))

(define (wire-or w1 w2)
  (let* ((outW (make-wire (wire-sim w1)))
        (wykonaj (gate-or outW w1 w2)))
    outW))

(define (wire-nor w1 w2)
  (let* ((outW (make-wire (wire-sim w1)))
        (wykonaj (gate-nor outW w1 w2)))
    outW))

(define (wire-xor w1 w2)
  (let* ((outW (make-wire (wire-sim w1)))
        (wykonaj (gate-xor outW w1 w2)))
    outW))

; ==============================
; SCHEMA:

(define (bus-set! wires value)
  (match wires
    ['() (void)]
    [(cons w wires)
     (begin
       (wire-set! w (= (modulo value 2) 1))
       (bus-set! wires (quotient value 2)))]))

(define (bus-value ws)
  (foldr (lambda (w value) (+ (if (wire-value w) 1 0) (* 2 value)))
         0
         ws))

(define (flip-flop out clk data)
  (define simt (wire-sim data))
  (define w1  (make-wire simt)) ;#f
  (define w2  (make-wire simt)) ;#f
  (define w3  (wire-nand (wire-and w1 clk) w2))
;                   #t       #f    #f #t   #f
  (gate-nand w1 clk (wire-nand w2 w1)) ;#f
  (gate-nand w2 w3 data) ;#t
  (gate-nand out w1 (wire-nand out w3)))
;            #t  #f       #t   #f  #t



;========================================
;testing

(define st (make-sim))
(define wire_test1 (make-wire st))
(define wire_test2 (make-wire st))
(define wire_test3 (make-wire st))
(wire-set! wire_test1 #f)
(wire-set! wire_test2 #f)
(wire-set! wire_test3 #f)
(flip-flop wire_test1 wire_test2 (wire-xor wire_test3 wire_test1))
(sim-wait! st 15)




;(define w1 (make-wire st))
;(define w2 (make-wire st))
;(define w3 (wire-xor (wire-nand (wire-and w1 w1) w2) w1))
;(define ch (make-wire st))
;(define (functest ch)
;  (define w4 (make-wire st))
;  (gate-and w4 w1 w2) ;#t
;  (gate-and w2 (wire-and w4 w1) w1) ;#t
;  (gate-and ch w2 w4)) ;#t
;(sim-wait! st 4)
;(check-equal? (wire-value w3) (xor (not (and (and (wire-value w1) (wire-value w1)) (wire-value w2))) (wire-value w1)))
;(wire-set! w2 #t)
;(sim-wait! st 4)
;(check-equal? (wire-value w3) (xor (not (and (and (wire-value w1) (wire-value w1)) (wire-value w2))) (wire-value w1)))
;(wire-set! w2 #f)
;(sim-wait! st 4)
;(check-equal? (wire-value w3) (xor (not (and (and (wire-value w1) (wire-value w1)) (wire-value w2))) (wire-value w1)))
;(wire-set! w2 #t)
;(wire-set! w1 #t)
;(sim-wait! st 40)
;(functest ch)
;(sim-wait! st 40)
;(check-equal? (wire-value ch) #t)
;(wire-set! w1 #f)
;(sim-wait! st 40)
;(check-equal? (wire-value ch) #f)







(define simtest (make-sim))

(define (make-counter n clk en)
  (if (= n 0)
      '()
      (let [(out (make-wire simtest))] 
        (flip-flop out clk (wire-xor en out)) 
        (cons out (make-counter (- n 1) clk (wire-and en out))))))

;2:
;out-> #f [n=2:(wire-xor en out)] [n2-1:(wire-and en out)]
;clk-> #f null
;en-> #f [n=2:(wire-xor en out)] [n2-1:(wire-and en out)]
;out #f -> #f
;(cons out (make-counter 1 clk (wire-and en out))))
;1:
;out: #f [n=1:(wire-xor en out)] [n1-0:(wire-and en out)]
;clk: #f
;en: #f

;answer: (cons  #f [n=2:(wire-xor en out)] [flip-flopn2:(wire-nand out w3)]  [n2-1:(wire-and en out)]
;               #f [n=1:(wire-xor en out)] [flip-flopn1:(wire-nand out w3)]  [n1-0:(wire-and en out)])

;clk -> [flip-flop2  (wire-and w1 clk)] [flip-flop2 (gate-nand w1 clk (wire-nand w2 w1))]
      ; [flip-flop1  (wire-and w1 clk)] [flip-flop1 (gate-nand w1 clk (wire-nand w2 w1))]

;if clk updates then w1 updates and then out updates. but if out updates our cons doesnt so thats the problem
;how to solve? join flip flop into one-liner and then ?we return big wire?

;what if we update when getting value?
;will it know which subwires to go to?

; WORKS ^ try to do this?
; PROBLEM: sim-wait!. Now instead of going front to back we go back to front, so we might not do some events
; in good order

; add events for calculating as new list? we wont need to care about sim-wait! because if some event was not
; done till here then we will get old answer, which is good for us i guess

(define sstest (make-sim))
(define wire_test2_3 (make-wire sstest))
(wire-set! wire_test2_3 #t)
(define wir (make-wire sstest))
(wire-set! wir #t)
(define (testfunc w)
  (define wire_test2_1 (make-wire sstest))
  (define wire_test2_2 (make-wire sstest))
  (wire-on-change! wire_test2_3 (lambda () (wire-set! wir (xor (wire-value wire_test2_1) (wire-value wire_test2_2))))))
(testfunc wire_test2_3)
(do-wire-events wire_test2_3)


(define clk (make-wire simtest))
(define en  (make-wire simtest))
(define counter (make-counter 2 clk en))
; counter  = #f #f #f #f
(wire-set! en #t)
;when counter gets to either #t#t#f#f or #t#t#t#t value doesnt change anymore

; Kolejne wywołania funkcji tick zwracają wartość licznika
; w kolejnych cyklach zegara. Licznik nie jest resetowany,
; więc początkowa wartość licznika jest trudna do określenia
(define (tick) ;doesnt change value :/
  (wire-set! clk #t)
  (sim-wait! simtest 20)
  (wire-set! clk #f)
  (sim-wait! simtest 20)
  (display counter)
  (bus-value counter))


