#lang racket

(provide
 twlist?
 twlist-nonempty?
 (contract-out
   [twlist-empty? (-> twlist? boolean?)]
   [make-twlist   (-> any/c twlist?)]
   [twlist-push-back   (-> twlist? any/c void?)]
   [twlist-push-front  (-> twlist? any/c void?)]
   [twlist-popfront    (-> twlist? void?)]
   [twlist-popback   (-> twlist? void?)]
   [first-elem       (-> twlist? any/c)]
   [last-elem        (-> twlist? any/c)]))

(struct twlist 
  ([previous]
   [elem]
   [next]) #:transparent #:mutable)

(define (twlist-empty? ls)
  (if (null? (twlist-elem ls))
      #t
      #f))

(define (empty-twlist) (twlist null null null))

(define (twlist-nonempty? ls)
  (not (twlist-empty? ls)))

(define (make-twlist elem)
  (twlist null elem null))

(define (twlist-push-back ls x)
  (if (twlist-empty? ls)
      (let ((update-elem (set-twlist-elem! ls x)))
        (set-twlist-previous! ls ls))
      (let ((last-twlist (twlist-previous ls)))
        (let ((update-next (set-twlist-next! last-twlist (make-twlist x)))
              (update-previous-newlast (set-twlist-previous! (twlist-next last-twlist) last-twlist)))
          (set-twlist-previous! ls (twlist-next last-twlist))))))

(define (twlist-push-front ls x) 
  (if (twlist-empty? ls)
      (let ((change-value (set-twlist-elem! ls x)))
        (set-twlist-previous! ls ls))
      (let ((old-value (twlist-elem ls))
            (old-next (twlist-next ls)))
        (let ((change-next (set-twlist-next! ls (twlist ls old-value old-next)))
              (change-previous-of-next-next (set-twlist-previous! (twlist-next (twlist-next ls)) (twlist-next ls))))
        (set-twlist-elem! ls x)))))
            

(define (twlist-popfront ls) 
  (if (twlist-empty? ls)
      (error "List is empty")
      (let ((next (twlist-next ls)))
        (if (null? next) ;length == 1
            (let ((change-elem (set-twlist-elem! ls null))
                  (change-next (set-twlist-next! ls null)))
              (set-twlist-previous! ls null))
            (let ((next-next (twlist-next next)))
              (if (null? next-next) ;length==2
                  (let ((change-elem2 (set-twlist-elem! ls (twlist-elem next))))
                        (set-twlist-next! ls null))
                  (let ((new-value (twlist-elem next))
                        (new-next next-next)
                        (next-next-new-previous ls))
                    (let ((change-new-value (set-twlist-elem! ls new-value))
                          (change-new-next (set-twlist-next! ls new-next)))
                          (set-twlist-previous! next-next next-next-new-previous)))))))))
      

(define (twlist-popback ls)
  (if (twlist-empty? ls)
      (error "List is empty")
      (let ((update-previous-of-first (set-twlist-previous! ls (twlist-previous (twlist-previous ls)))))
        (set-twlist-next! (twlist-previous ls) null))))

(define (first-elem ls)
  (twlist-elem ls))

(define (last-elem ls)
  (twlist-elem (twlist-previous ls))) 
              
(define x (empty-twlist))
(twlist-push-back x 5)
(twlist-push-back x 7)