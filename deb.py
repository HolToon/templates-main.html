def f():
    global m
    global n
    if n != 0:
        m += 1
        n -= 1
        return f()
m, n = list(map(int, input().split()))
f()
print(m)