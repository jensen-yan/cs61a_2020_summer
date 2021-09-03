(define (fact n)
     (if (= n 0) 1 (* n (fact (- n 1)))))

(define (fact-exp n)
     (if (= n 0) 1 (list '* n (fact-exp (- n 1)))))

(define (fib n)
    (if (<= n 1)
        n
        (+ (fib (- n 2)) (fib (- n 1)))))

(define (fib-exp n)
    (if (<= n 1)
        n
        (list '+ (fib-exp (- n 2)) (fib-exp (- n 1)))))

(define-macro (twice expr)
    (list `begin expr expr))

(define (check val)
    (if val 'passed 'failed))

; (define x -2)

(define-macro (check2 expr)
    (list 'if expr ''passed 
      (list 'quote (list 'failed: expr) )))

(define (map fn vals)
    (if (null? vals)
        ()
        (cons (fn (car vals))
              (map fn (cdr vals))
         )))

(define-macro (for sym vals expr)
    (list 'map  (list `lambda (list sym) expr)  vals)    
)
; (for x `(1 2 3 4) (* x x))
(define-macro (for sym vals expr)
    `(map (lambda (,sym) ,expr) ,vals)
)