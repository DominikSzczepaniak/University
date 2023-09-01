#lang plait

;(map f (map g xs)) = (map f (list (g xs[0]) (g xs[1]) ... (g xs[n])) = (list (f (g xs[0])) (f (g xs[1])) ... (f (g xs[n])))
;(map (lambda (x) (f (g x)) xs)
;lambda (x) gets every element of xs as x in order
; so first x = xs[0]
; second x = xs[1]
; ...
; (map (lambda (x) (f (g x)) xs) = (list (f (g xs[0])) (f (g xs[1])) (f (g xs[2])) ... (f (g xs[3])) = (map f (map g xs))  