(define ones (cons-stream 1 ones))
; (define int-stream (cons-stream ones int-stream))

(define (map-stream f s)
    (if (null? s)
        nil
        (cons-stream (f (car s))
            (map-stream f (cdr-stream s)))))

(define (filter-stream f s)
    (if (null? s)
        nil
        (if (f (car s))
            (cons-stream (car s) 
                (filter-stream f (cdr-stream s)))
            (filter-stream f (cdr-stream s))))

(define (reduce-stream f s start)
    (if (null? s)
        start
        (reduce-stream f (cdr-stream s)
            (f (car s) start))))

(define (sieve s)
    (cons-stream (car s)
        (sieve
        (filter-stream 
            (lambda (x) (not (=  0 (remainder x (car s)))))
            (cdr-stream s)))))

(define primes (sieve (int-stream 2)))