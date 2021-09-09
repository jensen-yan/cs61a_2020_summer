
(define-macro (def func args body)
    `(define ,func (lambda ,args ,body))   
)


(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define-macro ones cons)

(define all-three-multiples
    (cons-stream 3 
      (map-stream (lambda (x) (+ x 3)) all-three-multiples ))
)


(define (compose-all funcs)
  (lambda (x) 
    (if (null? funcs)
      x
      ((compose-all (cdr funcs)) ((car funcs) x)  ) ))
)


(define (partial-sums stream)
  (define (helper sum-so-far stream-remaining)
    (if (null? stream-remaining)
      nil
      (begin (define new-sum (+ sum-so-far (car stream-remaining)))
          (cons-stream new-sum 
              (helper new-sum (cdr-stream stream-remaining))))))
  (helper 0 stream)
)

