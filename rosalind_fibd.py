def fib(n, m):
  if m <= 0:
    return 1
  elif n <= 2:
    return 1
  else: 
    return fib(n-1, m-1) + fib(n-2, m-2)

n = 6
m = 3
#n = 81 
#m = 20

print fib(n,m)
