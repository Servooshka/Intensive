#1

def f(n):
    if n >= 2023:
        return n
    if n < 2023:
        return f(n + 1) + f(n + 2)


print(f(2019) - f(2020))

#2

import sys

sys.setrecursionlimit(3000)


def f2(n):
    if n == 1:
        return 1
    if n > 1:
        return (3 * n - 1) * f2(n - 1)


print(f2(1456) / f2(1452))


#3

def f3(n):
    if n > 3000:
        return n
    if n <= 3000 and n % 2 == 0:
        return n + f3(n + 1) + 1
    if n <= 3000 and n % 2 != 0:
        return f3(n + 2) + 2


print(f3(40) - f3(43))

#4

f = open('24_1.txt').readline()
f = f.replace('N', '*').replace('O', '*').replace('P', '*')
while '**' in f:
    f = f.replace('**', '* *')
f = f.split()
print(max(map(len, f)))


#5

count = 0
max_c = 0
f = open('2.txt').readline()
for i in range(len(f) - 6):
    if f[i] < f[i + 1] < f[i + 2] < f[i + 3] < f[i + 4] < f[i + 5] < f[i + 6]:
        count += 1
        max_c = max(max_c, count)
    else:
        max_c = max(max_c, count)
        count = 0
print(max_c)


#6

f = open('24_1.txt').readline()
f = f.replace('A', '*').replace('C', '&')
c = 0
v = 0
count = 0
flag = False
flag2 = False
for i in f:
    if flag:
        c += 1

    if flag2:
        v += 1

    if i == '*' and flag == False:
        c += 1
        flag = True

    if i == '&' and flag == True and flag2 == False:
        c = 0
        flag = False

    if i == '*' and flag == True:
        v += 1
        flag2 = True

    if i == '&' and flag2 == True and flag == False:
        v = 0
        flag2 = False

    if 4 <= c <= 7 or 4 <= v <= 7:
        count += 1
print(count)