(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
    (map (lambda (rest) (cons first rest))  rests)
  )

(define (zip pairs)
  (list (map car pairs) (map cadr pairs))
)

;; Problem 16
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 16
  (define (helper s id)
    (if (null? s)
      s
      (cons (list id (car s)) (helper (cdr s) (+ id 1)) )
    )
  )
  (helper s 0)
  )
  ; END PROBLEM 16

;; Problem 17
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 17
  (cond ((null? denoms) `())
    ((= total 0) `())
    ; total = denoms0， 选上denoms0作为一种情况，再看不要denoms0的其他情况
    ((= total (car denoms)) (cons (list total) (list-change total (cdr denoms))))
    ; total < denoms0, 看其他denoms行不行
    ((< total (car denoms)) (list-change total (cdr denoms)))
    ; total > denoms0: 两种情况： 选上denoms0， 不选denoms0， 分别递归
    (else  (append (cons-all (car denoms) 
                    (list-change (- total (car denoms)) denoms) )  
              (list-change total (cdr denoms))
              ))
  )
  )
  ; END PROBLEM 17

;; Problem 18
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 18
         expr
         ; END PROBLEM 18
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 18
         expr
         ; END PROBLEM 18
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           (append (list form params) (map let-to-lambda body))
           ; END PROBLEM 18
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           (define form (car (zip values)))
           (define params (map let-to-lambda (cadr (zip values))))
           (define body (map let-to-lambda body))
           (cons (append (list 'lambda form) body) params)
          ;  `((lambda ,(car (zip values)) ,(car body))  ,(cadr (zip values)))
           ; END PROBLEM 18
           ))
        (else
         ; BEGIN PROBLEM 18
         (map let-to-lambda expr)
         ; END PROBLEM 18
         )))