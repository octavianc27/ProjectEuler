n=600851475143

for i in range(2,n):
    if n%i==0:
        n=int(n/i)
        print(f'{i}, {n}')
    if n==1:
        break