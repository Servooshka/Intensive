#1

print('1: 36')


#2
# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 if not (((not x) and (not y)) or (y == w) or z):
#                     print(w,z,y,x)
print('2: wzyx')

#3

print('3: 10622')

#4

print('4: 1111')


#5


for n in range(500000, 0, -1):
    r = bin(n)[2:]
    if n % 5 == 0:
        r += '101'
    else:
        r += '1'
    if int(r, 2) % 7  == 0:
        r += '111'
    else:
        r += '1'
    r = int(r, 2)
    if r < 1_755_661:
        print('5:', n)
        break

#6

print('6: 36')


#7

print('7: 3')


#8

import itertools

a = 'омре'
c = 0
count = 0
for i in list(itertools.product(a, repeat=5)):
    s = ''.join(i)
    if s == 'ммрор':
        c = 1
    if s == 'ермое':
        c = 2
    if c == 1:
        count += 1

    if c == 2:
        break
print('8:', count)





#9

from statistics import mean
def uni(f):
    f = f.split()
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    if (f.count(f[a]) == 1 and f.count(f[b]) == 1 and f.count(f[c]) == 1) and f.count(f[d]) == 2 and \
                            (f[a] != f[b] and f[a] != f[c] and f[b] != f[c]):
                        av = (int(f[a]) + int(f[b]) + int(f[c])) / 3
                        if av < int(f[d]):
                            return True

with open('9.txt') as s:
    s = s.readlines()

count = 0

for i in s:
    if uni(i):
        count += 1
print('9:', count)



#10
# a = 52
# b = 26
# c = 15
# d = 65
# f = a + b + c + d
print('10: 158')


#11

print('11: 45')



#12

s = '3' + '7' * 311 + '3'
count = 0
while '27' in s or '377' in s or '4777' in s:
    if '27' in s:
        s = s.replace('27', '4', 1)
    if  '377' in s:
        s = s.replace('377', '2', 1)
    if '4777' in s:
        s = s.replace('4777', '3', 1)

for i in s:
    if int(i) % 2 != 0:
        count += int(i)
print('12:', count)



#13

from ipaddress import *

count = 0
net = ip_network('105.224.200.224/255.255.255.224')
for ip in net:
    ip = bin(int(ip))[2:]
    if ip.count('1') % 4 == 0:
        count += 1
print('13:', count)


#14


x = abs(13 * 5 ** 32 - 23 * 25 ** 25 + 11 * 5 ** 13 - 165)
count = 0
while x > 0:
    if x % 5 == 4:
        count += 1
    x //= 5
print('14:', count)


#15

for a in range(100, 0, -1):
    flag = True
    for x in range(100, -1, -1):
        for y in range(100, -1, -1):
            if not((2 * x + y != 70) or (x < y) or (a < x)):
                flag = False
                break
        if not flag:
            break
    if flag:
        print('15:', a)
        break


#16

def f(n):
    if n > 20:
        return n * n * n + n
    if n % 2 == 0 and n <= 20:
        return 3 * f(n + 1) + f(n + 3)
    if n % 2 != 0 and n <= 20:
        return f(n + 2) + 2 * f(n + 3)
count = 0
for n in range(1, 1457):
    if str(f(n)).count('2') == 0:
        count += 1

print('16:', count)

#17

with open('17.txt') as f:
    f = f.readlines()

kr = [int(i) for i in f if (abs(int(i)) % 4 == 0 and (str(int((i)))[-1]) not in '246')]
max_kr = max(kr)

min_sum = 10000000
count = 0
for i in range(len(f) - 1):
    left, right = int(f[i]), int(f[i + 1])
    summ = left + right

    if (left < 0 or right < 0) and\
            (abs(left) % 2 == 0 or abs(right) % 2 == 0) and \
            (summ ** 3 > max_kr):
        min_sum = min(min_sum, summ)
        count += 1

print('17:', count, min_sum ** 3)


#18

print('18: 1561 644')


#19

def play(s1, s2, t):
    if s1 + s2 >= 100 or t > 5:
        return t == 2
    t += 1
    if t % 2 == 1:
        return any(turns(s1, s2, t))
    else:
        return any(turns(s1, s2, t))

def turns(s1, s2, t):
    return [play(s1 + 4, s2, t),
            play(s1, s2 + 4, t),
            play(s1 ** 2, s2, t),
            play(s1, s2 ** 2, t)]

for s in range(1, 96):
    if play(3, s, 0):
        print('19:', s)
        break

#20

def play(s1, s2,t):
    if s1 + s2 >= 100 or t > 5:
        return t == 3
    t += 1

    if t % 2 == 1:
        return any(turns(s1, s2, t))
    else:
        return all(turns(s1, s2, t))

num = []
for s in range(1, 96):
    if play(3, s, 0):
        num.append(s)
print('20:', num[0] + num[-1])



#21

def play(s1, s2,t):
    if s1 + s2 >= 100 or t > 5:
        return t == 2 or t == 4
    t += 1

    if t % 2 == 1:
        return all(turns(s1, s2, t))
    else:
        return any(turns(s1, s2, t))

for s in range(1, 96):
    if play(3, s, 0):
        print(s)
# print('21: 4')




#22

print('22: 13')



#23

def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    if x > y:
        return f(x - 1, y) + f(x - 2, y) + f(x // 2, y)
print('23:', f(33, 25) * f(25, 20) * f(20, 15) * f(15, 3))


#24

with open('24.txt') as f:
    f = f.readline()

count = 0
for i in range(len(f) - 9):
    if f[i] == 'E':

        l = 1
        for j in range(1, 10):
            if f[i + j] in 'ABCDEF':
                l += 1
            if f[i + j] == 'F' and 6 <= l <= 9:
                count += 1
print('24:', count)



#25


def d(n):
    s = set()
    count = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s.add(i)
            count += 1
            if n % (n // i) == 0:
                s.add(n // i)
                count += 1
    s = sorted(s)
    if count < 5:
        return 0
    else:
        return s[-5]

count = 0
a = ''
for n in range(200_000_001, 200_000_000_000):
    if count == 5:
        break
    if d(n) > 0:
        count += 1
        a += str(d(n)) + ' '
print('25:', a)


#26

print('26: 45 12999')