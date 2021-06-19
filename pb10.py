import sympy as sp

s=sp.sieve.primerange(1,2_000_000)
print(sum(list(s)))