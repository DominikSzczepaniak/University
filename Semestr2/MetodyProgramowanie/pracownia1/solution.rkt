#lang racket
(require rackunit)

(provide (struct-out column-info)
         (struct-out table)
         (struct-out and-f)
         (struct-out or-f)
         (struct-out not-f)
         (struct-out eq-f)
         (struct-out eq2-f)
         (struct-out lt-f)
         table-insert
         table-project
         table-sort
         table-select
         table-rename
         table-cross-join
         table-natural-join)

(define-struct column-info (name type) #:transparent)

(define-struct table (schema rows) #:transparent)

(define cities
  (table
   (list (column-info 'city    'string)
         (column-info 'country 'string)
         (column-info 'area    'number)
         (column-info 'capital 'boolean))
   (list (list "Wrocław" "Poland"  293 #f)
         (list "Warsaw"  "Poland"  517 #t)
         (list "Poznań"  "Poland"  262 #f)
         (list "Berlin"  "Germany" 892 #t)
         (list "Munich"  "Germany" 310 #f)
         (list "Paris"   "France"  105 #t)
         (list "Rennes"  "France"   50 #f))))

(define countries
  (table
   (list (column-info 'country 'string)
         (column-info 'population 'number))
   (list (list "Poland" 38)
         (list "Germany" 83)
         (list "France" 67)
         (list "Spain" 47))))

(define (empty-table columns) (table columns '()))

;====================================================================================
; Wstawianie

(define (table-insert row tab)
  (define (check-length row tab)
    (if (= (length row) (length (table-schema tab)))
        #t
        (error "Zła ilość komórek")))
  (define t1 (check-length row tab))
  (define (check-type row tab-schema)
    (if (null? row)
        #t
        (cond
          [(equal? (column-info-type (first tab-schema)) 'string)
           (if (string? (first row))
               (check-type (rest row) (rest tab-schema))
               (error "Zly typ jakiejs komorki"))]
          [(equal? (column-info-type (first tab-schema)) 'number)
           (if (number? (first row))
               (check-type (rest row) (rest tab-schema))
               (error "Zly typ jakiejs komorki"))]
          [(equal? (column-info-type (first tab-schema)) 'boolean)
           (if (boolean? (first row))
               (check-type (rest row) (rest tab-schema))
               (error "Zly typ jakiejs komorki"))]
          [(equal? (column-info-type (first tab-schema)) 'symbol)
           (if (symbol? (first row))
               (check-type (rest row) (rest tab-schema))
               (error "Zly typ jakiejs komorki"))])))
  (define t2 (check-type row (table-schema tab)))
  (table (table-schema tab) (append (list row) (table-rows tab) )))

(check-equal?
 (table-insert (list "Rzeszow" "Poland" 129 #f) cities)
 (table
 (list
  (column-info 'city 'string)
  (column-info 'country 'string)
  (column-info 'area 'number)
  (column-info 'capital 'boolean))
 '(("Rzeszow" "Poland" 129 #f)
   ("Wrocław" "Poland" 293 #f)
   ("Warsaw" "Poland" 517 #t)
   ("Poznań" "Poland" 262 #f)
   ("Berlin" "Germany" 892 #t)
   ("Munich" "Germany" 310 #f)
   ("Paris" "France" 105 #t)
   ("Rennes" "France" 50 #f))))

;====================================================================================
; Projekcja

(define (exist-column-name col tab)
  (define (iter tab)
    (if (null? tab)
        #f
        (if (equal? col (column-info-name (first tab)))
            #t
            (iter (rest tab)))))
  (iter (table-schema tab)))
        
(define (col-positions cols tab xs)
  (define (col-position col tab val)
    (if (null? tab)
        null
        (if (equal? col (column-info-name (first tab)))
            val
            (col-position col (rest tab) (+ 1 val)))))
  (if (null? cols)
      xs
      (col-positions (rest cols) tab (cons (col-position (first cols) (table-schema tab) 0) xs))))


(define (table-project cols tab)
  (define (check-tab-is-table tab)
    (if (null? tab)
        (error "tab nie jest tablica")
        #t))
  (define checking-tab-is-table (check-tab-is-table tab))
  (define (check-exist cols tab)
    (if (null? cols)
        #t
        (if (equal? #t (exist-column-name (first cols) tab))
            (check-exist (rest cols) tab)
            #f)))
  (define existing_columns (check-exist cols tab))
  (define positions (col-positions cols tab '()))
  (define (add-solutions tab positions)
    (define (iter-rows val tab-values positions xs)
      (define sizeOfTab-values (length tab-values))
      (define (iter-columns val row newpositions listt)
        (if (null? newpositions)
            listt    
            (iter-columns (- val 1) row (cdr newpositions) (append (list (list-ref row (car newpositions))) listt))))
      (if (null? tab-values)
          xs
          (iter-rows (+ 1 val) (rest tab-values) positions (append xs (list (iter-columns (- sizeOfTab-values 1) (first tab-values) positions (list)))))))
    (iter-rows 0 (table-rows tab) positions (list)))
  (define (add-schema tab positions)
    (define (iter tab-schema newpositions xs)
      (if (null? newpositions)
          xs
          (iter tab-schema (cdr newpositions) (append xs (list (list-ref tab-schema (car newpositions)))))))
    (iter (table-schema tab) positions '()))
  (define tablerows (add-solutions tab positions))
  (define tableschema (add-schema tab positions))
  (if (null? cols)
      (table null null)
      (if (equal? #f existing_columns)
          (error "Jedna z nazw kolumn nie istnieje w tej tabeli")
          ;positions)))
          (table (reverse tableschema) tablerows))))


(check-equal? (table-project '(city country) cities) (table
 (list
  (column-info 'city 'string)
  (column-info 'country 'string))
 (list
  (list "Wrocław" "Poland")
  (list "Warsaw" "Poland")
   (list "Poznań" "Poland")
   (list "Berlin" "Germany")
   (list "Munich" "Germany")
   (list "Paris" "France")
   (list "Rennes" "France"))))
;====================================================================================
; Sortowanie
(define (procedure-type type)
  (cond
    [(equal? type 'number) <]
    [(equal? type 'string) string<?]
    [(equal? type 'boolean) (lambda (x y) (and y (not x)))]
    [(equal? type 'symbol) symbol<?]))

(define (schema-type col tab-schema)
  (if (null? tab-schema)
      (error "Nie ma takiej kolumny")
      (if (equal? col (column-info-name (first tab-schema)))
          (column-info-type (first tab-schema))
          (schema-type col (rest tab-schema)))))

(define (schema-val col tab-row tab-schema)
  (if (null? tab-row)
      (error "Nie ma takiej wartosci")
      (if (equal? col (column-info-name (first tab-schema)))
          (first tab-row)
          (schema-val col (rest tab-row) (rest tab-schema)))))

(define (table-compare cols tab-row tab-schema)
  (if (null? cols)
      #f
      (cond
        [(equal? (schema-val (first cols) (first tab-row) tab-schema)
                 (schema-val (first cols) (rest tab-row) tab-schema))
         (table-compare (rest cols) tab-row tab-schema)]
        [else ((procedure-type (schema-type (first cols) tab-schema))
               (schema-val (first cols) (first tab-row) tab-schema)
               (schema-val (first cols) (rest tab-row) tab-schema))])))
          
(define (table-sort cols tab)
  (if (null? cols)
      tab
      (if (cons? cols)
          (table
           (table-schema tab)
           (sort (table-rows tab)
                 (lambda (x y) (table-compare cols (cons x y) (table-schema tab)))))
          (table
           (table-schema tab)
           (sort (table-rows tab)
                 (lambda (x y) (table-compare (list cols) (cons x y) (table-schema tab))))))))
;====================================================================================
; Selekcja

(define-struct and-f (l r))
(define-struct or-f (l r))
(define-struct not-f (e))
(define-struct eq-f (name val))
(define-struct eq2-f (name name2))
(define-struct lt-f (name val))

(define (get-type name tab-schema)
  (if (null? tab-schema)
      (error "blad")
      (if (equal? (column-info-name (first tab-schema)) name)
          (column-info-type (first tab-schema))
          (get-type name (rest tab-schema)))))

(define (check form tab-row tab-schema)
  (cond
    [(and-f? form) (and (check (and-f-l form) tab-row tab-schema) (check (and-f-r form) tab-row tab-schema))]
    [(or-f? form) (or (check (or-f-l form) tab-row tab-schema) (check (or-f-r form) tab-row tab-schema))]
    [(not-f? form) (not (check (not-f-e form) tab-row tab-schema))]
    [(eq-f? form) (equal? (schema-val (eq-f-name form) tab-row tab-schema) (eq-f-val form))]
    [(eq2-f? form) (equal? (schema-val (eq2-f-name form) tab-row tab-schema) (schema-val (eq2-f-name2 form) tab-row tab-schema))]
    [(lt-f? form ) ((procedure-type (get-type (lt-f-name form) tab-schema)) (schema-val (lt-f-name form) tab-row tab-schema) (lt-f-val form))]))

(define (build-select form tab-row tab-schema)
  (if (null? tab-row)
      null
      (if (equal? #t (check form (first tab-row) tab-schema))
          (cons (first tab-row) (build-select form (rest tab-row) tab-schema))
          (build-select form (rest tab-row) tab-schema))))


(define (table-select form tab)
  (table (table-schema tab) (build-select form (table-rows tab) (table-schema tab))))
  

;====================================================================================
; Zmiana nazwy

(define (table-rename col ncol tab) 
  (define (iter-schema col ncol tab-schema i)
    (define (change-schema pos newName tab-schema answer iter-i)
      (if (= iter-i (length tab-schema))
          answer
          (if (= iter-i pos)
              (change-schema pos newName tab-schema (append answer (list (column-info newName (column-info-type (list-ref tab-schema pos))))) (+ 1 iter-i))
              (change-schema pos newName tab-schema (append answer (list (list-ref tab-schema iter-i))) (+ iter-i 1)))))
    (if (= i (length tab-schema))
        tab-schema
        (if (equal? (column-info-name (list-ref tab-schema i)) col)
            (change-schema i ncol tab-schema '() 0)
            (iter-schema col ncol tab-schema (+ i 1)))))
  (table (iter-schema col ncol (table-schema tab) 0) (table-rows tab)))

;====================================================================================
; Złączenie kartezjańskie

(define (join tab-row)
    (if (null? tab-row)
        null
        (cons (append (first (first tab-row)) (second (first tab-row))) (join (rest tab-row)))))

(define (table-cross-join tab1 tab2)
  (if (or (null? (table-rows tab1)) (null? (table-rows tab2)))
      (table (append (table-schema tab1) (table-schema tab2)) (list))
      (table (append (table-schema tab1) (table-schema tab2)) (join (cartesian-product (table-rows tab1) (table-rows tab2))))))

;====================================================================================
; Złączenie naturalne
(define (check-column-value-equal column-name tab-row1 tab-row2 tab1-schema tab2-schema)
  (define (find-id tab-schema i)
    (if (null? tab-schema)
        (error "blad")
        (if (equal? column-name (column-info-name (first tab-schema)))
            i
            (find-id (rest tab-schema) (+ i 1)))))
  (define id-column1 (find-id tab1-schema 0))
  (define id-column2 (find-id tab2-schema 0))
  (if (equal? (list-ref tab-row1 id-column1) (list-ref tab-row2 id-column2))
      #t
      #f))

(define (check-columns columns tab-row1 tab-row2 tab-schema1 tab-schema2)
  (if (null? columns)
      #t
      (if (equal? #t (check-column-value-equal (first columns) tab-row1 tab-row2 tab-schema1 tab-schema2))
          (check-columns (rest columns) tab-row1 tab-row2 tab-schema1 tab-schema2)
          #f)))

(define (intersect l1 l2)
  (define (common)
   (remove-duplicates
    (for/list ((i l1)
           #:when (member i l2))
      i)))
  (define (iter cols answer)
    (if (null? cols)
        answer
        (iter (rest cols) (append answer (list (column-info-name (first cols)))))))
  (iter (common) '()))

(define (add tab1-row tab2-row tab1-schema tab2-schema)
    (if (null? tab2-schema)
        tab1-row
        (if (member (first tab2-schema) tab1-schema)
            (add tab1-row (rest tab2-row) tab1-schema (rest tab2-schema))
            (add (append tab1-row (list (first tab2-row))) (rest tab2-row) tab1-schema (rest tab2-schema)))))
    
(define (decide-addition tab1-row tab2-row tab1-schema tab2-schema)
  (define common-columns (intersect tab1-schema tab2-schema))
  (if (equal? #t (check-columns common-columns tab1-row tab2-row tab1-schema tab2-schema))
      (add tab1-row tab2-row tab1-schema tab2-schema)
      #f))
        
(define (iter-tab2-rows tab1-row tab2-rows tab1-schema tab2-schema answer)
  (if (null? tab2-rows)
      answer
      (if (equal? #f (decide-addition tab1-row (first tab2-rows) tab1-schema tab2-schema))
          (iter-tab2-rows tab1-row (rest tab2-rows) tab1-schema tab2-schema answer)
          (iter-tab2-rows tab1-row (rest tab2-rows) tab1-schema tab2-schema (append answer (list (decide-addition tab1-row (first tab2-rows) tab1-schema tab2-schema)))))))
    
(define (iter-tab1-rows tab1-rows tab2-rows tab1-schema tab2-schema answer)
  (if (null? tab1-rows)
      answer
      (iter-tab1-rows (rest tab1-rows) tab2-rows tab1-schema tab2-schema (append answer (iter-tab2-rows (first tab1-rows) tab2-rows tab1-schema tab2-schema '())))))

(define (table-natural-join tab1 tab2)
  (define (check-tab)
    (if (and (table? tab1) (table? tab2))
        #t
        (error "Podane wejscie to nie tablice")))
  (define t1 (check-tab))
  (define rows (iter-tab1-rows (table-rows tab1) (table-rows tab2) (table-schema tab1) (table-schema tab2) '()))
  (define schema (remove-duplicates (append (table-schema tab1) (table-schema tab2))))
  (if (or (null? (table-rows tab1)) (= 0 (length (intersect (table-schema tab1) (table-schema tab2)))))
      '()
      (table schema rows)))


(define t1 (table (list (column-info 'city    'string)
         (column-info 'country 'string)
         (column-info 'area    'number)
         (column-info 'capital 'boolean))
          (list (list "asd" "asd" 1 #f))))

(define t2 (table (list (column-info 'asd    'string)
         (column-info 'bsf 'number)) '()))

