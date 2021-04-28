print((10*9*8*7*6*5*4*3*2*1)/((3*2*1)*(7*6*5*4*3*2*1)))

n, m = list(map(int, input().split()))
a = [h+1 for h in range(n*m)]
for i in range(n):
    if i % 2 == 0:
        print(' '.join(map(str, a[i * m:m + (i * m)])))
    elif i % 2 == 1:
        print(' '.join(map(str, a[m + (i * m) - 1:i * m - 1:-1])))

n, m = list(map(int, input().split()))
r = [[0]*m for i in range(n)]
a = [list(map(int, input().split())) for i in range(n)]
r[0][0] = a[0][0]
res = []
for i in range(1, m):
    r[0][i] = r[0][i-1]+a[0][i]
for i in range(1, n):
    r[i][0] = r[i-1][0]+a[i][0]
for i in range(1, n):
    for j in range(1, m):
        r[i][j] = a[i][j]+max(r[i][j-1], r[i-1][j])
j = 1
h = 1
l = 0
for f in range(n*m):
    l = r[-j][-h] - a[-j][-h]
    if j != n:
        if l == r[-j-1][-h]:
            j += 1
            res.insert(0, 'D')
    if h != m:
        if l == r[-j][-h-1]:
            h += 1
            res.insert(0, 'R')
print(r[-1][-1])
print(' '.join(map(str, res)))

n, m = list(map(int, input().split()))
a = [[0]*8 for i in range(8)]
a[8-m][n-1] = 1
for i in range(8-m+1):
    b = abs(i - 8 + m + 1)
    for j in range(7):
        a[b][j] = a[b + 1][j - 1] + a[b + 1][j + 1]
r = 0
for i in a[0]:
    r += i
print(r)
for i in a:
    print(' '.join(map(str, i)))

n = int(input())
A = [[4]*i for i in range(8//2-(1*(8%2)))]
for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()

n, m = list(map(int, input().split()))
a = [[0]*8 for i in range(8)]
a[8-m][n-1] = 1
r = 0
for i in range(8-m+1):
    b = abs(i-8+m+1)
    for j in range(7):
        a[b][j] = a[b+1][j-1] + a[b+1][j+1]
for i in range(len(a[0])):
    r += a[0][i]
print(r)

n, m = list(map(int, input().split()))
a = [[1]*m for i in range(n)]
for i in range(1, len(a)):
    for j in range(1, len(a[i])):
        a[i][j] = a[i-1][j]+a[i][j-1]
print(a[-1][-1])

n, m = list(map(int, input().split()))
A = [[i+n*j for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        print(A[i][j], end=' ')
    print()

n, m = list(map(int, input().split()))
a = [[abs(abs(j%2-i%2)-1) for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()

n, m = list(map(int, input().split()))
a = [i+1 for i in range(n*m)]
r = 0
print(a)

n = int(input())
a = [[abs(i-j) for j in range(n)] for i in range(n)]
for i in a:
    print(' '.join(map(str, i)))

a = list(map(int, input().split()))
m1 = min(a)
m2 = max(a)
i_min = a.index(m1)
i_max = a.index(m2)
a[i_min] = m2
a[i_max] = m1
print(' '.join(map(str, a)))


n, m = list(map(int, input().split()))
a = [list(map(str, input().split())) for i in range(n)]
k = int(input())
r = 0
h = False
for i in a:
    for j in range(len(i)):
        if int(i[j:j+k].count('0')) >= k:
            r = a.index(i)+1
            h = True
            break
    if h:
        break
print(r)

n, m = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(n)]
r = a[0][0]
res = 0
res_1 = 0
for i in range(len(a)):
    if max(a[i]) > r:
        r = max(a[i])
        for j in range(len(a[i])):
            if a[i][j] == r:
                res = j
                res_1 = i
                break
print(res_1, res)

n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
r = True
for i in range(n):
    for j in range(n):
        if a[j][i] != a[i][j]:
            r = False
            print("NO")
            print(a[j][i], a[i][j])
            print(j, i, i, j)
if r:
    print("YES")

n, m = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(n)]
x = int(input())
p = [list(map(int, input().split())) for j in range(x)]
r = []
for i in p:
    if i not in r:
        r.append(i)
res = 0
for i, j in r:
    res += a[i-1][j-1]
print(res)


n, m = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(n)]
k = int(input())
r = 'h'
res_1 = 0
for i in a:
    for j in range(len(i)):
        if i[j:j+k].count(0) >= k:
            res_1 = a.index(i)
            r = 'gg'
            break
    if r == 'gg':
        break
print(res_1)


n, m = list(map(int, input().split()))
a = []
a += [[str(1)]*m for i in range(n)]
for i in range(n-1):
    for j in range(m-1):
        a[i+1][j+1] = str(int(a[i][j+1]) + int(a[i+1][j]))
for i in a:
    print(' '.join(i))

n = int(input())
a = [list(map(str, input().split())) for i in range(n)]
r = 'r'
f = 0
t = 0
s = 0
for i in range(n*(n+1)):
    if f != n:
        r += str(a[f][s])+' '
        f += 1
    else:
        print(r[1:])
        f = 0
        s += 1
        r = 'r'

n = int(input())
a = [list(map(str, input().split())) for i in range(n)]
s = 0
r = 0
for i in range(n**2):
    a[s][r], a[r][s] = a[r][s], a[s][r]
    if r == n-1:
        s += 1
        r = 0
    else:
        r += 1

for i in a:
    print(' '.join(i))

n = int(input())
a = [list(map(str, input().split())) for i in range(n)]
r = 'r'
s = 0
f = 0
for i in range(n**2):
    if i != n:
        f += 1
        r += str(a[f][s])+' '
    else:
        s += 1
        print(r[1:])
        r = 'r'
        f = 0

n = int(input())
a = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    a[0][i], a[i][0] = a[i][0], a[0][i]
for i in a:
    print(' '.join(i))

n = int(input())
a = [list(map(str, input().split())) for i in range(n)]
t = 0
r = 0
for i in range(n**2):
    print(a[r][t])
    if r == n-1:
        r = 0
        t += 1
    else:
        r += 1

n = int(input())
a = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    a[i][i], a[-i-1][i] = a[-i-1][i], a[i][i]
for i in a:
    print(' '.join(i))

n, m = list(map(int, input().split()))
a = [list(map(str, input().split())) for i in range(n)]
r = a[0][0]
o = a[0][0]
p = []
po = [0, 0]
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] > r:
            r = a[i][j]
            p = [i, j]
    if r > o:
        o = r
        po = p
print(' '.join(map(str, po)))


n, m = list(map(int, input().split()))
a = [list(map(str, input().split())) for i in range(n)]
b, c = list(map(int, input().split()))
for i in a:
    i[b], i[c] = i[c], i[b]
for i in a:
    print(' '.join(i))


n = list(map(int, input().split()))
t = [['.']*8 for i in range(8)]
for i in n:
    a = i+1
    if i == n[0]-1:
        None

n = list(map(int, input().split()))
t = [['.']*8 for i in range(8)]
t[n[0]-3][n[1]] = '*'
t[n[0]-3][n[1]-2] = '*'
t[n[0]+1][n[1]] = '*'
t[n[0]+1][n[1]-2] = '*'
t[n[0]-2][n[1]+1] = '*'
t[n[0]-2][n[1]-3] = '*'
t[n[0]][n[1]+1] = '*'
t[n[0]][n[1]-3] = '*'

t[n[0]-1][n[1]-1] = 'K'
for i in t:
    print(' '.join(i))


n = int(input())
a = [['.']*n for elem in range(n)]
r = n // 2
a[r] = ['*' for i in a[r]]
for i in range(n):
    a[i][r] = '*'
for i in range(n):
    l = -i-1
    a[l][i] = '*'
for i in range(n):
    a[i][i] = '*'
for i in a:
    print(' '.join(i))

x = list(map(int, input().split()))
a = max(x)
b = min(x)
c = x.index(b)
d = x.index(a)
x.remove(a)
x.remove(b)
x.insert(c, a)
x.insert(d, b)
print(' '.join(map(str, x)))

x = list(map(str, input().split()))
a = max(x)
b = min(x)
c = x.index(a)
d = x.index(b)
x.remove(a)
x.insert(c, b)
x.insert(d, a)
x.pop(c)
print(' '.join(x))

x = list(map(str, input().split()))
a = max(x)
b = min(x)
c = x.index(a)
d = x.index(b)
x.remove(a)
x.insert(c, b)
x.insert(d, a)
x.remove(b)
print(' '.join(x))

x = list(map(int, input().split()))
r2 = 0
r3 = 0
for i in range(len(x)):
    for l in x[i+1:]:
        if x[i] == l:
            r2 += 1
print(r2)

x = list(map(int, input().split()))
r = []
for i in range(len(x)):
    if x[i] not in x[:i] and x[i] not in x[i+1:]:
        r.append(str(x[i]))
print(' '.join(r))

x = list(map(str, input().split()))
k = list(map(int, input().split()))
C = k[-1]
x.insert(k[0], str(C))
print(' '.join(x))

x = list(map(str, input().split()))
k = int(input())
x.pop(k)
print(' '.join(x))

x = list(map(int, input().split()))
s = []
for i in range(len(x)):
    r = i
    if len(x) % 2 == 1:
        if i % 2 == 1:
            r = -i-1
        s.append(x[r])
    else:
        if i % 2 == 1:
            r = -i
        s.append(x[r])
print(' '.join(map(str, s)))

x = list(map(int, input().split()))
s = []
for i in range(len(x)):
    r = i
    if i % 2 == 1:
        r = -i-1
        print(r)
    s.append(x[r])
print(' '.join(map(str, s)))

x = input().split()
print(' '.join(x[len(x)+1::-1]))

x = int(input())
s = [x**i for i in range(int(input()))]
print(s)

s = list(map(int, input().split()))
res = 2**31
a = 0
b = 0
for i in range(len(s)):
    for l in range(len(s)):
        if l != i:
            g = abs(s[l] - s[i])
            if g < res:
                res = g
                a = i
                b = l
print(a, b)

n = int(input())
s = list(map(int, input().split()))
r = (n-1)/2
for i in s:
    lc = 0
    rc = 0
    for l in s:
        if l < i:
            lc += 1
        elif l > i:
            rc += 1
    if lc == r and rc == r:
        print(i)
        break
print('end')

s = list(map(int, input().split()))
r = s[0]-s[1]
a = s[0]
b = s[1]
for i in range(len(s)):
    for l in range(len(s)):
        if i != l:
            g = abs(s[i]-s[l])
            if g < r:
                a = i
                b = l
                r = g
print(a, b)

s = list(map(int, input().split()))
r = s[0]-s[1]
a = s[0]
b = s[1]
for i in range(len(s)):
    if i != len(s)-1:
        g = abs(s[i]-s[i+1])
        if g < r:
            a = s[i]
            b = s[i+1]
            r = g
print(a, b)

s = list(map(str, input().split()))
print(s[-1], ' '.join(s[:len(s)-1]))

s = list(map(int, input().split()))
x = int(input())
res = len(s)
for i in range(len(s)):
    if s[i]-x < 0:
        res = i
        break
res += 1
print(res)


s = list(map(int, input().split()))
count = 0
for i in range(len(s)):
    if s[i] not in s[:i]:
        count += 1
print(count)

s = list(map(int, input().split()))
res = 1000
for i in range(len(s)):
    if s[i] > 0:
        if s[i] < res:
            res = s[i]
print(res)

s = list(map(int, input().split()))
for i in range(len(s)):
    if i != 0:
        if (s[i]<0 and s[i-1]<0) or (s[i]>0 and s[i-1]>0):
            print(s[i-1], s[i])
            break

s = list(map(int, input().split()))
count = 0
for i in range(len(s)):
    if i != 0 and i != len(s)-1:
        if s[i-1] < s[i] and s[i+1] < s[i]:
            count += 1
print(count)

s = list(input().split())
res = []
for i in range(0, len(s), 2):
    res.append(s[i])
print(' '.join(map(str, res)))

s = list(map(int, input().split()))
res = []
for i in s:
    if i % 2 == 0:
        res.append(i)
print(' '.join(map(str, res)))

s = input()
a = s.split()
print(a)

n = int(input())
a = []
for i in range(n):
    i += 1
    a.append(i**2)
print(a)

s = input().lower()
m_a = 0
g = 0
m_b = s[0]
for i in s:
    g += 1
    m = s.count(i)
    if i.isalpha():
        if m > m_a:
            m_a = m
            m_b = i.upper()
        elif m == m_a:
            m_b += i.upper()
b = m_b[-1]
for i in m_b:
    if i not in b:
        b += i
res = b[0]
for i in range(65, 90):
    if chr(i) in b:
        res += chr(i)
res = res[1:]
print(res)
print(m_a)

def Capitalize(S):
    s = S.lower()
    i = 0
    s1 = s[-1]
    if s[-1].isalpha() == False:
        s = s[:-1] + s[-1].replace(s[-1], '')
    while i != len(s):
        if s[i].isalpha():
            if s[i-1].isalpha() == False:
                s = s[0:i] + s[i:].replace(s[i], s[i].upper(), 1)
        i += 1
    if s1.isalpha() == False:
        s = s.replace(s[0], s[0].upper(), 1) + s1
    else:
        s = s.replace(s[0], s[0].upper(), 1)
    return s
S = input()
print(Capitalize(S))

def IsPalindrome(S):
    s = S.lower()
    r = 0
    res = 0
    for i in s:
        r -= 1
        if i == s[r]:
            res += 1
        else:
            o = False
    if res == len(s):
        o = True
    return o
S = input()
if IsPalindrome(S):
    print('YES')
else:
    print('NO')

def Capitalize(S):
    s = S.lower()
    i = 0
    s1 = s[-1]
    if s[-1].isalpha() == False:
        s = s[:-1] + s[-1].replace(s[-1], '')
    while i != len(s):
        if s[i] == ' ' or s[i] < 'A' or 'Z' < s[i] < 'a' or 'z' < s[i]:
            i += 1
            s = s[0:i] + s[i:].replace(s[i], s[i].upper(), 1)
        i += 1
    if s1.isalpha() == False:
        s = s.replace(s[0], s[0].upper(), 1) + s1
    else:
        s = s.replace(s[0], s[0].upper(), 1)
    return s
S = input()
print(Capitalize(S))

def Capitalize(S):
    s = S.lower()
    i = 0
    while i != len(s):
        if ord(s[i]) < 65 or 90 < ord(s[i]) < 97 or 122 < ord(s[i]) < 127:
            i += 1
            s = s[0:i]+s[i:].replace(s[i], s[i].upper(), 1)
        i += 1
    s = s.replace(s[0], s[0].upper(), 1)
    return s
S = input()
print(Capitalize(S))

#===========================================
def Capitalize(S):
    s = S.lower()
    i = 0
    while i != len(s):
        if s[i] == ' ':
            i += 1
            s = s[0:i]+s[i:].replace(s[i], s[i].upper(), 1)
        i += 1
    s = s.replace(s[0], s[0].upper(), 1)
    return s
S = input()
print(Capitalize(S))
#===========================================

a = input()
b = input()
a1 = ord(a[0])
a2 = int(a[1])
b1 = ord(b[0])
b2 = int(b[1])
if a1 == b1:
    if a2-b2==1 or a2-b2==-1:
        print("YES")
    else:
        print("NO")
elif a2 == b2:
    if a1-b1==1 or a1-b1==-1:
        print('YES')
    else:
        print("NO")
elif (a2-b2==1 and (a1-b1==1 or a1-b1==-1)) or (a2-b2==-1 and (a1-b1==-1 or a1-b1==1)):
        print("YES")
else:
    print('NO')

a = input()
b = input()
r1 = ord(a[0])+ord(a[1]) - ord(b[0])+ord(b[1])
r2 = ord(a[0])-ord(a[0])
if r2 != -1 or r2 != 1:
    print("NO")
elif r1 == -2 or r1 == -1 or r1 == 0 or r1 == 1 or r1 == 2:
    print("YES")
else:
    print("NO")

a = input()
b = input()
ra = ord(a[0])+ord(a[1])
rb = ord(b[0])+ord(b[1])
print(ra)
print(rb)
if a[0] == b[0]:
    r = ord(a[1]) - ord(b[1])
    if r == -1 or r == 0 or r == 1:
        print("YES")
    else:
        print("NO")
elif a[1] == b[1]:
    r = ord(a[0]) - ord(b[0])
    if r == -1 or r == 0 or r == 1:
        print("YES")
    else:
        print("NO")
else:
    print("No")

def CaesarCipherChar(c, k):
    return  chr(ord(S)+k)
def CaesarCipher(s,k):
    r = s[0]
    for i in s:
        if i.isalpha():
            g = ord(i)+int(k)
            if 90 < g < 97:
                r += chr(g - 90 + 64)
            elif 122 < g:
                r += chr(g - 122 + 96)
            else:
                r += chr(g)
        else:
            r += i
    r = r[1:]
    s = r
    return s
S = input()
print(CaesarCipher(S, 3))

def CaesarCipherChar(c, k):
    return  chr(ord(S)+k)
def CaesarCipher(s,k):
    for i in s:
        if i.isalpha():
            d = ord(i)+int(k)
            if 97 > d > 90:
                r = d - 90 + 25
            elif d > 122:
                r = d - 122 + 25
            else:
                r = d
            s = s.replace(i, chr(r))
    return s
S = input()
print(CaesarCipherChar(S, 3))


def IsPalindrome(S):
    s = S.lower()
    for i in range(len(s)):
        m = -i
        if s[i] == s[m-1]:
            res = True
        elif s[i] != s[m-1]:
            res = False
    return res
S = input()
if IsPalindrome(S):
    print('YES')
else:
    print('NO')

a = input()
r = IsPalindrome(a)
if r:
    print("YES")
else:
    print("NO")
s = input().lower()
m_a = 0
m_b = s[0]
for i in s:
    m = s.count(i)
    if i.isalpha():
        if m > m_a:
            m_a = m
            m_b = i.upper()
        elif m == m_a:
            m_b += i.upper()
b = m_b[-1]
for i in m_b:
    if i not in b:
        b += i
print(b)
print(m_a)

s = input().lower()
h = s[0]
max_g = 0
max_b = s[0]
for i in s:
    g = 0
    if i.isalpha():
        for u in s:
            if u == i:
                g += 1
                if g > max_g:
                    max_g = g
                    max_b += i.upper()
print(max_g)
print(max_b)

def Capitalize(s):
    return None
a = input()
res = Capitalize(a)
print(res)

def Capitalize(s):
    f = 0
    res = s
    for i in res:
        if res[f].isalpha() == False:
            g = res[f+1]
            res = res.replace(g, g.upper())
            f += 1
    return res
a = input()
res = Capitalize(a)
print(res)

def Capitalize(s):
    f = 0
    for i in s:
        f += 1
        if i.isalpha():
            g = s[f-1]
            if g.isalpho():
                break
            else:
                s = s.replace(s[g], g.upper)
    return s
a = input()
res = Capitalize(a)
print(res)

def sss(c):
    if c.isupper():
        c = c.lower()
    elif c.islower():
        c = c.upper()
    return c
a = input()
ans = sss(a)
print(ans)


s = ord(input())
d = ord(input())
res = chr(s)
while s <= d:
    res += chr(s)
    s += 1
res = res.replace(res[0], '', 1)
print(res)

print(chr(int(input())))

s = input()
res = s[0]
for i in s:
    res += '*'+i
print(res[2:])


s = input()
i = 0
while i != 1:
    s = s.replace(s[i], s[i]+'*', 1)
    i += 2
    if i == len(s):
        i = 1
print(s[0:len(s)-1:1])

s = input()
s = s.replace('h', 'H', s.count('h')-1)
s = s.replace('H', 'h', 1)
print(s)

s = input()
first = s.find('h')
second = s.rfind('h')
h = s[first+1:second].replace('h', 'H')
print()


s = input()
print(s.count(' ')+1)

print(input().replace('1', 'one'))

s = input()
result = s[0]
for i in s:
    n = s.count(i)
    first = s.find(i)
    second = s.rfind(i)
    answer = s[first:second+1]
    if len(answer) > len(result):
        result = answer
print(result)


s = 'Abrakadabra'
print(s.replace('ra', 'e'))

n = input()
print(n[::2] + n[1::2])

n = input()
if n == n[::-1]:
    print('YES')
else:
    print('NO')

n = input()
print(n[2])
print(n[-2])
print(n[:5])
print(n[:-2])
print(n[::2])
print(n[1::2])
print(n[::-1])
print(len(n))

n = input()
res = int(n[0])
i = 0
for c in n:
    i += 1
    if c == '+':
        res += int(n[i])
    elif c == '-':
        res -= int(n[i])
print(res)

n = int(input())
res_i = 0
i = 0
while n != 0:
    if i == n:
        res_i += 1
    
    n = int(input())


n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)

n = int(input())
a = 0
s = 0
while s <= n:
     s1 = n-s
     a += (s1//2+1)*(s//10+1)
     s += 5
print(a)

n = int(input())
i = 2
res_1 = n
while i != 0:
    if n % i == 0:
        res_1 = i
        i = 0
    elif i > 23:
        i = 0
    else:
        i += 1
print(res_1)

n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)


x = int(input())
p = int(input())
y = int(input())
i = 0
while x < y:
    x *= 1 + p / 100
    x = int(100 * x) / 100
    i += 1
print(i)

x = int(input())
p = int(input())
y = int(input())
num = 0
i = 1
while i != 0:
    percent = x / 100 * p
    x = x + percent
    num = num + 1
    if x > y:
        i = 0
print(num)

n = int(input())
i = 0
d = 2
while i != 0:
    if n % i == 0:
        d = 3
        print('del')
    elif i > n:
        i = 0


n = int(input())
i = 2
while i != 0:
    m = 1
    res = 1
    while m <= 3:
        if i % m == 0:
            res += 1
        m += 1
        if m == 3:
            if n % i == 0:
                res_1 = i
                i = 0
            else:
                i = i + 1
print(res)

x = int(input())
p = int(input())
y = int(input())
num = 0
i = 1
while i != 0:
    percent = x / 100 * p
    percent = percent // 1
    x = x + percent
    num = num + 1
    if x > y:
        i = 0
print(num)

n = int(input())
c = n
b = 0
a = 0
res = 0
while n != 0:
    a = b
    b = c
    c = n
    if a < b and b > c:
        res += 1
    n = int(input())
print(res)


n = int(input())
a = 0
b = 1
i = 1
res = 0
while i != 0:
    res += 1
    b_1 = b
    b += a
    a = b_1
    i = n - b
    if b > n:
        print(-1)
        i = 0
    elif n == b:
        print(res+1)

n = int(input())
b = 0
i = 1
a = 0
res = 0
while i != 0:
    b_1 = b
    b += a
    a = b_1
    i = n - b
    res += 1
    if i == 0:
        print(res)
    elif b > n:
        print("-1")
print('end')

e = int(input())
a = 10 ** 9
res = 0
i = 0
while e != 0:
    res = res + e
    i += 1
    e = int(input())
res = res / i
print(res)


e = int(input())
a = e
res = 0
while a != 0:
    if e < a:
        res += 1
    a = int(input())
print(res)

e = int(input())
a = 10 ** 9
b = 10 ** 9
while e != 0:
    if e < a:
        b = a
        a = e
    elif e < b:
        b = e
    e = int(input())
print(b)

elem = int(input())
prev_1 = elem
prev_2 = elem
prev = 10 ** 9
while elem != 0:
    if elem >= prev_1:
        if elem < prev:
            if prev < 10**9:
                prev_1 = prev
            else:
                prev_1 = elem
            prev = elem
        elif elem >= prev:
            prev_1 = prev_2
            prev_2 = elem
    elem = int(input())
print(prev)
print(prev_2)
print(prev_1)
print('end')


n = int(input())
i = 0
while i**2 <= n:
    print(i**2)
    i += 1


n = int(input())
i = 2
while i != 0:
    m = 1
    res = 1
    while m <= 3:
        if i % m == 0:
            res += 1
        m += 1
        if m == 3:
            if n % i == 0:
                res_1 = i
                i = 0
            else:
                i = i + 1
print(res_1)

n = int(input())
m = 1
res = 0
while m != 3:
    if n % m == 0:
        res += 1
    m += 1
    print(m)
print(res + 1)


x = int(input())
p = int(input())
y = int(input())
num = 0
while x <= y:
    percent = x / 100 * p
    percent = int(percent)
    x = x + percent
    num = num + 1
print(num)


n = int(input())
i = 1
if n == 1:
    print("YES")
while i != n:
    i = i * 2
    if i == n:
        print("YES")
    elif i > n:
        print("NO")
        i = n

n = int(input())
if n % 2 == 0 or n == 1:
    print("YES")
else:
    print("NO")



n = int(input())
while n >= 0:
    n = n // 2
    if 2 - n == 0:
        print("YES")
        n = -1

n = int(input())
a = 0
b = 1
i = True
res = 0
while i != False:
    res = res + 1
    b_1 = b
    b = b + a
    a = b_1
    if n == b:
        print(res + 1)
        i = False
    elif res > n:
        print(-1)
        i = False



n = int(input())
while n % 13 != 0:
    print(n)
    n += 1


n = int(input())
b = 1
c = 0
for i in range(1, n+1):
    a = b * i
    b = a
    c = c + a
print(c)

n = int(input())
res = 1
a_1 = 1
for i in range(1, n+2):
    a = a_1 * i
    if a == 1:
        res = 0
    a_1 = res
    res = res + a
    print(res)



n = int(input())
res = 1
a = 0
for i in range(0, n+1):
    res = (i+1) * a * 1
    print(res)
    a = i
print(res)


n = int(input())
res = 0
m = int(input())
for i in range(n-1):
    m_1 = int(input())
    res += m * m_1
    m = m_1
print(res)



n = int(input())
res = 0
for i in range(1, n+1):
    res = res * 10 + int(i)
    print(res)


n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        print(i)

n = int(input())
res = 0
for i in range(n):
    if int(input()) == 0:
        res += 1
print(res)


a = int(input())
b = int(input())

for i in range(2):
    a_1 = a % 2
    a += a_1
for i in range(a, b+1, 2):
    print(i)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
res = (a - c) // d
for i in range(res, b, c):
    print(i)



a = int(input())
b = 1
for i in range(1, a+1):
    b = b * i
print(b)

k = int(input())
l = int(input())
m = int(input())
n = int(input())
res_y = (k - l) % 2
res_x = (m - n) % 2
if res_y == res_x:
    print('YES')
elif res_y != res_x:
    print('NO')
else:
    print('NO')


k = int(input())
l = int(input())
m = int(input())
n = int(input())

res_y = (k - m) % 2
print(res_y)
res_x = (l - m) % 2
print(res_x)
print(m - n)
if res_y == 0 and res_x == 0:
    print("YES")
else:
    print("NO")


k = int(input())
l = int(input())
m = int(input())
n = int(input())

a = k % l
if m % n == a or n % m == a:
    print("YES")
else:
    print("NO")



a = int(input())
b = int(input())
if a == 0:
    if b == 0:
        print('INF')
    else:
        print("NO")
else:
    if b % a == 0:
        print(-b // a)
    else:
        print("NO")


a = int(input())
b = int(input())
if a == 0:
    if b == 0:
        print('INF')
    else:
        print("NO")
else:
    b = -b
    x = b // a
    if b / a == 0:
        print(x)
    else:
        if x == 0:
            print("NO")
        else:
            print(x)



#bochki bochka bochek
n = int(input())
number_1 = n % 10
number_2 = n % 100
number_2 = number_2 // 10
if number_1 == 1:
    print(n, 'bochka')
elif number_1 == 1 or number_1 == 2 or number_1 == 3 or number_1 == 4:
    if number_2 == 2 and number_1 == 0 or number_2 == 1:
        print(n, 'bochek')
    else:
        print(n, 'bochki')
else:
    print(n, 'bochek')


a = int(input())
b = int(input())
c = int(input())
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a, b, c)


a = int(input())
b = int(input())
c = int(input())
if a > b > c:
    print(c, b, a)
elif a > c > b:
    print(b, c ,a)
elif b > c > a:
    print(a, c, b)
elif b > a > c:
    print(c, a, b)
elif c > a > b:
    print(b, a, c)
elif c > b > a:
    print(a, b, c)


a = int(input())
b = int(input())
c = int(input())
res = 1
if a == b:
    res = res + 1
if b == c:
    res = res + 1
if c == a:
    if a != b:
        res = res + 1
if res == 1:
    res = res - 1
print(res)


a = int(input())
b = int(input())
c = int(input())
if a > c:
    if a > b:
        print(int(a))
    else:
        print(b)
else:
    if c > b:
        print(c)
    else:
        print(b)


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a <= d:
    if b <= e or c <= e:
        print("YES")
    else:
        print("NO")
elif b <= d:
    if a <= e or c <= e:
        print("YES")
    else:
        print("NO")
elif c <= d:
    if a <= e or b <= e:
        print("YES")
    else:
        print("NO")
else:
    print("NO")

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a > b:
    a = b
if b > c:
    b = c
res_1 = False
res_2 = False
if a <= d or b <= d:
    res_1 = True
if b <= e or a <= e:
    res_2 = True
if res_2 and res_2:
    print("YES")
else:
    print("NO")


n = int(input())
m = int(input())
x = int(input())
y = int(input())
if m < n:
    short = m
    long = n
if n < m:
    short = n
    long = m
before_short = long - y
before_long = short - x
if before_short < y:
    res_1 = before_short
if y < before_short:
    res_1 = y
if before_long < x:
    res_2 = before_long
if x < before_long:
    res_2 = x
if res_2 < res_1:
    print(res_2)
if res_1 < res_2:
    print(res_1)


k = int(input())
l = int(input())
m = int(input())
n = int(input())
km = k - m
ln = l - n
if km < 0:
    km = -km
if ln < 0:
    ln = -ln
if (k - m) == (l - n) or km == ln or km == 2 or ln == 2 or km == 0 or ln == 0:
    print("YES")
else:
    print("NO")

k = int(input())
l = int(input())
m = int(input())
n = int(input())
km = k - m
ln = l - n
if km < 0:
    km = -km
if ln < 0:
    ln = -ln
if ln == 2 and km == 1 or ln == 1 and km == 2:
    print("YES")
else:
    print("NO")


k = int(input())
l = int(input())
m = int(input())
n = int(input())
if (k - m) == (l - n) or (k + l) == (m + n) or (k - l) == (m - n):
    print("YES")
else:
    print("NO")

n = int(input())
a = n // 2
b = n % 2
c = a * b
c_1 = a + c
c_2 = c_1 + b
print(c_2)



a = int(input())
b = int(input())
a_1 = a // b
b_1 = b // a
c = (a*a_1) + (b*b_1)
c_1 = a_1 + b_1
c = c // c_1
print(c)

a = int(input())
b = int(input())

a_1 = a // b
#   = 8 // 5 = 1
print(a_1)
b_1 = b // a
#   = 5 // 8 = 0
print(b_1)
a_2 = a * a_1
#   = 8 * 1 = 8
print(a_2)
b_2 = b * b_1
#   = 5 * 0 = 0
print(b_2)
c = a_2 + b_2
# = 8 + 0 = 8
d = c // b
d_1 = c // a
print(c)

k = int(input())
n = int(input())
a = n // k
b_1 = n % k
b_2 = b_1 + k
c = b_2 // (k+1)
a = a + c
print(a)

n = int(input())
v = n % 10000
n = '0' + str(v)
n = int(n)
a = n // 1000
b = n % 10
a_1 = n // 100 % 10
b_1 =n // 10 % 10
a_2 = a_1 - b_1
b_2 = a - b
i = 1 - (1 * b_2) - (1 * a_2)
print(i)

k = int(input())
n = int(input())
a = n // k
b_1 = n % k
b_2 = b_1 + k
c = b_2 // (k+1)
b = b_2 % (k+1) + (c)
a = a + c
print(a, b)

k = int(input())
n = int(input())
k = k + 1

c = n // k + 1
print(c)
a = k - 1
a_1 = n % k
b_1 = n % k + 1
print(b_1)
b = n - (c*k) + 2
print(c, b_1)

k = int(input())
n = int(input())

a = k % n           #50, 50
a_1 = n % k         #0, 10
b = n - a           #50, 60
b_1 = b // k        #1, 1
b = b % n           #50, 60
c = 1 + b_1         #2, 2
num = c*k + b
print(num)
num_1 = num // k
c_1 = b // k
c = c + c_1
b = b % k
print(num_1)
print(c, b)

n = int(input())
m = int(input())

a = n % m
b = m - a
b_1 = b // n
print(b)
c = 1 + b_1
print(c, b)

#.. // 50
#2 % 7
#1 + 1*0
#0714285714285714 + (1-0714285714285714)
# 0 + 0, 0.392 + 0.718

#a = a * n
#b_1 = b * n
#b = b_1 % 100
#b_2 = b_1 // 100
#a = a + b_2

#a = k % n
#b = n - a
#b = b % n
#print(b)