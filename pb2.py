from functools import cache

@cache
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

i=1
s=0
while fib(i)<=4_000_000:
    if fib(i)%2==0:
        s+=fib(i)
    i+=1

print(s)