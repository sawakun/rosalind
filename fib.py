def fib(n, k):
        if n <= 2:
                return 1
        else: 
                return fib(n-1, k) + fib(n-2, k)*k

n= 32
k = 5
print fib(n,k)
