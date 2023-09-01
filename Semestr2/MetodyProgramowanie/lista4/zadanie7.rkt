#lang racket

(define empty-queue (cons '() '()))  ; pusta kolejka
(define (empty? q) (null? (car q))) ; czy kolejka jest pusta?
(define (push-back x q) 
  (if (null? (car q)) 
      (cons (list x) '())
      (cons (car q) (cons (cons x (cdr q)) '())))) ; dodaj element na koniec kolejki
(define (front q) 
  (if (null? (car q)) 
      (car (reverse (cdr q)))
      (car (car q)))) ; podejrzyj element na początku kolejki 
(define (pop q) 
  (if (null? (car q))
      (cons '() (reverse (cdr q)))
      (cons (cdr (car q)) (cdr q)))) ; zdejmij element z przodu kolejki

;Implementacja wykorzystuje parę list q, z których pierwsza reprezentuje prefiks kolejki, a druga
;sufiks w odwróconej kolejności. Jeśli pierwsza lista jest pusta, to znaczy że kolejka jest pusta,
;w przeciwnym przypadku możemy odczytać pierwszy element kolejki z pierwszej listy (car (car q)).
;Dodawanie elementu na koniec kolejki polega na dokładaniu go na przód drugiej listy (cons x (cdr q))
;i zastępowaniu pierwszej listy odwróconą drugą listą ((cons (reverse (cdr q)) '())).

;Usuwanie elementu z przodu kolejki polega na usunięciu pierwszego elementu z pierwszej listy (cdr (car q)) i
;zwróceniu pary list z zaktualizowanymi wartościami ((cons (cdr (car q)) (cdr q))). Jeśli pierwsza lista jest pusta,
;to znaczy że usunięcie elementu spowodowałoby, że pierwsza lista stałaby się pusta i musimy zastąpić ją
;odwróconą drugą listą ((cons '() (reverse (cdr q)))).