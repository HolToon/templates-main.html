
n = int(input())
a = list(map(str, input().split()))
b = [0]
if a[-1] == a[-2]:
    a.pop(-1)
b = a[-1:0:-1]
b.append(a[0])
if ' '.join(b) in ' '.join(a):
    b = [0]
if ' '.join(b[-1:0:-1]) in ' '.join(a):
    for i in range(len(b)-1):
        if b[i] in a:
            b.pop(i)
if b != [0]:
    b.pop(0)
    print(len(b))
print(' '.join(list(map(str, b))))

a = input()
s = a[0]
a = a[-1:0:-1]
a += s
r = []
i = 0
for i in range(len(a)):
    if a[i] != '0':
        r.append(a[i])
    else:
        if a[i - 1] != ' ':
            if a[i - 1] != '0':
                r.append(a[i])
print(''.join(r))

a = list(map(int, input().split()))
i = 0
while i < len(a):
    if len(a) != 1:
        if i != len(a) - 1:
            if a[i+1] != 2 and a[i] == 2:
                a.remove(2)
    i += 1
print(sum(a) // len(a))

A = int(input())
B = int(input())
C = int(input())
ac = A // C
acc = A - (C * ac)
r = (B - acc) - A
res = r // C
res = res // C
print(res + 2)

a = input()
s = a[0]
a = a[-1:0:-1]
a += s
r = 's'
for i in range(len(a)):
    if a[i] != '0':
        r += a[i]
print(r[1:])

l = int(input())
n = int(input())
a = [int(input()) for i in range(n)]
for i in range(len(a)):
    if a[0] == 0:
        a.remove(0)
    elif a[-1] == 0:
        a.pop(-1)
    else:
        break
c = 0
i = 0
while i < len(a):
    if a[i] == 0:
        c += 1
        if c == l:
            a.pop(i)
    elif a[i] == 1:
        c = 0
    i += 1
res = len(a) // l
if len(a) % l != 0:
    res += 1
print(res)

a = list(map(int, input().split()))
i = 0
while i < len(a):
    if len(a) != 1:
        if a[i+1] != 2 and a[i] == 2:
            a.remove(2)
    i += 1
print(sum(a) // len(a))

a = input()
s = a[0]
a = a[-1:0:-1]
a += s
r = 's'
for i in range(len(a)):
    if a[i] != '0':
        r += a[i]
print(r[1:])

l = int(input())
n = int(input())
a = [int(input()) for i in range(n)]
r = a
for i in range(len(a)):
    if a[i] == 1:
        a = a[i:]
        for i in range(len(a)):
            if a[-i-1] == 1:
                a = a[:-i-1]
                a.append(1)
                break
        break
print(a)
i = 3
c = 0
for j in range(len(a)):
    if a[j] == 0:
        c += 1
    else:
        c = 0
    if c == l:
        a.pop(j)
        break
print(a)
# print(a // n)


n = int(input())
a = list(map(str, input().split()))
b = [0]
if a[-1] == a[-2]:
    a.pop(-1)
b = a[-1:0:-1]
b.append(a[0])
if ' '.join(b) in ' '.join(a):
    b = [0]
if b != [0]:
    b.pop(0)
    print(len(b))
print(' '.join(list(map(str, b))))

def f():
    global m
    global n
    if n != 0:
        if n >= 0:
            m += 1
            n -= 1
        else:
            m -= 1
            n += 1
        f()
m, n = list(map(int, input().split()))
f()
print(m)

n = int(input())
a = list(map(str, input().split()))
b = [0]
print(a[5], 'kkk')
for i in range(1, n):
    print(i)
    if a[i] == a[i - 1]:
        a.pop(i)
b = a[-1:0:-1]
b.append(a[0])
if ' '.join(b) in ' '.join(a):
    b = [0]
if b != [0]:
    b.pop(0)
print(' '.join(list(map(str, b))))

n = int(input())
a = [int(input()) for i in range(n)]
m = max(a)
i = 0
while i != m:
    for j in range(len(a)):
        if a[j] > m:
            i += 1
            a[j] -= 1
    m -= 1
print(max(a))


n = int(input())
a = [['-' for j in range(2 * n - 1)] for i in range(2 * n - 1)]
for i in range(n - 1):
    for j in range(n - i):
        a[-j][i] = 0
    for j in range(n - i - 1):
        a[j][-i-1] = 0
for i in range(n):
    a[i][0] = 1
    a[0][i] = 1
for y in range(1, 2 * n - 1):
    for x in range(1, 2 * n - 1):
        if a[y][x] != 0:
            a[y][x] = a[y - 1][x] + a[y][x - 1] + a[y - 1][x - 1]
print(a[-1][-1])

l = int(input())
n = int(input())
a = [int(input()) for i in range(n)]
r = a
for i in range(len(a)):
    if a[i] == 1:
        a = a[i:]
        for i in range(len(a)):
            if a[-i-1] == 1:
                a = a[:-i-1]
                a.append(1)
                break
        break
res = len(a) // l
if len(a) % l > 0:
    res += 1
print(res)

n, m = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(n)]
my = []
p = [0]
for i in range(len(a)):
    m = min(a[i])
    for x in range(len(a[i])):
        if a[i][x] == m:
            break
    for j in range(n):
        my.append(a[j][x])
    if max(my) == m:
        p = [i+1, x+1]
        my = []
print(' '.join(list(map(str, p))))

n = int(input())
a = list(map(str, input().split()))
b = []
for i in a:
    b.insert(0, i)
l = 1
for i in range(len(b)-1):
    i += 1
    if b[i] == b[i-1]:
        l += 1
b = b[l:]
print(len(b))
print(' '.join(b))

n = int(input())
a = [['0' for j in range(n)] for i in range(n)]

b = n // 2
a[0][b] = '1'
c = 1
x = b + 1
y = -1
while c != 9:
    c += 1
    y1 = y
    x1 = x
    if x == n:
        x = 0
        if (x == n and y == -n - 1) or a[x][y] != '0':
            x -= 1
            y += 2
    if y1 == -n-1:
        y = -1
        if (x1 == n and y1 == -n - 1) or a[x1][y1] != '0':
            x -= 1
            y += 2
    a[y][x] = str(c)
    x += 1
    y -= 1
    for i in a:
        print(' '.join(i))
    print('===============================')

m = int(input())
n = int(input())
a = n - m
print(a)
b = a - 1
print(b)
res = a - b
print(res)

def f():
    global m
    global n
    if n != 0:
        m += 1
        n -= 1
        f()
m, n = list(map(int, input().split()))
f()
print(m)

n, m = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(n)]
r = []
p = 0
for i in a:
    r.append(min(i))
d = max(r)
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == d:
            p = i+1, j+1
            break
    if p != 0:
        break
print(' '.join(map(str, p)))

n = int(input())
a = [['0' for j in range(n)] for i in range(n)]

b = n // 2
a[0][b] = '1'
c = 1
x = b + 1
y = -1
while c != 9:
    c += 1
    a[y][x] = str(c)
    x += 1
    y -= 1
    if x == n-1 and y == -n:
        x -= 1
        y -= 2
        print("f")
    elif y == -n:
        y = -1
        x += 1
        print("R")
    elif x == n-1:
        x = 0
        y -= 1
        if y == -n-1:
            y = -2
            x += 1
        print("x")
    elif x <= n-1 and y >= -1:
        if a[y][x] != '0':
            y += 1
            print("Y")
    # else:
    #     x += 1
    #     y -= 1
    print(y, x, '<-', c)
for i in a:
    print(' '.join(i))


# if x == n and y == n:
#     x -= 1
#     y -= 2
# elif x == n:
#     x = 0
#     y -= 1
# elif y == n:
#     y = -1
#     x = 0


l = int(input())
n = int(input())
a = [int(input()) for i in range(n)]
r = a
for i in range(len(a)):
    if a[i] == 1:
        a = a[i:]
        for i in range(len(a)):
            if a[-i-1] == 1:
                a = a[:-i-1]
                a.append(1)
                break
        break
res = len(a) // l
if len(a) % l > 0:
    res += 1
print(res)

a = input()
res = 'w'
for i in a[len(a):0:-1]:
    if i != '0':
        res += str(i)
res += a[0]
print(res[1:])

a = list(map(int, input().split()))
for i in range(len(a)-2):
    if a[i+1] != 2 and a[i] == 2:
        a.remove(2)
print(sum(a) // len(a))


a = input()
l = 0
for i in a:
    if i == ' ':
        l += 1
    else:
        a = a[l:]
        break
a = list(map(str, a.split()))
for i in range(len(a)):
    a.insert(i*2+1, ' ' * (i + 1))
l = 0
for i in a:
    if i == ' ':
        a = a[:-1]
print(''.join(a))


a = input()
r = 0
l = 0
for i in a:
    if i.isalpha():
        l += 1
    else:
        if l > r:
            r = l
        l = 0
res = 'w'
for i in a:
    if i.isalpha():
        if 97 > ord(i) + r > 90:
            d = ord(i) + r - 90
            res += chr(64 + d)
        elif ord(i) + r > 122:
            d = ord(i) + r - 122
            res += chr(96 + d)
        else:
            res += chr(ord(i) + r)
    else:
        res += i
print(res[1:])

a = int(input())

a = 'a'
for i in range(97, 123):
    a += chr(i)
    print(a[1:])

a, c = list(map(float, input().split()))
b = 2 * a
c = c / 100
res = 0
while a < b:
    a = int(a + a * c)
    res += 1
print(res)


b, a = input().split()
r = int(a) - int(b) + 1
if (int(b) - 1) % r == 0:
    print("YES")
else:
    print("NO")

a = list(map(str, input().split()))
res = 0
for i in range(len(a)-2):
    if a[i+2] == a[i]:
        res += 1
    else:
        res -= 1
if a[-1] == '1' and a[0] == '1':
    res += 1
if res not in [0, -2]:
    print("YES")
else:
    print("NO")

m = int(input())
n = int(input())
r = m - n
print(r, r - 1)
res = r - (r - 1)
print(res)

a = list(map(str, input().split()))
res = 0
for i in range(len(a)-1):
    if a[i] == '1':
        if a[i + 1] != a[i]:
            res += 1
if a[-1] == '1':
    if a[-1] != a[-2]:
        res += 1
if res > 1:
    print("YES")
else:
    print("NO")

a = list(map(int, input().split()))
res = []
res1 = []
for i in range(3):
    a[-1], a[-2] = a[-2], a[-1]
    res.append(''.join(map(str, a)))
    a[-1], a[0] = a[0], a[-1]
    res.append(''.join(map(str, a)))
for i in res:
    if int(i) % 2 == 0:
        res1.append(i)
print(max(res1))


a = list(map(int, input().split()))
c0 = []
c1 = []
for i in a:
    if i % 2 == 0:
        c0.append(i)
    else:
        c1.append(i)
r0 = max(c0)
r1 = max(c1)
print(c0, c1)
print(r0, r1)

A = int(input())
B = int(input())
C = int(input())
ac = A // C
acc = A - (C * ac)
r = (B - acc) - A
res = r // C
print(res + 1)

A = int(input())
B = int(input())
C = int(input())
r = (B - A) // C
print(r)

A = int(input())
B = int(input())
C = int(input())
r = B - A
res = r // C
print(res + 1)

p = int(input())
n = int(input())
def f(p, n):
    if n//p != 0:
        f(p, n//p)
        print(n % p, end='')
    else:
        print(n % p, end='')
    return '('+str(p)+')'
print(str(n)+'(10)=', end='')
print(f(p, n))

# a = str(n%p)
# n = n//p
# a += str(n%p)
# n = n//p
# a += str(n%p)
# n = n//p
# a += str(n%p)
# n = n//p
# a += str(n%p)
# n = n//p


import sys
sys.setrecursionlimit(10**9)
def A(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return A(m - 1, 1)
    elif m > 0 and n > 0:
        return A(m-1, A(m, n-1))
    else:
        return 0
m, n = list(map(int, input().split()))
print(A(m, n))

p = int(input())
n = int(input())
b = str(n)
a = str(n%p)
n = n//p
a += str(n%p)
n = n//p
a += str(n%p)
n = n//p
a += str(n%p)
n = n//p
a += str(n%p)
n = n//p
r = int(b[0])*10**(len(b)-1) + int(b[1])*10**(len(b)-2) + int(b[2])*10**(len(b)-3)
print(r, a[-1:0:-1]+a[0])

def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return power(a, n-1)*a
    else:
        b = a * a
        return power(b, n/2)
a = float(input())
n = int(input())
print(power(a, n))
def f(x):
    if x != 0:
        f(int(input()))
        print(x)
    else:
        print(0)
f(int(input()))

def f(x):
    if x > 0:
        g(x - 1)
def g(x):
    print('*', end='#')
    if x > 1:
        f(x-3)
f(11)

def f(n):
    print(n)
    if n == 0:
        return 1
    else:
        return f(n - 1) * n
print(f(5))

def f():
    global a
    global b
    b, c = a, b
def g():
    global a
    global d
    c = '0'
    a = d + c
a = '2'
b = '3'
c = '5'
d = '7'
f()
g()
f()
print(a + b + c + d)
def min_num(n):
    for i in range(1, n+1):
        if n - (i+1)*(i+1) < 0:
            return i*i
def resultn(x, y):
    xn = min_num(x)
    yn = min_num(y)
    if min_num(x + y) > yn + xn:
        return 'Petya gives paint to Vasya'
    elif min_num(x + y) < yn + xn:
        return 'Petya leaves paint to himself'
    return 'Equal'
print(resultn(int(input()), int(input())))


def makeLevel(n):
    for j in range(n+2):
        print('*'*(j+1))
def tree(n):
    for i in range(n):
        makeLevel(i)
n = int(input())
tree(n)

def triangle(a,b,c):
    if a < b+c and b < a+c and c < a+b:
        return True
    else:
        return False

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if triangle(a,b,c) or triangle(a,b,d) \
  or triangle(a,c,d) or triangle(b,c,d):
    print("YES")
else:
    print("NO")