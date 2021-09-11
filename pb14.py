def collatz_len(n):
    ct = 1
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n+1
        ct += 1
    return ct


len_max = i_max = 0
for i in range(1, 1000001):
    current_len = collatz_len(i)
    if current_len > len_max:
        len_max = current_len
        i_max = i

print(i_max)
