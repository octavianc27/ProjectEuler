from common import prime_factors
i=0
s=0
def ndiv(n):
    ct=0
    for i in range(1,n+1):
        if n%i==0:
            ct+=1
    return ct

while True:
    i+=1
    s+=i
    print(primef)