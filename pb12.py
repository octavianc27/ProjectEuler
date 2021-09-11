def ndiv(n):
    ct=0
    for i in range(1,int(n**0.5+1)):
        if n%i==0:
            ct+=2
        if i*i==n:
            ct-=1
    return ct

def tri_number(n):
    return int(n*(n+1)/2)

i=0
while(ndiv(tri_number(i))<500):
    i+=1
    
print(tri_number(i))