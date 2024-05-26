# https://www.tutorialspoint.com/python/python_generators.htm

def fibonacci(n):
   fibo = []
   a, b = 0, 1
   while True:
      c=a+b
      if c>=n:
         break
      fibo.append(c)
      a, b = b, c
   return fibo

f = fibonacci(10)
for i in f:
   print (i)