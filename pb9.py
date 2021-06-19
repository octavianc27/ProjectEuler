for i in range(1001):
    for j in range(i+1,1001-i):
        k=1000-i-j
        if i<j and j<k:
            if k**2==i**2+j**2:
                print(f"{i},{j},{k}")
                print(i*j*k)