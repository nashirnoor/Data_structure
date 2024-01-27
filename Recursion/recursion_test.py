def fact(n):
    if n<=1:
        return 1
    else:
        return n* fact(n-1)
    
d = fact(5)
print(d)