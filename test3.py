n = list(map(int, input().split()))
a = n[0]
m = 0
sm = 0
l = []
for i in range(n[1]):
    if a % 2 == 1:
        a = 3 * a + 1
    else:
        a = a / 2
    l.append(str(int(a)))
for i in range(len(l)):
    if int(l[i][-1] + l[i][-2] + l[i][-3]) > sm:
        sm = int(l[i][-1] + l[i][-2] + l[i][-3])
        m = str(l[i]) + ' ' + str(i + 1)
print(m)