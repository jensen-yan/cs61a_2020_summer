(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cddr s))
)


(define (sign num)
  'YOUR-CODE-HERE
  (cond ((< num 0) -1)
    ((= num 0) 0)
    (else 1)
  )
)


(define (square x) (* x x))

(define (pow x y)
  'YOUR-CODE-HERE
  (cond ((= y 0) 1)
    ((= y 1) x)
    ((even? y) (square (pow x (/ y 2))))
    (else (* x (square (pow x (/ (- y 1) 2))) ))
  )
)


(define (unique s)
  'YOUR-CODE-HERE
  (if (null? s)  nil
    (cons (car s) 
      (filter  
          (lambda (x) (not (equal? (car s) x)) )
          (unique (cdr s))
      ) 
    )
  )
)


(define (replicate x n)
  'YOUR-CODE-HERE
  ; (if (= n 0)
  ;   nil
  ;   (cons x (replicate x (- n 1)) )
  ; )
  (define (replicate-tail n lst)
    (if (= n 0)
      lst
      (replicate-tail (- n 1) (cons x lst))  
    )
  )
  (replicate-tail n nil)
)


(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
  (if (= n 0)
    start
    (combiner
      (term n)
      (accumulate combiner start (- n 1) term)
    )   
  )
)


(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
  (define (accumulate-helper n result)
    (if (= n 0)
      result
      (accumulate-helper (- n 1) (combiner (term n) result))
    )
  )
  (accumulate-helper n start)
)


(define-macro (list-of map-expr for var in lst if filter-expr)
  'YOUR-CODE-HERE
  `(map 
    (lambda (,var) ,map-expr) 
    (filter 
      (lambda (,var) ,filter-expr) 
      ,lst
    ))
)

