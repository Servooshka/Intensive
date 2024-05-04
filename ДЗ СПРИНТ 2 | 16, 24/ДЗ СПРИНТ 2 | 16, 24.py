#1

def f(n):
    if n >= 2023:
        return n
    if n < 2023:
        return f(n + 1) + f(n + 2)


print('1:', f(2019) - f(2020))

#2

import sys

sys.setrecursionlimit(3000)


def f2(n):
    if n == 1:
        return 1
    if n > 1:
        return (3 * n - 1) * f2(n - 1)


print('2:', f2(1456) / f2(1452))


#3

def f3(n):
    if n > 3000:
        return n
    if n <= 3000 and n % 2 == 0:
        return n + f3(n + 1) + 1
    if n <= 3000 and n % 2 != 0:
        return f3(n + 2) + 2


print('3:', f3(40) - f3(43))

#4

f = open('24_1.txt').readline()
f = f.replace('N', '*').replace('O', '*').replace('P', '*')
while '**' in f:
    f = f.replace('**', '* *')
f = f.split()
print('4:', max(map(len, f)))


#5

count = 0

f = open('2.txt').readline()
for i in range(len(f) - 6):
    if f[i] <= f[i + 1] <= f[i + 2] <= f[i + 3] <= f[i + 4] <= f[i + 5] <= f[i + 6]:

        count += 1
        if count == 1:
            print('5:', f[i:i + 7])
print('5:', count)


#6

f = open('24_3.txt').readline()
count = 0
ind = f.index('A')
for i in range(ind, len(f) - 6):
    if f[i] == 'A':
        for j in range(3, 7):
            if f[i + j] == 'C':
                count += 1
print('6:', count)
