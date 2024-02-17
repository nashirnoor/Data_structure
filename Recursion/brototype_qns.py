def f(n):
    if n<=1:
        return
    f(n-1)
    print(n,end=" ")
    f(n-1)

f(5)